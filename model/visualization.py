import geopandas
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
import numpy as np
from matplotlib import rc
import matplotlib.patches as mpatches

def mapper(boundary_file, results_csv, end_year, output_folder, fig_title):
	'''
	Plots a geographical map with the geospatial distribution
	of technologies by a given end year
	'''

	print("Mapping "+fig_title)

	res_df = pd.read_csv(results_csv)

	final_elec_code = 'FinalElecCode' + str(end_year)

	#Select from the full results, the FinalElecCode in the end year for that scenario along with the coordinates

	res_df = res_df[['X_deg', 'Y_deg', final_elec_code]]
	res_gdf_dict = {}

	code_colors = {1: 'tab:cyan',
		       2: 'tab:green',
		       3: 'tab:orange',
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

	ax2.scatter(res_gdf_dict[1]['X_deg'].values, res_gdf_dict[1]['Y_deg'].values, zorder=3, color=code_colors[1], s=5, label='Grid')

	#ax2.scatter(res_gdf_dict[2]['X_deg'].values, res_gdf_dict[2]['Y_deg'].values, zorder=2, color=code_colors[2], s=5, label='Stand-alone Diesel')

	ax2.scatter(res_gdf_dict[3]['X_deg'].values, res_gdf_dict[3]['Y_deg'].values, zorder=4, color=code_colors[3], s=5, label='Stand-alone PV')

	#ax2.scatter(res_gdf_dict[4]['X_deg'].values, res_gdf_dict[4]['Y_deg'].values, zorder=2, color=code_colors[4], s=5, label='Mini-grid Diesel')

	ax2.scatter(res_gdf_dict[5]['X_deg'].values, res_gdf_dict[5]['Y_deg'].values, zorder=2, color=code_colors[5], s=5, label='Mini-grid PV')

	#ax2.scatter(res_gdf_dict[6]['X_deg'].values, res_gdf_dict[6]['Y_deg'].values, zorder=2, color=code_colors[6], s=5, label='Mini-grid Wind')

	#ax2.scatter(res_gdf_dict[7]['X_deg'].values, res_gdf_dict[7]['Y_deg'].values, zorder=2, color=code_colors[7], s=5, label='Mini-grid Hydro')

	#ax2.scatter(res_gdf_dict[8]['X_deg'].values, res_gdf_dict[8]['Y_deg'].values, zorder=2, color=code_colors[8], s=5, label='Hybrid Mini-grid')

	
	lgnd = ax2.legend(loc="lower right", scatterpoints=1, fontsize=16)
	for handle in lgnd.legend_handles:
	    handle.set_sizes([14.0])

	ax2.set_axis_off()

	#Comment this line out if you do not want the title in the figure
	#ax2.set_title(fig_title, loc='left', fontsize=16)

	fig.savefig(output_folder+fig_title+" map.png", format="png")

def donuts(results_csv, end_year, output_folder, fig_title):
	'''
	Plots a nested pie chart showing the rural-urban electrified
	population share and what each type of technology each population
	type is electrified by
	'''

	print("Plotting donut chart of "+fig_title)

	total_pop = 0

	res_df = pd.read_csv(results_csv)

	final_elec_code = 'FinalElecCode' + str(end_year)
	is_urban = 'IsUrban'
	pop = 'Pop' + str(end_year)

	#Select from the full results the FinalElecCode in the end year, population is the end year and the is_urban designation for that scenario

	res_df = res_df[[final_elec_code, is_urban, pop]]

	res_df = res_df.pivot_table(index = final_elec_code, columns = is_urban, aggfunc=sum)

	res_df = res_df.fillna(0)

	tech_dict = {1: 'Grid',
		       2: 'Stand-alone Diesel',
		       3: 'Stand-alone PV',
		       4: 'Mini-grid Diesel',
		       5: 'Mini-grid PV',
		       6: 'Mini-grid Wind',
		       7: 'Mini-grid Hydro',
		       8: 'Hybrid Mini-grid',
		       99: 'Not Electrified'}

	code_colors = {1: 'tab:cyan',
		       2: 'tab:green',
		       3: 'tab:orange',
		       4: 'tab:red',
		       5: 'mediumorchid',
		       6: 'tan',
		       7: 'tab:pink',
		       8: 'tab:olive',
		       99: 'tab:gray'}

	vals = []
	tech_labels = []
	pop_labels = ['Rural', 'Urban']
	inner_colors = ['#F18AAD', '#F3C65F']
	outer_colors = []
	index_list = list(res_df.index.values)

	for column in res_df:
		vals.append(list(res_df[column]))
		total_pop += res_df[column].sum() / 1000000

		for i in range(len(index_list)):
			if list(res_df[column])[i] != 0:
				tech_labels.append(tech_dict[index_list[i]])

				outer_colors.append(code_colors[index_list[i]])

	vals = np.array(vals)

	centre_text = 'Total \nPopulation ≈ \n'+ str(round(total_pop, 1)) + ' M'

	rc('font',**{'family':'serif','serif':['Georgia']})
	plt.rcParams['font.size'] = 18

	fig, ax = plt.subplots(figsize=(11, 8))

	size = 0.3

	inner_vals = vals.sum(axis=1)
	outer_vals = [i for i in vals.flatten() if i != 0]

	#inner ring
	inside_ring = ax.pie(inner_vals, radius=1-size, wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.2f%%', pctdistance=0.7, colors=inner_colors, labels=['']*len(inner_vals))

	#outer ring
	outside_ring = ax.pie(outer_vals, radius=1, wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.2f%%', pctdistance=1.2, colors=outer_colors, labels=['']*len(outer_vals))

	
	ax.text(0., 0., centre_text, horizontalalignment='center', verticalalignment='center')
	ax.set(aspect="equal")
	
	rural_leg_patch = mpatches.Patch(color=inner_colors[0], label=pop_labels[0])
	urban_leg_patch = mpatches.Patch(color=inner_colors[1], label=pop_labels[1])

	first_legend = ax.legend(handles=[rural_leg_patch, urban_leg_patch], loc='upper left', bbox_to_anchor=(-0.4, 1.05), title='Population Typology',frameon=True,fancybox=True)

	ax.add_artist(first_legend)

	tech_patches = []

	for t in range(len(set(tech_labels))):
		if mpatches.Patch(color=outer_colors[t], label=tech_labels[t]) not in tech_patches:
			tech_patches.append(mpatches.Patch(color=outer_colors[t], label=tech_labels[t]))

	ax.legend(handles=tech_patches, loc='upper left', title='Technology',frameon=True,fancybox=True, bbox_to_anchor=(0, 0.3), bbox_transform=fig.transFigure)

	
	fig.savefig(output_folder+fig_title+" donut.png", format="png")





#User input starts here

boundary_file_path = "./utils/visual_files/bf_admin0_hno_2022.shp"

results_folder_path = "./OnSSET_Output/bau/"
results_csv = ["BFA-1-0_0_0_0_0_0_2021-2030.csv",
	       "BFA-1-1_1_1_1_1_1_2030-2040.csv",
	       "BFA-1-2_2_2_2_2_2_2040-2050.csv",
	       "BFA-1-3_3_3_3_3_3_2050-2060.csv",
	       "BFA-1-4_4_4_4_4_4_2060-2070.csv"
	       ]

map_folder = "./Maps_Output/bau/"
figure_title = ["BAU 2030",
		"BAU 2040",
		"BAU 2050",
		"BAU 2060",
		"BAU 2070"]

year = [2030,2040,2050,2060,2070]

for y in range(len(year)):
	mapper(boundary_file_path, results_folder_path+results_csv[y], year[y], map_folder, figure_title[y])
	donuts(results_folder_path+results_csv[y], year[y], map_folder, figure_title[y])

	

print("Done!")
