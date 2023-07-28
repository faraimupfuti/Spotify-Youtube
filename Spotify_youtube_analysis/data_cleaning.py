'''
Module data wrangling: To clean and process artists' useful data from the source to a csv file for analysis and visualization.
By Swati Mishra
20-7-2023
'''

# imports
import pandas as pd
import numpy as np
import os

# creating a data model to analyse musicality and popularity

def artists_analysis_csv(file_name):
    '''
    Function to clean and process source data to create new data
    '''
    df = pd.read_csv(file_name).drop(columns=['Unnamed: 0'])

    my_df = {}
    
    for name in df['Artist'].unique():
        a_df = df[df['Artist'] == name].filter(['Artist', 'Track', 'Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness',
        'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Views', 'Likes', 'Comments', 'Duration_ms', 'Stream']).replace(to_replace=np.nan, value=0.0)

        new_df = a_df.drop(columns=['Track'])
        new_df = new_df.mean(numeric_only=True)
        track_count = a_df['Track'].count()

        if 'Artists' not in my_df:
            my_df.update({'Artists':[str(name)]})
            my_df.update({'Tracks':[track_count]})
        else:
            my_df['Artists'].append(str(name))
            my_df['Tracks'].append(track_count)

        for k,v in new_df.items():
            if k in my_df:
                my_df[k].append(v)
                
            else:
                my_df.update({k:[v]})

    new_df1 = pd.DataFrame(data=my_df)
    if os.path.exists('Artist_performance_popularity.csv'):
        new_df2 = pd.read_csv('Artist_performance_popularity.csv')
        new_df2.update(new_df1)
        new_df2.to_csv('Artist_performance_popularity.csv', index=False)
    else:
        new_df1.to_csv('Artist_performance_popularity.csv', index=False)

# function call
if __name__ == "__main__":
    artists_analysis_csv('Spotify_Youtube.csv')

# .................................................end of module...............................................................................