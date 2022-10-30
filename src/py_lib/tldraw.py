# ===============================================
# ===============================================
# *\src\py_lib\tldraw.py
# ===============================================
# ===============================================
#
# 

import linecache

from draw_src.line_chart import line_chart

import argparse

parser = argparse.ArgumentParser( description = 'manual to this script' )

parser.add_argument( '--line' )
parser.add_argument( '--bar' )
# add args definition

args = parser.parse_args()
# save readin args to val args

if args.line:
    line_chart()

