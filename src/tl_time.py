# ===============================================
# ===============================================
# *\src\py\com_serial.py
# ===============================================
# ===============================================
#
# tool to show local time now

import time

print()
print( "> time now:" , time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )
# print local time in format "Y-M-D H:M:S"
print()