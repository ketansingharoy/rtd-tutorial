Reading seismograms
===================

Reading seismograms from the ObsPy FDSN web service
---------------------------------------------------
The ``SeisScan.read`` function utilizes `FDSN web service client for ObsPy <https://docs.obspy.org/packages/obspy.clients.fdsn.html>`_ to request ``ObsPy.Stream`` object and station metadata (station coordinates and response information). Finally, it attaches the metadata information to each ``ObsPy.Trace`` of the ``Obspy.Stream`` object and returns the ``Obspy.Stream`` object.

Let's do the following example. In a python file or jupyter notebook cell, type the following commands.

Don't forget to replace "path-to-SeisScan-directory" by SeisScan absolute path.

>>> import sys
>>> from obspy import UTCDateTime
>>>
>>> SeisScan_path = "path-to-SeisScan-directory"
>>> sys.path.insert(0, SeisScan_path)
>>>
>>> import SeisScan as ss
