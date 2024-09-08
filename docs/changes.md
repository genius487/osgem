# Changes

This documentation describes the main changes made in this modeller as compared to the files found in the State of Goa and OnSSET repositories.

## OSeMOSYS_PULP_Model.py
To be written

## OSeMOSYS_PULP_functions.py
To be written

## onsset.py
In the `calibrate_elec_current` function, the functionality was changed to operate as it does in the original onsset.py in the calibration process, *for the first scenario/LCOE period* , and for subsequent periods the `ElecPop` column in the GIS file is copied to the `ElecPopCalib` column. The appropriate start year electrification rates for the total, urban, and rural populations are calculated.

## Postprocessing.py
To be written

## runner.py
To be written

## specs.py
No changes
