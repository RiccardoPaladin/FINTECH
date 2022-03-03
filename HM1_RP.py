"""
HOMEWORK 1 - Riccardo Paladin
FA 595 - Financial Technology
"""

import numpy as np
import matplotlib.pyplot as plt


def sin_cos(x):
    """
    :param x: Interval of period
    :return: Sin and Cos plot
    """
    s = np.sin(x)
    c = np.cos(x)
    plt.plot(x, s, x, c)                   # Plot with sin and cos
    plt.title('Plot of sin and cos')       # Title
    plt.xlabel('Periods')                  # Label X
    plt.ylabel('Sin and Cos')              # Label Y
    plt.legend(['sin(x)', 'cos(x)'])       # Legend
    plt.show()

x = np.arange(0,2*np.pi,0.01)
sin_cos(x)



