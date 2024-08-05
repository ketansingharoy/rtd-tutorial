Welcome to SeisScan Documentation!
==================================

.. image:: ../../SMU_logo.png
    :width: 100

.. image:: ../../SeisScan_fig.png
    :width: 600

**SeisScan** is an open source Python package to detect and locate microearthquakes. The method leverages the signal coherence across clusters of seismic stations to generate characteristic functions that are backprojected (migrated) to detect and locate seismic events. The following table of content contains infomation to install and use the package.

.. note::

   This project is under active development.

Contents
--------

.. toctree::
   :maxdepth: 2

   Installation
   Data Structure
   Tuning SeisScan
      Choice of minimum interstation distance and frequency range of interest (Coherency analysis)
      Choice of sliding window length for estimating Peak Cross-correlation Function
      Choice of maximum interstation distance
      Subnetwork selection and characteristic function
   Backprojection
      Prepare travel time lookup table
      Detection and location
   API

Indices and tables
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
