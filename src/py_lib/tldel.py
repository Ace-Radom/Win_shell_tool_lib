# ===============================================
# ===============================================
# *\src\py_lib\tldel.py
# ===============================================
# ===============================================
#
# delete one file or folder, if it exists

import argparse
from hashlib import new

import os
import sys
import shutil

parser = argparse.ArgumentParser( description = 'manual to this script' )

parser.add_argument( '--path'    , type = str  , default = ""    )
parser.add_argument( '--file'    , type = bool , default = False )
parser.add_argument( '--folder'  , type = bool , default = False )
# add args definition

args = parser.parse_args()
# save readin args to val args

if args.path == "":
    print( "> ERROR: File or Folder Path not given" )
    sys.exit()

if ( not args.file ) and ( not args.folder ):
    print( "> ERROR: Don't know what (file or folder) needs to be created" )
    sys.exit()

if args.file and args.folder:
    print( "> ERROR: Cannot create file and folder at the same time" )
    sys.exit()
# judge if error or illegal flags occur

# ================================================================ #

def del_folder( path ):
    folder = os.path.isdir( path )
    # check if this folder exists

    if folder:
        shutil.rmtree( path )
        # delete this folder and all folder adn files in this root folder
    else:
        print( "> Folder" + path + " doesn't exist" )

def del_file( path ):
    file = os.path.isfile( path )
    # check if this file exists

    if file:
        os.remove( path )
        # delete this file
    else:
        print ( "> File " + path + " doesn't exist" )

# ================================================================ #

new_path = args.path
# file / folder needs to be deleted

if not os.path.isabs( new_path ):
    new_path = os.path.abspath( new_path )
# if there's not one absolute path, get it absolute

if args.folder:
    del_folder( new_path )

if args.file:
    del_file( new_path )