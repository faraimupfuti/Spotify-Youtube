'''
Module for data processing and plotting musicality: Horizontal bar graph plots to show musicality, top views and streams of top 13 artists worldwide for their
top 10 tracks from Youtube and Spotify
By Swati Mishra
20-7-2023
'''

# imports
from matplotlib import pyplot as plt
import pandas as pd

# data manipulation
def musicality_plots(file_name):
	'''
	function to analyse musical details of artist's tracks and plot barh graphs
	'''
	pdf = pd.read_csv(file_name)
	pdf1 = pdf.drop(columns=['Views', 'Likes', 'Comments'])
	pdf2 = pdf1[pdf1['Artists'] == "Joey Bada$$"].replace("Joey Bada$$", "Joey Badass")
	pdf1.update(pdf2)

	base = pow(10, len(str(round(pdf1['Stream'].max()))))
	pdf1['Stream'] = pdf1['Stream'].apply(lambda x: (round((x/base)*100))) # great replacement method # d1 got updated

	# Stream turns into logarithmic values causing errors. aaplying functions to clean
	mdf = pdf1.nlargest(n=10, columns='Stream', keep='all')
	artists = [f"{a}{mdf[mdf['Artists'] == a]['Stream'].values}" for a in mdf['Artists']]

	dance_df = mdf['Danceability'].apply(lambda x: round(x, 2)*100)
	energy_df = mdf['Energy'].apply(lambda x: round(x, 2)*100)
	live_df = mdf['Liveness'].apply(lambda x: round(x, 2)*100)
	# mdf

	fig, ax = plt.subplots(1, figsize=(18, 7))
	fig1, ax1 = plt.subplots(1, figsize=(18, 7))
	fig2, ax2 = plt.subplots(1, figsize=(18, 7))
	fig3, ax3 = plt.subplots(1, figsize=(18, 7))

	# plot 1
	line1 = ax.barh(artists, dance_df, color='green')
	line2 = ax.barh(artists, energy_df, color='blue')
	line3 = ax.barh(artists, live_df, color='magenta')
	ax.legend([line1, line2, line3], ['Danceability', 'Energy', 'Liveness'], title="No. of tracks: 10")
	ax.set_title("Top 13 most streamed singers, and danceability, energy and liveness in their tracks", pad=10, fontdict={'color':"purple"})
	ax.set_ylabel("Artists", fontdict={'fontsize':15, 'color':"purple"})

	# Add annotation to bars, get_width gives padding from bar, get_y alignment around bar's width
	for i in ax.patches:
		ax.text(i.get_width()+0.2, i.get_y()+0.2,
				str(round((i.get_width()))),
				fontsize=10, fontweight='bold',
				color='violet')

	# highlight lowest and highest streamed artists
	for ind in range(-len(mdf.nsmallest(2, columns='Stream', keep='all')),0):
		plt.setp(ax.get_yticklabels()[ind], color='red')
	for ind1 in range(0,2):
		plt.setp(ax.get_yticklabels()[ind1], color='purple')
	fig.set_facecolor('white')
	fig.savefig('dance.png', facecolor='white')

	# plot 2
	l1 = ax1.barh(artists, mdf['Loudness'].apply(lambda x: round(x, 2)*100), color='purple')
	l2 = ax1.barh(artists, mdf['Speechiness'].apply(lambda x: round(x, 2)*100), color='red')
	ax1.legend([l1, l2], ['Loudness', 'Speechiness'], title="No. of tracks: 10")
	ax1.set_title("Top 13 most streamed singers, and loudiness and speechiness in their tracks", pad=10, fontdict={'color':"green"})
	ax1.set_ylabel("Artists", fontdict={'fontsize':15, 'color':"green"})

	# Add annotation to bars, get_width gives padding from bar, get_y alignment around bar's width
	for i in ax1.patches:
		ax1.text(i.get_width()+0.2, i.get_y()+0.2,
				str(round((i.get_width()))),
				fontsize=10, fontweight='bold',
				color='violet')
	
	# highlight lowest and highest streamed artists
	for ind in range(-len(mdf.nsmallest(2, columns='Stream', keep='all')),0):
		plt.setp(ax1.get_yticklabels()[ind], color='red')
	for ind1 in range(0,2):
		plt.setp(ax1.get_yticklabels()[ind1], color='green')
	fig1.set_facecolor('white')
	fig1.savefig('loudness1.png', facecolor='white')

	# plot 3
	a = ax2.barh(artists, mdf['Valence'].apply(lambda x: round(x, 2)*100), color='yellow')
	b = ax2.barh(artists, mdf['Acousticness'].apply(lambda x: round(x, 2)*100), color='lightgreen')
	c = ax2.barh(artists, mdf['Instrumentalness'].apply(lambda x: round(x, 2)*100), color='cyan')
	ax2.legend([a, b, c], ['Valence', 'Acousticness', 'Instrumentalness'], title="No. of tracks: 10")
	ax2.set_title("Top 13 most streamed singers, and valence, accousticness and instrumentalness in their tracks", pad=10, fontdict={'color':"purple"})
	ax2.set_ylabel("Artists", fontdict={'fontsize':15, 'color':"purple"})

	# Add annotation to bars, get_width gives padding from bar, get_y alignment around bar's width
	for i in ax2.patches:
		ax2.text(i.get_width()+0.2, i.get_y()+0.2,
				str(round((i.get_width()))),
				fontsize=10, fontweight='bold',
				color='orange')

	# highlight lowest and highest streamed artists	
	for ind in range(-len(mdf.nsmallest(2, columns='Stream', keep='all')),0):
		plt.setp(ax2.get_yticklabels()[ind], color='red')
	for ind1 in range(0,2):
		plt.setp(ax2.get_yticklabels()[ind1], color='purple')
	fig2.set_facecolor('white')
	fig2.savefig('valence.png', facecolor='white')

	# plot 4
	d = ax3.barh(artists, mdf['Tempo'].apply(lambda x: round(x, 2)*100), color='maroon')
	e = ax3.barh(artists, mdf['Key'].apply(lambda x: round(x, 2)*100), color='orange')
	ax3.legend([d, e], ['Tempo', 'Key'], title="No. of tracks: 10")
	ax3.set_title("Top 13 most streamed singers, and tempo and key of their tracks", pad=10, fontdict={'color':"purple"})
	ax3.set_ylabel("Artists", fontdict={'fontsize':15, 'color':"purple"})

	# Add annotation to bars, get_width gives padding from bar, get_y alignment around bar's width
	for i in ax3.patches:
		ax3.text(i.get_width()+0.2, i.get_y()+0.2,
				str(round((i.get_width()))),
				fontsize=10, fontweight='bold',
				color='violet')
    
	# highlight the artists with highest and lowest gap between views and streams
	for ind in range(-len(mdf.nsmallest(2, columns='Stream', keep='all')),0):
		plt.setp(ax3.get_yticklabels()[ind], color='red')
	for ind1 in range(0,2):
		plt.setp(ax3.get_yticklabels()[ind1], color='purple')
	fig3.set_facecolor('white')
	fig3.savefig('tempo.png', facecolor='white')

# function call
if __name__ == "__main__":
	musicality_plots('Artist_performance_popularity.csv')

# ..............................................end of module......................................................................................