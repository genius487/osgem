"""Provides a GUI for the user to choose input files

This file runs either the calibration or scenario modules in the runner file,
and asks the user to browse to the necessary input files
"""

from utils.OSeMOSYS_PULP_functions import *
from utils.OSeMOSYS_PULP_Model import *
from utils.Postprocessing import *
import os
import datetime as dt
import getopt
import sys
import warnings
import tkinter as tk
import pandas as pd
import logging
import numpy as np
import random
from tkinter import filedialog, messagebox
warnings.filterwarnings("ignore")
from utils.runner import calibration, scenario
from openpyxl import load_workbook


def percentdifference(oldlist, newlist):
    """

    Arguments
    ---------
    oldlist : List[int]
    newlist : List[int]

    """

    diffs = []

    for x,y in zip(oldlist, newlist):
        if x == y:
            diffs.append(0)
        else:
            diffs.append(abs((y-x)/x))

    return diffs


def runOSGEM(onsset_demand=[]):
    """

    Arguments
    ---------
    onsset_demand : List[int]

    """

    ########################################################
    # USER-DEFINED-PARAMS
    ########################################################

    # OSeMOSYS
    arg_input = "bfa-pulp-bau.xlsx"
    arg_solver = "cbc"
    arg_output = "csv"
    arg_input_dir_osemosys = "OSeMOSYS_Input_Data"
    arg_output_dir_osemosys = "OSeMOSYS_Output_Data"

    lcoe_start_years = [2021, 2031, 2041, 2051, 2061]
    lcoe_end_years = [2030, 2040, 2050, 2060, 2070]

    demand_parameter = "SpecifiedAnnualDemand"
    fuel_name = "DEMRES002"
    tolerance = 0.01
    kWhconverter = 0.000001  # multiplier to converter kWh demand from OnSSET to your demand unit in OSeMOSYS
    lcoe_unit_conv = 0.000001  # multiplier to converter LCOE unit from OSeMOSYS to the sUSD/kWh unit of OnSSET

    # OnSSET
    onsset_input_folder = "./OnSSET_Input/bau/"
    onsset_results_folder = "./OnSSET_Output/bau/"  # Name of RESULTS folder to save outputs
    onsset_summary_folder = "./OnSSET_Output/bau/"  # Name of SUMMARIES folder to save outputs

    specs_file = "burkina-specs-bau.xlsx"  # Name of the specs file
    specs_file_calib = "burkina-specs-bau-calibrated.xlsx"  # Name of the calibrated specs file

    gis_files = ["Burkina_Faso_IRENA_final.csv",
                 "Burkina_Faso_IRENA_final_2030.csv",
                 "Burkina_Faso_IRENA_final_2040.csv",
                 "Burkina_Faso_IRENA_final_2050.csv",
                 "Burkina_Faso_IRENA_final_2060.csv"]  # Names of GIS files

    gis_files_calib = ["Burkina_Faso_IRENA_final_calibrated.csv",
                       "Burkina_Faso_IRENA_final_2030_calibrated.csv",
                       "Burkina_Faso_IRENA_final_2040_calibrated.csv",
                       "Burkina_Faso_IRENA_final_2050_calibrated.csv",
                       "Burkina_Faso_IRENA_final_2060_calibrated.csv"]  # Names of calibrated GIS files

    # ----------------------------------------------------------------------------------------------------------------------
    #	OSeMOSYS SETUP - DATA SOURCES and MONTE CARLO SIMULATION
    # ----------------------------------------------------------------------------------------------------------------------

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info(f"\t{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\tOSeMOSYS-PuLP-HP started.")

    # Input data
    inputFile = arg_input
    if 'txt' in str(arg_input):
        inputDir = "data"
    else:
        inputDir = arg_input_dir_osemosys

    outputDir = arg_output_dir_osemosys
    if arg_output == 'csv':
        outputDir = arg_output_dir_osemosys
    if arg_output == 'excel':
        outputDir = arg_output_dir_osemosys
    solver = arg_solver

    if 'txt' in str(arg_input):
        otoole = True
    else:
        otoole = False

    # ----------------------------------------------------------------------------------------------------------------------
    #    LOAD DATA
    # ----------------------------------------------------------------------------------------------------------------------

    # Convert demand units from kWh to the unit of the OSeMOSYS model
    onsset_demand = [i * kWhconverter for i in onsset_demand]

    # Run and obtain results from OSeMOSYS
    res_df, df, sets_df, defaults_df = OSeMOSYS_PULP_Model(inputFile, inputDir, solver, otoole, onsset_demand, demand_parameter, fuel_name)

    # Calculate the LCOE for the user-defined periods
    res_df, new_lcoes = getLCOE(res_df, df, sets_df, defaults_df, lcoe_start_years, lcoe_end_years)

    # Convert LCOE units from the resultant units in OSeMOSYS to the USD/kWh of OnSSET
    new_lcoes = [i * lcoe_unit_conv for i in new_lcoes]

    # res_df.to_csv('res.csv')
    modelName = inputFile.split('.')[0]

    # CSV
    if arg_output == 'csv':
        outputFileCSV = f"{modelName}_results.csv"
        saveResultsToCSV(res_df, outputDir, outputFileCSV)

    # Excel
    if arg_output == 'excel':
        outputFileExcel = f"{modelName}_results.xlsx"
        saveResultsToExcel(res_df, outputDir, outputFileExcel)

    logging.info(f"\t{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t"
                 f"All results are saved now.")

    # Print out LCOE for each period with the associated end year
    print("The LCOEs for the periods are as follows:")
    for i in range(len(lcoe_end_years)):
        print(lcoe_end_years[i], ": ", new_lcoes[i])

    # ----------------------------------------------------------------------------------------------------------------------
    #    ONSSET
    # ----------------------------------------------------------------------------------------------------------------------

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    specs_path = onsset_input_folder + specs_file
    specs_path_calib = onsset_input_folder + specs_file_calib

    gis_files_path = [onsset_input_folder + name for name in gis_files]
    gis_files_calib_path = [onsset_input_folder + name for name in gis_files_calib]

    # Insert/Update LCOEs into OnSSET from OSeMOSYS

    scenario_parameters = pd.read_excel(specs_path, sheet_name='ScenarioParameters')

    # Check to see if LCOEs have changed significantly between runs

    if onsset_demand != []:
        old_lcoes = scenario_parameters["GridGenerationCost"].to_list()
    else:
        old_lcoes = [100 for i in new_lcoes]

    if all(i < tolerance for i in percentdifference(old_lcoes, new_lcoes)):
        logging.info("The LCOEs from the previous run are sufficiently close to the LCOEs from the current run. "
                     "Therefore, Model is optimized")
        return 1, onsset_demand
    else:
        scenario_parameters["GridGenerationCost"] = new_lcoes

        book = load_workbook(specs_path)
        writer = pd.ExcelWriter(specs_path, engine='openpyxl')
        writer.book = book
        std = book.get_sheet_by_name('ScenarioParameters')
        book.remove_sheet(std)
        scenario_parameters.to_excel(writer, sheet_name='ScenarioParameters', index=False)
        #writer.save()
        writer.close()

    # Initialize list for new residential demand from OnSSET

    onsset_annual_new_demand = []

    # Perform Analysis for each period

    for scen in range(len(lcoe_end_years)):
        print('\n Analyzing the period ending in {}'.format(lcoe_end_years[scen]))

        # Perform calibration

        calibration(specs_path, gis_files_path[scen], specs_path_calib, gis_files_calib_path[scen], scen)

        # run scenario(s)

        scenario_demand = scenario(specs_path_calib, gis_files_calib_path[scen], onsset_results_folder,
                                   onsset_summary_folder, scen, specs_path, gis_files_path)

        onsset_annual_new_demand += scenario_demand

    onsset_cumulative_new_demand = list(np.cumsum(onsset_annual_new_demand))

    return 0, onsset_cumulative_new_demand #kWh


if __name__ == "__main__":

    onsset_new_resid_demand_old = []
    tolerance = 0.01

    run_model = True
    loop = 0

    while run_model:
        loop += 1
        print(f"\n ITERATION {loop}")
        is_optimized, onsset_new_resid_demand_new = runOSGEM(onsset_new_resid_demand_old)

        # EXTRA: necessary for my models as capacity cannot grow in the first 3 years of the OSeMOSYS model
        onsset_new_resid_demand_new[0:2] = [0, 0, 0]

        if is_optimized == 1:
            run_model = False
        else:

            if len(onsset_new_resid_demand_old) == len(onsset_new_resid_demand_new):
                if all(i < tolerance for i in percentdifference(onsset_new_resid_demand_old, onsset_new_resid_demand_new)):
                    logging.info("Model is optimized")
                    run_model = False

            onsset_new_resid_demand_old = onsset_new_resid_demand_new

