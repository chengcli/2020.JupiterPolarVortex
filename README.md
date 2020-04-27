### Folder structure

data/
  *velocity profile of south polar cyclone*
  grassi_spc.csv 
  *velocity profile of north polar cyclone*
  grassi_npc.csv

figs/
  *fitting to Grassi's observation* 
  grassi_velocity_fitting.[png/eps]

*code to make grassi_velocity_fitting*
plot_grassi.py

### Comments
Grassi's observation of the polar cyclones are presented in
Grassi, D., et al. "First Estimate of Wind Fields in the Jupiter Polar Regions From JIRAM‐Juno Images."
Journal of Geophysical Research: Planets 123.6 (2018): 1511-1524.

The CSV data in the data folder are extracted from their Figure 6 (a,b) using
[WebPlotDigiter](https://automeris.io/WebPlotDigitizer/)
