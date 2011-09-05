#!/usr/bin/env python
###
# Part of the Adaptive Divergence through Direction of Selection workflow.
# Copyright (C) 2011  Tim te Beek <tim.te.beek@nbic.nl>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###
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
import logging
FILE_HANDLER = logging.FileHandler(sys.argv[2], mode = 'w')
FILE_HANDLER.setFormatter(logging.Formatter())
FILE_HANDLER.setLevel(logging.INFO)
logging.root.addHandler(FILE_HANDLER)

#Run main method within module with remaining arguments
if sys.argv[3:]:
    MODULE.main(sys.argv[3:])
else:
    MODULE.main()
