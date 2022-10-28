# ===============================================
# ===============================================
# *\src\py_lib\tlos.py
# ===============================================
# ===============================================
#
# read os and computer details

import argparse

import wmi

parser = argparse.ArgumentParser( description = 'manual to this script' )

parser.add_argument( '--Computer_System' , type = bool , default = False )
parser.add_argument( '--Hardware' , type = bool , default = False )
parser.add_argument( '--Serial_Number' , type = bool , default = False )
# add args definition

args = parser.parse_args()
# save readin args to val args

if_get_CS = args.Computer_System
if_get_H  = args.Hardware
if_get_SN = args.Serial_Number
# save get_infos status

# ================================================================ #

system_info = wmi.WMI()

def get_Computer_System_info():
    for Computer_System in system_info.Win32_ComputerSystem():
        print( "> Computer Name:     %s" % Computer_System.Caption )
        print( "> User Name:         %s" % Computer_System.UserName )
# get Computer name, User name

def get_Hardware_info():
    device_num_count = 0
    for processor in system_info.Win32_Processor():
        print( "> CPU %d:             %s" % ( device_num_count , processor.Name.strip() ) )
        device_num_count += 1

    device_num_count = 0
    memsize_total = 0
    memlist = []

    for mem in system_info.Win32_PhysicalMemory():
        this_memsize = int( mem.Capacity )
        memsize_total += this_memsize / 1024 ** 3
        memlist.append( "> RAM %d Manufacture: %s" % ( device_num_count , mem.Manufacturer ) )
        memlist.append( "> RAM %d Model:       %s" % ( device_num_count , mem.PartNumber ) )
        memlist.append( "> RAM %d Size:        %.2fGB" % ( device_num_count , this_memsize / 1024 ** 3 ) )
        device_num_count += 1

    print( "> RAM total Size:    %.2fGB" % memsize_total )

    for i in memlist:
        print( i )

    device_num_count = 0

    for disk in system_info.Win32_DiskDrive():
        diskSize = int( disk.size )
        print("> Disk %d Model:      %s" % ( device_num_count , disk.Caption ) )
        print("> Disk %d Size:       %.2fGB" % ( device_num_count , diskSize / 1024 ** 3 ) )
        device_num_count += 1

    for Computer_Model in system_info.Win32_ComputerSystem():
        print( "> Manufacture:       %s" % Computer_Model.Manufacturer )
        print( "> Computer Model:    %s" % Computer_Model.model )

    device_num_count = 0

    for graphic_card in system_info.Win32_VideoController():
        print( "> GPU %d:             %s" % ( device_num_count , graphic_card.name ) )
        device_num_count += 1

def get_Serial_Number():
    print( "> Motherboard Serial-Number: %s" % system_info.Win32_BaseBoard()[0].SerialNumber.strip() )
    print( "> Processor Serial-Number:   %s" % system_info.Win32_Processor()[0].ProcessorID.strip() )
# get Motherboard and CPU Serial-Number
    
# ================================================================ #

if not ( if_get_CS or if_get_H or if_get_SN ): # no further flags is added
    if_get_CS = True
    if_get_H  = True
    if_get_SN = True

print()

if if_get_CS:
    get_Computer_System_info()
    print()

if if_get_H:
    get_Hardware_info()
    print()

if if_get_SN:
    get_Serial_Number()
    print()