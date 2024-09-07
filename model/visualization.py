import geopandas
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
import numpy as np

def visualize(boundary_file, results_csv, end_year, output_folder, fig_title):
	print("Mapping "+fig_title)

	res_df = pd.read_csv(results_csv)

	final_elec_code = 'FinalElecCode' + str(end_year)

	#Select from the full results, the FinalElecCode in the end year for that scenario along with the coordinates

	res_df = res_df[['X_deg', 'Y_deg', final_elec_code]]
	res_gdf_dict = {}

	code_colors = {1: 'tab:cyan',
				   2: 'tab:orange',
				   3: 'tab:green',
				   4: 'tab:red',
				   5: 'mediumorchid',
				   6: 'tan',
				   7: 'tab:pink',
				   8: 'tab:olive',
				   99: 'tab:gray'}

	# Separate that selection by Code (1-8,99)
	
	for code in code_colors:
		res_df_by_tech = res_df[res_df[final_elec_code] == code]

		res_gdf_dict[code] = res_df_by_tech	

	# Import shapefile for country outline

	boundary = geopandas.read_file(boundary_file)
	boundary = boundary.set_crs('epsg:3857')

	# Plotting

	fig, ax2 = plt.subplots(figsize=(10,10))

	# You can comment this line out if you don't have a shapefile 
	boundary.plot(ax=ax2, color='black', edgecolor='black', zorder=1)
	
	ax2.scatter(res_gdf_dict[99]['X_deg'].values, res_gdf_dict[99]['Y_deg'].values, zorder=1, color=code_colors[99], s=0.005, label='Not Electrified')

	ax2.scatter(res_gdf_dict[1]['X_deg'].values, res_gdf_dict[1]['Y_deg'].values, zorder=2, color=code_colors[1], s=5, label='Grid')

	ax2.scatter(res_gdf_dict[2]['X_deg'].values, res_gdf_dict[2]['Y_deg'].values, zorder=2, color=code_colors[2], s=5, label='Stand-alone Diesel')

	ax2.scatter(res_gdf_dict[3]['X_deg'].values, res_gdf_dict[3]['Y_deg'].values, zorder=2, color=code_colors[3], s=5, label='Stand-alone PV')

	ax2.scatter(res_gdf_dict[4]['X_deg'].values, res_gdf_dict[4]['Y_deg'].values, zorder=2, color=code_colors[4], s=5, label='Mini-grid Diesel')

	ax2.scatter(res_gdf_dict[5]['X_deg'].values, res_gdf_dict[5]['Y_deg'].values, zorder=2, color=code_colors[5], s=5, label='Mini-grid PV')

	ax2.scatter(res_gdf_dict[6]['X_deg'].values, res_gdf_dict[6]['Y_deg'].values, zorder=2, color=code_colors[6], s=5, label='Mini-grid Wind')

	ax2.scatter(res_gdf_dict[7]['X_deg'].values, res_gdf_dict[7]['Y_deg'].values, zorder=2, color=code_colors[7], s=5, label='Mini-grid Hydro')

	ax2.scatter(res_gdf_dict[8]['X_deg'].values, res_gdf_dict[8]['Y_deg'].values, zorder=2, color=code_colors[8], s=5, label='Hybrid Mini-grid')

	
	lgnd = ax2.legend(loc="lower right", scatterpoints=1, fontsize=16)
	for handle in lgnd.legend_handles:
	    handle.set_sizes([14.0])

	ax2.set_axis_off()

	#Comment this line out if you do not want the title in the figure
	ax2.set_title(fig_title, loc='left', fontsize=16)

	fig.savefig(output_folder+fig_title+".png", format="png")



#User input starts here

boundary_file_path = "./utils/visual_files/bf_admin0_hno_2022.shp"

results_folder_path = "./OnSSET_Output/bau/"
results_csv = ["BFA-1-0_0_0_0_0_0_2021-2030.csv",
			   "BFA-1-1_1_1_1_1_1_2030-2040.csv",
			   "BFA-1-2_2_2_2_2_2_2040-2050.csv",
			   "BFA-1-3_3_3_3_3_3_2050-2060.csv",
			   "BFA-1-4_4_4_4_4_4_2060-2070.csv"
			   ]

map_folder = "./Maps_Output/"
figure_title = ["BAU 2030",
				"BAU 2040",
				"BAU 2050",
				"BAU 2060",
				"BAU 2070"]

year = [2030,2040,2050,2060,2070]

for y in range(len(year)):
	visualize(boundary_file_path, results_folder_path+results_csv[y], year[y], map_folder, figure_title[y])

print("Done!")