Example Data
============
In the entire tutorial, we shall use an example dataset returned by ``SeisScan.read_example`` function.

>>> import SeisScan as ss
>>> event_dict, st_main, inventory, rs_list, model_name = ss.read_example()

The function returns four quantities which are described below.

  **event_dict** is a ``dictionary`` containing event information.

  **st_main** is an ``ObsPy.Stream`` with station metadata added.

  **inventory** is an ``ObsPy.Inventory`` of station metadata.

  **rs_list** is a ``Subnetworks`` or a list of ``Subnetwork``.

  **model_name** is an earth model name.

Let's extract information

>>> evt0 = UTCDateTime(event_dict["evt0"])
>>> evlo = event_dict["evlo"]
>>> evla = event_dict["evla"]
>>> evdp = event_dict["evdp"]
>>> mag = event_dict["mag"]
