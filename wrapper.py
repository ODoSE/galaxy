#!/usr/bin/env python
"""Module to generically wrap modules contained in divergence package for usage from within Galaxy.
First command line argument is a module within the divergence package, e.g: "divergence.translate".
Further arguments are passed to the named module's main method."""

__author__ = "Tim te Beek"
__contact__ = "brs@nbic.nl"
__copyright__ = "Copyright 2011, Netherlands Bioinformatics Centre"
__license__ = "MIT"

#First argument contains fully qualified name of module to be imported
import sys
NAME = sys.argv[1]
PACKAGE = 'divergence'
try:
    MODULE = __import__(NAME, fromlist = [PACKAGE])
except ImportError as ie:
    print('Could not import {0} from {1}'.format(NAME, PACKAGE))

#Second argument contains name of logging output file to use
import logging
FILE_HANDLER = logging.FileHandler(sys.argv[2], mode = 'w')
FILE_HANDLER.setFormatter(logging.Formatter())
FILE_HANDLER.setLevel(logging.INFO)
logging.root.addHandler(FILE_HANDLER)

try:
    #Run main method within module with remaining arguments
    if sys.argv[3:]:
        MODULE.main(sys.argv[3:])
    else:
        MODULE.main()
except SystemExit:
    #Do not report SystemExit errors to FogBugz: Just exit
    raise
except:
    #Should any other error occur, report it to FogBugz automatically
    from bugzscout import report_error_to_fogbugz
    MESSAGE = report_error_to_fogbugz()
    logging.info('Automatic bug submission reported: %s', MESSAGE)
    raise
finally:
    #Always remove logging handler from root
    logging.root.removeHandler(FILE_HANDLER)

#Snippet to log available environment variables from inside a Galaxy tool: 
#for key in sorted($searchList[2].keys())
#silent   sys.stderr.write("\t{0} = {1} ({2})\n".format(str(key), str($searchList[2][key]), type($searchList[2][key])))
#end for
