# OSGEM: Open Source Geo-spatial Energy Modeller

# Scope

This repository contains the source code of the Open Source Geo-spatial Energy Modeller (OSGEM), a hybrid modelling tool comprising of code from ([OSeMOSYS](http://www.osemosys.org/)), specifically from an OSeMOSYS-PuLP implementation by the [State_of_Goa](https://github.com/robertodawid/State_of_Goa)) repository, and ([OnSSET](http://www.onsset.org/)).

This model was applied to a country case of Burkina Faso and was created in conjuction with a Master's thesis by the author. Data for that case can be found in this repository and the thesis can be found here (link to be added upon thesis completion).

## Installation

OSGEM requires Python > 3.9 and a number of different packages, and can be installed by doing the following, assuming a fresh install of Anaconda. ([Miniconda](https://docs.anaconda.com/miniconda/) is the lightest distribution of Anaconda). At this end of this, you will have an environment in which to do your modelling.

```
conda install git
git clone <insert .git link here>
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

## More Information
More on how OSeMOSYS works can be found in the [OSeMOSYS ReadTheDocs](https://osemosys.readthedocs.io/en/latest/) and more on OnSSET can be found in the more [OnSSET ReadTheDocs](https://onsset.readthedocs.io/en/latest/) or in the [GEP-OnSSET documentation](https://github.com/global-electrification-platform/gep-onsset/tree/master/docs/source) on Github. More about the tool could be found in the associated thesis or I can be contacted at samonthompson@yahoo.com.
