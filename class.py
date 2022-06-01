import tools, plots, utils
from core import selections
import matplotlib.pyplot as plt

class Filter:
    def __init__(self, filter):
        self.filename, self.ID, self.data, self.T, self.DC_T, self.DC_R, self.TReadout, self.RReadout = tools.process_data(filter)
    
    def plot_T(self):
        plots.draw_T(self.data, self.DC_T, self.ID)

    def plot_R(self):  
        plots.draw_R(self.data, self.TReadout, self.RReadout, self.DC_T, self.DC_R, self.ID)
    
    def plot_A(self):
        plots.draw_A(self.data, self.TReadout, self.RReadout, self.DC_T, self.DC_R, self.ID)

    def plot_QE(self):
        plots.draw_QE(self.TReadout, self.RReadout)

plt.figure()
pe = Filter({"FilterID":"PE2.1"})
opto = Filter({"FilterID":"OPTO1.1"})
pe.plot_A()
plt.show(block=True)