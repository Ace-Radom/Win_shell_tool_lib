# ===============================================
# ===============================================
# *\src\py_lib\tlhash.py
# ===============================================
# ===============================================
#
# 

from ctypes.wintypes import tagRECT
import hashlib
from pickle import TRUE

import sys

import argparse

parser = argparse.ArgumentParser( description = 'manual to this script' )

parser.add_argument( '--MD5'          , type = bool , default = False )
parser.add_argument( '--SHA1'         , type = bool , default = False )
parser.add_argument( '--SHA256'       , type = bool , default = False )
parser.add_argument( '--SHA512'       , type = bool , default = False )
parser.add_argument( '--file'         , type = str  , default = ""    )
parser.add_argument( '--show_comment' , type = bool , default = True  )
# add args definition

args = parser.parse_args()
# save readin args to val args

if args.file == "":
    print( "> ERROR: File Path not given" )
    sys.exit()

file = args.file

target_set = False

if args.MD5:
    if target_set:
        print( "> ERROR: Cannot calculate two different Hash function in one time" )
        sys.exit()
    
    target_set = True

    target = hashlib.md5()

if args.SHA1:
    if target_set:
        print( "> ERROR: Cannot calculate two different Hash function in one time" )
        sys.exit()
    
    target_set = True

    target = hashlib.sha1()

if args.SHA256:
    if target_set:
        print( "> ERROR: Cannot calculate two different Hash function in one time" )
        sys.exit()
    
    target_set = True

    target = hashlib.sha256()

if args.SHA512:
    if target_set:
        print( "> ERROR: Cannot calculate two different Hash function in one time" )
        sys.exit()
    
    target_set = True

    target = hashlib.sha512()

with open( file , 'rb' ) as rFile:
    while True:
        data = rFile.read( 4096 )
        if not data:
            break
        target.update( data )
    
print( target.hexdigest() )