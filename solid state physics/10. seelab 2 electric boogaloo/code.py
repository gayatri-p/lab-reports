import numpy as np
import matplotlib.pyplot as plt
import eyes17.eyes
from scipy.stats import linregress

# Connect with the Seelab module
board = eyes17.eyes.open()
board.set_pv1(4) # set 4 V to PV1

def readV1(file, T):
    # function to write the temperature (manual) and corresponding V1 value to a file
    with open(file, "a") as f:
        v1 = board.get_voltage('A3')
        print(str(v1))
        f.write(f'{T} {v1}\n')

# taking readings
temp = 56 # Celcius
readV1('out.txt', temp)

# 
def straight_line(x, m, c): return m*x+c
def fit_line(xs, ys):
    popt = linregress(xs, ys)
    xFit = np.arange(min(xs), max(xs), 2e-6)

    label = f'For the best fit line (r-value = {popt.rvalue**2:.3f}):\nslope = {popt.slope:.3e} ± {popt.stderr:.3e}'  + f'\nintercept = {popt.intercept:.3e} ± {popt.intercept_stderr:.3e}' 
    return xFit, straight_line(xFit, popt.slope, popt.intercept), (popt.slope, popt.intercept), (popt.stderr, popt.intercept_stderr), label