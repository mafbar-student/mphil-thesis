from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

plt.style.use('seaborn-v0_8-paper')

defect_density = [2**12, 2**13, 2**14,2**15, 2**16, 2**17]
pce = [19.9322, 20.6711, 20.7923, 20.6839, 20.5136, 20.3728]

plt.scatter(defect_density, pce, marker='o' ,color='#c20a0a')
plt.xlabel(r'Defect density ($cm^{-3}$)')
plt.ylabel('Power conversion efficiency (%)')
plt.title('Power conversion efficiency vs defect density of active layer')

plt.xscale('log')
plt.plot(defect_density, pce, color='#c20a0a')
plt.show()