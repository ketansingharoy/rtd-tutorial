Reading seismograms
===================

Reading seismograms from the ObsPy FDSN web service
---------------------------------------------------
The ``SeisScan.read_fdsn`` function utilizes `FDSN web service client for ObsPy <https://docs.obspy.org/packages/obspy.clients.fdsn.html>`_ to request ``ObsPy.Stream`` object and station metadata (station coordinates and response information). Finally, it attaches the metadata information to each ``ObsPy.Trace`` of the ``Obspy.Stream`` object and returns the ``Obspy.Stream`` object.

Let's do the following example. In a python file or jupyter notebook cell, type the following commands to import some important libraries.

.. note::

    Don't forget to replace "path-to-SeisScan-directory" by SeisScan absolute path.

>>> import sys
>>> from obspy import UTCDateTime
>>>
>>> SeisScan_path = "path-to-SeisScan-directory"
>>> sys.path.insert(0, SeisScan_path)
>>>
>>> import SeisScan as ss

Now, it's time to pull some data from IRIS FDSN with the following parameters.

>>> provider = "IRISPH5" # key string for FDSN web server
>>> network = "YW"
>>> station = "1002"
>>> location = ""
>>> channel = "DPZ"
>>> attach_coordinates = True
>>> attach_response = True
>>> starttime = UTCDateTime('2016-07-11 05:55:00')
>>> endtime = starttime + 60
