# Python and Matplotlib
# For my dissertation and publication, I use Python's matplotlib package to produce the plots. Here, I will briefly put the code that I use to get the exact plots in my publications.
# I am not sure if this is the best way to produce these plots, but this is the way that I did it
# This is the crude method. I'll be posting the proper method in a bit, using .csv files.
# This is also just one example of producing a plot for the thickness variable gathered from SCAPS-1D simulation

# install matplotlib, numpy, and scipy first

from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

# this is just a particular style. you can print(plt.style.available) to try different styles

plt.style.use('seaborn-v0_8-paper')

# put the main variable here, and the four important variables which are:
# v_oc, jsc, ff, pce
# if you want to go for further analysis, you can plot stuff like Nyquist plot too from SCAPS-1D results
# define the variables here

thickness = [..]
v_oc = [..]
jsc = [..]
ff = [..]
pce = [..]

# First, we make a scatter plot of the v_oc vs thickness. so, a scatter plot will be produced (no lines)

plt.scatter(thickness, v_oc)
plt.xlabel('Thickness (nm)')
plt.ylabel(r'Open-circuit Voltage, $V_{oc}$ (V)')
plt.title('Open-circuit voltage vs layer thickness')

# now, we want to make a smooth line because by default, matplotlib will plot straight lines from point to point
# but, we want a smooth line. so, we need to use interpolate and spline to produce a curve from the data points
# in ms excel, this simply means clicking the "smooth line chart" options when making a chart
# in python, you have to make a new curve which corresponds to the original xy data
# x_new, bspline, v_oc_new
thickness_new = np.linspace('minimum x', 'maximum x', 'number of data points; the higher the smoother')
bspline = interpolate.make_interp_spline(thickness, v_oc)
v_oc_new = bspline(thickness_new)

# plot it

plt.plot(thickness_new, v_oc_new, color='#c20a0a')

# produce a visual plot

plt.show()

