# Changes

This documentation describes the main changes made in this modeller as compared to the files found in the State of Goa and OnSSET repositories.

## OSeMOSYS_PULP_Model.py
In the `LOAD DATA` section, functionality was added to accept demand data from OnSSET results to the appropriate OSeMOSYS parameter and fuel.

## OSeMOSYS_PULP_functions.py
The `getDiscountFactors` and `getLCOE` functions were added to facilitate the calculated of the LCOEs from the OSeMOSYS results.

## onsset.py
In the `calibrate_elec_current` function, the functionality was changed to operate as it does in the original onsset.py in the calibration process, *for the first scenario/LCOE period* , and for subsequent periods the `ElecPop` column in the GIS file is copied to the `ElecPopCalib` column. The appropriate start year electrification rates for the total, urban, and rural populations are calculated.

## Postprocessing.py
To be written

## runner.py
To be written

## specs.py
No changes
