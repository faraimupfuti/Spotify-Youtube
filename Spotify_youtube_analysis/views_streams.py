'''
Module to analyse processed data to plot views, streams, likes, comments, duration in milliseconds,
to show popularity of top 10 most streamed artists: Line graph to show data analysis of popularity of most streamed artists.
By Swati Mishra
20-7-2023
'''
# imports
import pandas as pd
import matplotlib.pyplot as plt

# data analysis
def popularity_plot(file_name):
    '''
    funtion to read processed data and analyse it to plot line graph
    '''
    ydf = pd.read_csv(file_name)
    
    # creating top 10 most streamed artists
    max10 = ydf.nlargest(10, ['Stream'], keep='all')
    max10_views = max10['Views']
    max10_likes = max10['Likes']
    max10_comments = max10['Comments']
    max10_duration_ms = max10['Duration_ms']
    max10_stream = max10['Stream']
    max10_artist = max10['Artists']
    max10_tracks = max10['Tracks']

    # line graph plot
    figure, axes = plt.subplots(figsize=(15,8))

    a1 = axes.plot(max10_views,max10_artist)
    a2 = axes.plot(max10_stream,max10_artist)
    a3 = axes.plot(max10_likes,max10_artist)
    a4 = axes.plot(max10_comments,max10_artist)
    a5 = axes.plot(max10_duration_ms,max10_artist)
    a6 = axes.plot(max10_tracks,max10_artist)

    axes.legend([a1[0], a2[0], a3[0], a4[0], a5[0], a6[0]], ['Views', 'Stream', 'Likes', 'Comments', 'Duration_ms'], title="No. of tracks: 10")
    axes.set_title("Popularity comparison in views, likes, comments, streams, duration_ms of Top 10 most streamed singers", pad=10, fontdict={'color':"darkviolet"})
    axes.set_ylabel("Artists", fontdict={'fontsize':15, 'color':"darkviolet"})

    for ind in [0,3,8]:
        plt.setp(axes.get_yticklabels()[ind], color='red')

    for ind1 in [1,5,7,9]:
        plt.setp(axes.get_yticklabels()[ind1], color='purple')

    figure.set_facecolor('white')
    figure.savefig('views_streams.png', facecolor='white')

    plt.show()
    plt.close(figure)

# function call
if __name__ == "__main__":
	popularity_plot('Artist_performance_popularity.csv')

# ...............................................end of module..............................................................................