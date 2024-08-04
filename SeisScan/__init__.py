"""
SeisScan - Python library for microearthquake detection and location.
"""

__version__ = "0.1.0"

from .read_fdsn import read_fdsn, read_fdsn_inventory
from .read_data.read_example import read_example

__all__ = ['read_fdsn', 'read_fdsn_inventory', 'read_example']
