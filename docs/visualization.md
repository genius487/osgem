# Visualization

This documentation provides things to note that the user should kno before using this script to visualize the geo-spatial results.

In the `utils` folder, there is a folder named `visual_files` where the shapefiles for the country outline are kept. Only the **.shp** and **.shx** shapefiles should be stored in this folder. You may find shapefiles from GADM's [website](https://gadm.org/).

Your results are unlikely to have each technology (ie. grid, stand-alone PV, mini-grind Wind, etc.) represented. In the script, you should comment out (with a `#` before the command) the lines that plot the results that do not appear in your CSV to prevent extra entries in the legend.

For best visibility of the results, you may need to adjust the `zlevel` parameter in the plotting commands to choose which technology should be shown on top of another, or the `s` parameter which affects the size on the point as it is plotted on the graph. Also, feel free to adjust the colours in the `code_colors` dictionary near to the top of the `visualize` function in the script.

The following table is a description of the parameters for the script.

| Parameter | Description | Data Type |
| --------- | ----------- | --------- |
| boundary_file_path | Path/location of the **.shp** shapefile of the country boundary | String/Text |
| results_folder_path | Path/location of the folder that contains the results CSVs | String/Text |
| results_csv | List of names of the CSV files that contain the results | List[string]/List of Text |
| map_folder | Path/location of the folder when the images are to be saved | String/Text |
| figure_title | List of textstrings representing the filenames of the images when saved, and the titles of the figures | List[string]/List of Text |
| year | List of years that the results represent | List[int]/List of Numbers |

