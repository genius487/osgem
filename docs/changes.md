# Changes

This documentation describes the main changes made in this modeller as compared to the files found in the State of Goa and OnSSET repositories.

## gui_runner.py and OSeMOSYS.py |> osgem.py
The main files from both tools were integrated into the main script that runs this hybrid modeller. osgem.py contains three sections:-
- the `percentdifference` function responsible for calculating the degree of change in the most current and most previous list of LCOEs or newly-electrified Annual Demands on the Grid by the Residential sector to determine if another run of OSeMOSYS or OnSSET should be performed,
- the `runOSGEM` function which performs the main work of the modelling. All the user-defined parameters for running a modelling is collected at the top, described in the docs. The OSeMOSYS portion of the script is ran first, which produces OSeMOSYS results. From these results, the LCOEs for each defined period are calculated. Next, these LCOEs are compared to the previous LCOEs calculated to determine if it is necessary to run the OnSSET portion of code. If it is necessary, the OnSSET calibration and scenario functions are run to generate the residential electricity demand on the grid, which is the output of this function. And Finally,
- the `main` function that allows the script to be executed from the terminal/command prompt. The `runOSGEM` function is executed from here and the demand results are compared to the previously generated demand results to determine if the `runOSGEM` function needs to be ran again. The script will run recursively until the tolerance level is met.

## OSeMOSYS_PULP_Model.py
In the `LOAD DATA` section, functionality was added to accept demand data from OnSSET results to the appropriate OSeMOSYS parameter and fuel.

## OSeMOSYS_PULP_functions.py
The `getDiscountFactors` and `getLCOE` functions were added to facilitate the calculated of the LCOEs from the OSeMOSYS results.

## onsset.py
In the `calibrate_elec_current` function, the functionality was changed to operate as it does in the original onsset.py in the calibration process, *for the first scenario/LCOE period* , and for subsequent periods the `ElecPop` column in the GIS file is copied to the `ElecPopCalib` column. The appropriate start year electrification rates for the total, urban, and rural populations are calculated.

## Postprocessing.py
No changes

## runner.py
The `scenario` function now analyzes one scenario per function run, as opposed to looping through all scenarios in the original version of the function. The hard coded parameters techno-economic parameters were replaced with with variables that the users can change in the `Specs`files. See the docs for more on that. An `update` function was also introduced to update the Specs and GIS files for the next scenario run, and to obtain new grid demand in that period to be added to OSeMOSYS. You can alter this function to change what parameters you want changed between runs.

## specs.py
No changes
