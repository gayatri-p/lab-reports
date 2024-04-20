import RigolWFM.wfm as rigol
import matplotlib.pyplot as plt

filename = 'advanced electronics/propagation delay report/wfm/d.wfm'
scope = 'DS1102E'

w = rigol.Wfm.from_file(filename, scope)
w.plot()
plt.show()