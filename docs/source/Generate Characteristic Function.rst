Generate Characteristic Function
================================

Read example data.

>>> from obspy import UTCDateTime
>>> import SeisScan as ss
>>>
>>> event_dict, st_main, inventory, subnetworks, model_name = ss.read_example()

Select Stream for the stations in the ``Subnetworks``.

>>> from obspy import Stream
>>>
>>> st = Stream()
>>> 
>>> for subnetwork in subnetworks:
>>>     reference = subnetwork["reference"]
>>>     secondaries = subnetwork["secondaries"]
>>>     
>>>     st += st_main.select(station=reference)
>>>     
>>>     for secondary in secondaries:
>>>         st += st_main.select(station=secondary)

Pre-process data.

>>> from obspy import Stream
>>>
>>> #--- take a copy of the selected stream
>>> st_proc = st.copy()
>>> 
>>> #--- detrend the data
>>> st_proc.detrend(type='linear');
>>> 
>>> #--- remove instrument response
>>> pre_filt = [0.1, 0.2, 200.0, 250.0]   # Hz
>>> st_proc.remove_response(output='VEL', pre_filt=pre_filt);
>>> 
>>> #--- rotation from 'Z12' to 'ZNE
>>> st_proc.rotate('->ZNE', inventory=inventory);
>>> 
>>> #--- filter
>>> f1, f2 = 25.0, 75.0
>>> st_proc.select(component='Z').filter('bandpass', freqmin=f1, freqmax=f2);
>>> 
>>> f1, f2 = 10.0, 30.0
>>> st_proc.select(component='N').filter('bandpass', freqmin=f1, freqmax=f2);
>>> st_proc.select(component='E').filter('bandpass', freqmin=f1, freqmax=f2);
>>> 
>>> #--- Merge traces with similar seed_id
>>> st_proc.merge(method=1, fill_value=0);
>>> 
>>> #--- Trim the stream so that every trace has similar starttime and endtime
>>> starttime = min([tr.stats.starttime for tr in st_proc])
>>> endtime = max([tr.stats.endtime for tr in st_proc])
>>> st_proc.trim(starttime, endtime, pad=True, fill_value=0);

Compute characteristic function (Local Similarity)

>>> import dask
>>> from dask.distributed import Client as dask_Client
>>>
>>> #--- start dask client for parallel processing
>>> n_workers = os.cpu_count() - 2
>>> dask_client = dask_Client(n_workers=n_workers)
>>>
>>> channels = ['DPZ', 'DPN', 'DPE']
>>> w = 0.75 # window length in seconds
>>> dt = 0.05 # stride in seconds
>>> max_lag = 0.1 # maximum lag in seconds
>>> 
>>> st_dls = Stream()
>>>
>>> for channel in channels:
>>>     _, _, _, _, _, st_dls_ = ss.do_ls(st_proc, channel, subnetworks=subnetworks, w=w, dt=dt, max_lag=max_lag, dask_client=dask_client)
>>>     st_dls += st_dls_
>>>
>>> #--- close dask client
>>> dask_client.close()
