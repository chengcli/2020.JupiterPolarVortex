### Folder structure

~~~
 data/
  grassi_spc.csv # velocity profile of south polar cyclone
  grassi_npc.csv # velocity profile of north polar cyclone

 figs/
  grassi_velocity_fitting.[png/eps] # fitting to Grassi's observation
  plot_grassi.py # code to make grassi_velocity_fitting
~~~

### Comments
Grassi's observation of the polar cyclones are presented in

[Grassi, D., et al.](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2018JE005555)
"First Estimate of Wind Fields in the Jupiter Polar Regions From JIRAM‐Juno Images."
<br> Journal of Geophysical Research: Planets 123.6 (2018): 1511-1524.

The CSV data in the data folder are extracted from their Figure 6 (a,b) using
[WebPlotDigiter](https://automeris.io/WebPlotDigitizer/)
