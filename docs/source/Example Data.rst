Example Data
============
In the entire tutorial, we shall use an example dataset returned by ``SeisScan.read_example`` function. The dataset contains event informatin (Quinones, 2021), waveform stream and station metadata from IRIS fullwaveform experiment in Oklahoma (Sweet et al., 2018).

>>> from obspy import UTCDateTime
>>> import SeisScan as ss
>>>
>>> event_dict, st_main, inventory, rs_list, model_name = ss.read_example()

The function returns four quantities which are described below.

  **event_dict** is a ``dictionary`` containing event information.

  **st_main** is an ``ObsPy.Stream`` with station metadata added.

  **inventory** is an ``ObsPy.Inventory`` of station metadata.

  **rs_list** is a ``Subnetworks`` or a list of ``Subnetwork``.

  **model_name** is an earth model name.

Let's extract the event information.

>>> evt0 = UTCDateTime(event_dict["evt0"])    # event origin time
>>> evlo = event_dict["evlo"]                 # event longitude
>>> evla = event_dict["evla"]                 # event latitude
>>> evdp = event_dict["evdp"]                 # event depth (km)
>>> mag = event_dict["mag"]                   # event magnitude



** References **

1. Quinones L. 2021. Tracking induced seismicity in the Fort Worth Basin, Texas and Northern Oklahoma using local and large‐N style arrays, Earth Sci. Theses and Dissertations 22 , available at https://scholar.smu.edu/hum_sci_earthsciences_etds/22.

2. Sweet J. R. Anderson K. R. Bilek S. L. Brudzinski M. Chen X. DeShon H. Hayward C. Karplus M. Keranen K., and Langston C., et al. 2018. A community experiment to record the full seismic wavefield in Oklahoma, Seismol. Res. Lett.  89, no. 5, 1923–1930, doi:https://doi.org/10.1785/0220180079.
