# for testing
from sympy import *

z = symbols('z')
macd = [5, 3, 0, 2]
sig = [0, 4, 9, 0]
x_coor = [1, 2, 3, 4]
crosses = 0


for elem in range(len(macd) - 1):

    # calculating slope -> m
    macd_slope = (macd[elem + 1] - macd[elem]) / ((x_coor[elem + 1]) - x_coor[elem])
    print('mac slope on', x_coor[elem], 'iteration:', macd_slope)

    sig_slope = (sig[elem + 1] - sig[elem]) / ((x_coor[elem + 1]) - x_coor[elem])
    print('sig slope on', x_coor[elem], 'iteration:', sig_slope)

    print('-----------')

    # creating equation for macd and sig ONLY FOR TESTING NOT NEEDED IN FINALY VERSION
    macd_equat = (macd_slope * z) + (macd_slope * x_coor[elem]) + macd[elem]
    print('macd_equat on', x_coor[elem], 'iteration:', macd_equat)
    sig_equat = (sig_slope * z) + (sig_slope * x_coor[elem]) + sig[elem]
    print('sig_equat on', x_coor[elem], 'iteration:', sig_equat)

    print('-----------')

    b = (macd_slope * x_coor[elem]) + macd[elem]
    d = (sig_slope * x_coor[elem]) + sig[elem]

    print('b is:', b)
    print('d is:', d)

    print('-----------')

    if macd_slope == sig_slope:
        print('lines are parallel and there is no intersection!')

    else:
        x = (d - b) / (macd_slope - sig_slope)
        y = (macd_slope * x) + b
        print('x coor:', x)
        print('y coor:', y)
        print('-------------------------------------')
