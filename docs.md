# Documentation

This documentation provides explanations for additional parameters added in OSGEM to create a functioning model only. For explanation of the other parameters, please see the ReadTheDocs links referred to in the README.

## OSeMOSYS
These parameters are found in the input file for the OSeMOSYS-PuLP portion of OSGEM.

| Parameter | Description | Unit |
| --------- | ----------- | ---- |
| LCOEResidInv[r,t,y] | Annualized investment cost of assets existing at the start of the model period before discounting. | Monetary units |
| LCOETagFuel[r,f,y] | Binary parameter tagging the fuels that contribute to energy that makes us the denominator in the LCOE formula. It has value 1 for the technologies contributing, 0 otherwise. | Dimensionless  |
| LCOETagTechnology[r,t,y] | Binary parameter tagging the technologies that contribute to costs that go into the numerator of the LCOE formula. It has value 1 for the technologies contributing, 0 otherwise. | Dimensionless  |




## OSGEM
These parameters are found in the main script that runs OSGEM (``osgem.py``) that the user's needs to edit in order to run the modeller.

| Parameter | Description | Unit |
| --------- | ----------- | ---- |
| arg_input | Supply the name of the OSeMOSYS input file | N/A |
| arg_solver | Supply the name of the solver. ```cbc``` is the default. Other ready options are ```cplex```, ```scip```, ```highs```, ```copt```, and ```gurobi``` | N/A |
| arg_output | Supply the output format, ```csv``` or ```excel``` | N/A |
| arg_input_dir_osemosys | Supply the name of the folder that contains the OSeMOSYS input files | N/A |
| arg_output_dir_osemosys | Supply the name of the folder will contains the OSeMOSYS output files (create the folder beforehand) | N/A |
| lcoe_start_years | List of years denoting the start of each period the LCOE is to be calculated for | N/A |
| lcoe_end_years | List of years denoting the (inclusive) end of each period the LCOE is to be calculated for | N/A |
| demand_parameter | Selection of which OSeMOSYS demand parameter the OnSSET-calculated demand will change, `SpecifiedAnnualDemand` or `AccumulatedAnnualDemand` | N/A | 
| fuel_name | Selection of which OSeMOSYS fuel/commodity the OnSSET-calculated demand will change as is named in the OSeMOSYS input file | N/A | 
| tolerance | Percetage as a decimal that the new OnSSET-calculated demand can differ from the previous OnSSET-calculated demand | Dimensionless | 
| kWhconverter | multiplier to converter kWh demand from OnSSET to your demand unit in OSeMOSYS | kWh / OSeMOSYS Fuel Units |
| lcoe_unit_conv | multiplier to converter LCOE unit from OSeMOSYS to the USD/kWh unit of OnSSET | USD/kWh / (OSeMOSYS Monetary Units/OSeMOSYS Fuel Units) | 
| onsset_input_folder | Supply the name of the folder that contains the OnSSET input files | N/A |
| onsset_results_folder | Supply the name of the folder that contains the OnSSET results files (create the folder beforehand) | N/A |
| onsset_summary_folder | Supply the name of the folder that contains the OnSSET result summary files (create the folder beforehand) | N/A |
| specs_file | Supply the name of the OnSSET specs file | N/A |
| specs_file_calib | Supply what will be the name of the OnSSET specs file after calibration | N/A |
| gis_files | Supply the list of names of the OnSSET GIS input files before calibration, where the first name in the list is a GIS file that already exists (corresponding to your first LCOE period), and the subsequent names are the pre-calibration GIS files that OSGEM will create for the subsequent LCOE periods in the analysis | N/A |
| gis_files_calib | Supply what will be the list of names of the OnSSET GIS input files after calibration | N/A |

