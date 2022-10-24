# ===============================================
# ===============================================
# *\src\py_lib\tlnew.py
# ===============================================
# ===============================================
#
# create one file, if this file doesn't exist

import argparse

import os
import sys

parser = argparse.ArgumentParser( description = 'manual to this script' )

parser.add_argument( '--path'    , type = str  , default = ""    )
parser.add_argument( '--file'    , type = bool , default = False )
parser.add_argument( '--folder'  , type = bool , default = False )
parser.add_argument( '--overlay' , type = bool , default = False )
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

def create_folder( path ): # create folder
    folder = os.path.isdir( path )
    # check if this folder already exists

    if not folder:
        os.makedirs( path )
    else:
        print( "> Folder " + path + " already exists" )

def create_file( path ): # create file
    file = os.path.isfile( path )
    # check if this file already exists

    if not file:
        parentdir = os.path.dirname( path )
        if not os.path.exists( parentdir ):
            os.makedirs( parentdir )
        # if there's one not created folder in this path, create it

        open( path , 'w' ).close()
    else:
        print( "> File " + path + " already exists" )

new_path = args.path
# created file / folder path

# ================================================================ #

if not os.path.isabs( new_path ):
    new_path = os.path.abspath( new_path )
# if there's not one absolute path, get it absolute

#print( new_path )
# debug line

if args.folder:
    create_folder( new_path )

if args.file:
    create_file( new_path )