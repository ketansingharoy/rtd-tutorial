Installation
############

Create a new conda environment
::
    conda create -n SeisScan python=3.10

Activate the environment
::
    conda activate SeisScan

Install dependencies
::
    conda install -c conda-forge numpy, scipy, matplotlib, cartopy, pandas, utm, obspy, dask

Add SeisScan to python path
::
    >>> import sys
    >>> sys.path.insert(0, "path to SeisScan")
