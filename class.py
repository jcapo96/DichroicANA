import tools, plots
from core import selections
import matplotlib.pyplot as plt

class Filter:
    def __init__(self, filter):
        self.filename, self.ID, self.data, self.T, self.DC_T, self.DC_R = tools.process_data(filter)
    
    def plot_T(self):
        plots.draw_T(self.data, self.DC_T, self.ID)

plt.figure()
pe = Filter({"FilterID":"PE2.1"})
opto = Filter({"FilterID":"OPTO1.1"})
pe.plot_T()
opto.plot_T()
plt.show(block=True)