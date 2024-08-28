# OSGEM: Open Source Geo-spatial Energy Modeller

# Scope

This repository contains the source code of the Open Source Geo-spatial Energy Modeller (OSGEM), a hybrid modelling tool comprising of code from ([OSeMOSYS](http://www.osemosys.org/)), specifically from an OSeMOSYS-PuLP implementation by the [State_of_Goa](https://github.com/robertodawid/State_of_Goa)) repository, and ([OnSSET](http://www.onsset.org/)).

This model was applied to a country case of Burkina Faso and was created in conjuction with a Master's thesis by the author. Data for that case can be found in this repository and the thesis can be found here (link to be added upon thesis completion).

## Input data

This modeller requires three input files, one for OSeMOSYS modelling and two for OnSSET modelling. The following will describe the changes that were made in order to make OSGEM work as a hybrid model.

### OSeMOSYS Input file

The input data is a **.xlsx* file found in the default location of:
```
./model/OSeMOSYS_Input_Data/
```
The user is free to change the location of where the input is located. The input data contains all the parameters necessary to run the optimization. The documentation regarding the parameters is similar to that found in the original version [OSeMOSYS-GNU](https://osemosys.readthedocs.io/en/latest/) as referred to in the State_of_Goa implementation. Additional parameters are needed to calculate the LCOE from OSeMOSYS in this modeller and are described in the [docs](https://github.com/genius487/osgem/blob/main/docs.rst).

### OnSSET Input files

To be written

## Installation

OSGEM requires Python > 3.9 and a number of different packages, and can be installed by doing the following, assuming a fresh install of Anaconda. ([Miniconda](https://docs.anaconda.com/miniconda/) is the lightest distribution of Anaconda). At this end of this, you will have an environment in which to do your modelling. After opening an Anaconda prompt, run:

```
conda install git
git clone https://github.com/genius487/osgem.git
cd osgem
conda env create -n osgem -f environment.yml
```

## Run the model

From the ```osgem``` folder:

```
conda activate osgem
cd model
python osgem.py
```

## Output and Visualization

OSGEM yields results from the OSeMOSYS and OnSSET portions of code. The result files are of the same format in this modeller as they are in both tools. The OSeMOSYS results are outputted as a CSV or Excel file, from which a pivot table can be made of the results for subsequent table making and graphing. The OnSSET results are outputted as a series of CSV files where that data can be collected and transformed. The geo-spatial data can be plotted using QGIS (or Geopandas) for visualization. See relevant OSeMOSYS and OnSSET documentation for more.

## More Information
More on how OSeMOSYS works can be found in the [OSeMOSYS ReadTheDocs](https://osemosys.readthedocs.io/en/latest/) and more on OnSSET can be found in the more [OnSSET ReadTheDocs](https://onsset.readthedocs.io/en/latest/) or in the [GEP-OnSSET documentation](https://github.com/global-electrification-platform/gep-onsset/tree/master/docs/source) on Github. More about the tool could be found in the associated thesis or I can be contacted at samonthompson@yahoo.com.
