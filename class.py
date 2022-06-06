import tools, plots, utils
from core import selections
import pandas as pd
import csv
import matplotlib.pyplot as plt

class Filter:
    def __init__(self, filter):
        self.filename, self.angles, self.ID, self.data, self.T, self.DC_T, self.DC_R, self.TReadout, self.RReadout = tools.process_data(filter)

    def plot_T(self):
        plots.draw_T(self.data, self.DC_T, self.ID)
        plt.title("PE vs OPTO: " + str(self.angles) + " º")

    def plot_R(self):  
        plots.draw_R(self.data, self.TReadout, self.RReadout, self.DC_T, self.DC_R, self.ID)
    
    def plot_A(self):
        plots.draw_A(self.data, self.TReadout, self.RReadout, self.DC_T, self.DC_R, self.ID)

    def plot_QE(self):
        plots.draw_QE(self.TReadout, self.RReadout)

class FilterCIEMAT:
    def __init__(self, filter):
        self.fnameCIEMAT, self.dataCIEMAT = tools.process_ciemat(filter)
    
    def plot_ciemat(self, angle):
        plots.draw_ciemat(self.dataCIEMAT, angle)

plt.figure()
pe = Filter({"FilterID":"PE2.1"})
opto = Filter({"FilterID":"OPTO1.1"})
pe_ciemat2 = FilterCIEMAT({"FilterID":"PE2.3","Angle":"35-50"})
pe_ciemat2.plot_ciemat("45_M1")
# pe.plot_T()
# opto.plot_T()
# pe_ciemat2.plot_ciemat("00_M2")
# pe_ciemat2.plot_ciemat("15_M1")
# pe_ciemat2.plot_ciemat("30_M1")
# pe_ciemat.plot_ciemat("45_M1")
plt.grid("on")
plt.show(block=True)