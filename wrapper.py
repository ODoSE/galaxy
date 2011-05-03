"""Module to generically wrap modules contained in divergence package for usage from within Galaxy.
First command line argument is a module within the divergence package, e.g: "divergence.translate".
Further arguments are passed to the named module's main method."""
import sys
NAME = sys.argv[1]
PACKAGE = 'divergence'
try:
    MODULE = __import__(NAME, fromlist = [PACKAGE])
except ImportError as ie:
    print('Could not import {0} from {1}'.format(NAME, PACKAGE))
MODULE.main(sys.argv[2:])
