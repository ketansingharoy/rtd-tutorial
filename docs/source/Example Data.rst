Example Data
============
In the entire tutorial, we shall use an example dataset returned by ``SeisScan.read_example`` function.

>>> import SeisScan as ss
>>> event_dict, st_main, inventory, rs_list, model_name = ss.read_example()

``event_dict`` is a ``dictionary`` containing event information. Let us extract them.

>>> evt0 = UTCDateTime(event_dict["evt0"])
>>> evlo = event_dict["evlo"]
>>> evla = event_dict["evla"]
>>> evdp = event_dict["evdp"]
>>> mag = event_dict["mag"]
