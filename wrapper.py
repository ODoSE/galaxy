"""Module to generically wrap modules contained in divergence package for usage from within Galaxy.
First command line argument is a module within the divergence package, e.g: "divergence.translate".
Further arguments are passed to the named module's main method."""
#First argument contains fully qualified name of module to be imported
import sys
NAME = sys.argv[1]
PACKAGE = 'divergence'
try:
    MODULE = __import__(NAME, fromlist = [PACKAGE])
except ImportError as ie:
    print('Could not import {0} from {1}'.format(NAME, PACKAGE))
    
#Second argument contains name of logging output file to use
import logging as log
file_handler = log.FileHandler(sys.argv[2], mode='w')
log.root.addHandler(file_handler)

#Run main method within module with remaining arguments
MODULE.main(sys.argv[3:])
