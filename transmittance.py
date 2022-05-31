import pandas as pd
import numpy as np
import os, glob
import matplotlib.pyplot as plt

path = os.path.dirname(os.getcwd())
path_sample = glob.glob(path + "/**/" + "Sample_OPTO_30052022.txt", recursive = True)[0]
path_reference = glob.glob(path + "/**/" + "Reference_OPTO_30052022.txt", recursive = True)[0]
path_open = glob.glob(path + "/**/" + "Open_OPTO_30052022.txt", recursive = True)[0]
Sample = pd.DataFrame(pd.read_csv(str(path_sample), encoding= 'unicode_escape', sep='\t', header=0))
Reference = pd.DataFrame(pd.read_csv(str(path_reference), encoding= 'unicode_escape', sep='\t', header=0))
Open = pd.DataFrame(pd.read_csv(str(path_open), encoding= 'unicode_escape', sep='\t', header=0))

path_sample_pe = glob.glob(path + "/**/" + "Sample_PE_30052022.txt", recursive = True)[0]
path_reference_pe = glob.glob(path + "/**/" + "Reference_PE_30052022.txt", recursive = True)[0]
path_open_pe = glob.glob(path + "/**/" + "Open_PE_30052022.txt", recursive = True)[0]
Sample_pe = pd.DataFrame(pd.read_csv(str(path_sample_pe), encoding= 'unicode_escape', sep='\t', header=0))
Reference_pe = pd.DataFrame(pd.read_csv(str(path_reference_pe), encoding= 'unicode_escape', sep='\t', header=0))
Open_pe = pd.DataFrame(pd.read_csv(str(path_open_pe), encoding= 'unicode_escape', sep='\t', header=0))

names = ["Date", "WL", "AV", "ERR", "DEG"]
Sample.columns = names
Reference.columns = names
Open.columns = names

Sample_pe.columns = names
Reference_pe.columns = names
Open_pe.columns = names

sample_corr = Sample["AV"]-Open["AV"]
sample_err = np.sqrt(Sample["ERR"]**2 + Open["ERR"]**2)
reference_corr = Reference["AV"]-Open["AV"]
transmittance = 100*(sample_corr/reference_corr)

sample_corr_pe = Sample_pe["AV"]-Open_pe["AV"]
sample_err_pe = np.sqrt(Sample_pe["ERR"]**2 + Open_pe["ERR"]**2)
reference_corr_pe = Reference_pe["AV"]-Open_pe["AV"]
transmittance_pe = 100*(sample_corr_pe/reference_corr_pe)

plt.plot(Sample["WL"], transmittance, "o", markersize=10, label="OPTO 45º")
plt.plot(Sample_pe["WL"], transmittance_pe, "s", markersize=10, label="PE_SET2 45º")
plt.title("Comparison OPTO vs PE_SET2")
plt.xlabel("Wavelength (nm)", fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0,100)
plt.ylabel("Transmittance (%)", fontsize=20)
plt.grid("on")
plt.legend(loc="best")
plt.show(block=True)