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
    
    def plot_ciemat(self, filename, angle):
        plots.draw_ciemat(filename, angle)

plt.figure()
pe = Filter({"FilterID":"PE2.1"})
opto = Filter({"FilterID":"OPTO1.1"})
pe.plot_T()
opto.plot_T()
opto.plot_ciemat("20220601_DUNE_Filtro_Dicroico_70capas_0_35", "00_M2")
opto.plot_ciemat("20220601_DUNE_Filtro_Dicroico_70capas_0_35", "15_M1")
opto.plot_ciemat("20220601_DUNE_Filtro_Dicroico_70capas_0_35", "30_M1")
opto.plot_ciemat("20220601_DUNE_Filtro_Dicroico_70capas_0_35_50", "45_M1")
plt.xlim(410, 550)
plt.ylim(0,10)
plt.yticks(range(0,10))
plt.show(block=True)