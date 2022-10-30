# ===============================================
# ===============================================
# *\src\py_lib\draw_src\line_chart.py
# ===============================================
# ===============================================
#
# 

import numpy as np

import matplotlib.pyplot as plt

def line_chart():
    while True:
        shell_in = input( "> " )

        if shell_in == "end":
            break
        # end of readin

        if shell_in == "new line":
            xlist = []
            ylist = []

            while True:
                x , y = input( "> x, y point: " ).split()
                # read in [x|y]

                if x == 'e': # e is the break mark for reading in [x|y]
                    break
                else:
                    xlist.append( float ( x ) )
                    ylist.append( float ( y ) )

            xlistnp = np.array( xlist )
            ylistnp = np.array( ylist )

            c = input( "> line colour: ") # get line colour
            ls = input( "> line style: " ) # get line style
            l = input( "> line label: " ) # get line label
            
            plt.plot( xlistnp , ylistnp , label = l , color = c , linestyle = ls )
            # draw line
        
        if shell_in == "title":
            title = input( "> title: " )
            title_pos = input( "> title position: " )
            title_c = input( "> title colour: " )
            title_s = input( "> title size: " )
            plt.title( title , loc = title_pos , color = title_c , size = title_s )
        # set title

        if shell_in == "x-label":
            x = input( "> label: " )
            x_pos = input( "> label position: " )
            plt.xlabel( x , loc = x_pos )
        
        if shell_in == "y-label":
            y = input( "> label: " )
            y_pos = input( "> label position: " )
            plt.ylabel( y , loc = y_pos )
        # set labels for x/y-axis

        if shell_in == "grid":
            plt.grid()

    plt.legend()
    plt.show()