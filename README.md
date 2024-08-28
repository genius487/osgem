# OSGEM: Open Source Geo-spatial Energy Modeller

conda env create -f -n osgem environment.yml

# Scope

This repository contains the source code of the Open Source Geo-spatial Energy Modeller (OSGEM), a hybrid modelling tool comprising of code from ([OSeMOSYS](http://www.osemosys.org/)), specifically from an OSeMOSYS-PuLP implementation by the [State_of_Goa](https://github.com/robertodawid/State_of_Goa)) repo, and ([OnSSET](http://www.onsset.org/)).


The repository also includes sample test files available in ```.\test_data```
and sample output files available in ```.\sample_output```.

## Installation

### Requirements

OnSSET requires Python > 3.5 with the following packages installed:
- et-xmlfile
- jdcal
- numpy
- openpyxl
- pandas
- python-dateutil
- pytz
- six
- xlrd
- notebook
- seaborn
- matplotlib
- scipy

### Install with pip

Install onsset from the Python Packaging Index (PyPI):

```
pip install onsset
```

### Install from GitHub

Download or clone the repository and install the package in `develop`
(editable) mode:

```
git clone https://github.com/onsset/onsset.git
cd onsset
python setup.py develop
```

## Contact
For more information regarding the tool, its functionality and implementation
please visit https://www.onsset.org or contact the development team
at seap@desa.kth.se.