'''
Steamlit plots to show musicality, top views and streams of top 13 artists worldwide for their top 10 tracks from Youtube and Spotify
'''

# imports
import streamlit as st
import pandas as pd

# page title
st.set_page_config(page_title="Spotify Kaggle Data Plots")
st.title("Spotify-Top 13 singing artists on Youtube Plots 📈")
st.subheader("Spotify_Youtube music and popularity data analysis")

# file uploads
container = st.container()

st.write("Main data file: Spotify_Youtube.csv")
# st.subheader("Choose one csv file to upload")
# uploaded_file1 = st.file_uploader('Choose a CSV file', type=['csv'], key="1")
# if uploaded_file1:
#     st.markdown("----")
#     df2 = pd.read_csv(uploaded_file1)
#     st.dataframe(df2)

df = pd.read_csv('Spotify_youtube_analysis/Spotify_Youtube.csv')
st.dataframe(df)
# container.write(df)

# file uploads
# st.write("Manipulated new data file for analysis: Artist_performance_popularity.csv")
# st.subheader("Choose one csv file to upload")
# uploaded_file2 = st.file_uploader('Choose a CSV file', type=['csv'], key="2")
# if uploaded_file2:
#     st.markdown("----")
#     df2 = pd.read_csv(uploaded_file2)
#     st.dataframe(df2)

# Dashboard plots
# col1, col2 = st.columns([3,3], gap="small")
st.write("**Bar graphs**") #** bolds the string
st.write("Showing Danceability, Energy and Liveness:")
st.image("Spotify_youtube_analysis/dance.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write("Showing Loudness and Speechiness:")
st.image("Spotify_youtube_analysis/loudness.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")

st.write("Showing Valence, Acousticness and Instrumentalness:")
st.image("Spotify_youtube_analysis/valence.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write("Showing Tempo and Key:")
st.image("Spotify_youtube_analysis/tempo.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")

st.write("**Line graph**")
st.write("Showing Views, Stream, Likes, Comments and Duration_in_milliseconds:")
st.image("Spotify_youtube_analysis/views_streams.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")

# Reports
st.write("Analysis report")
st.write("a) Bar graphs")
st.write(
'''
1. XXXTENTACION has least views with very high share of energy and highest danceability,
   but has one of the highest streams equal to Dua lipa. He has second highest loudness,
   but less than billie and has one of the highest speechiness in his tracks.
2. Bille E has lowest streams, lowest valence in her songs, but with highest loudness with significant speechiness,
   highest accousticness and instrumentalness with significant danceability and energy is one of the top 13 streamed artist.
3. Dua lipa with lowest danceabilty, highest energy and average liveness, significant speechiness and average loudness,
   highest valence equal to maroon 5 and greater than bruno, justin and ed sheeran,
   lowest accousticness and negligible or none instrumentalness in her tracks, is one of the top 13 streamed artists.
4. Bruno, Maroon 5 and dua lipa have the highest valence in their songs.
5. Imagine dragons have highest liveness and second highest energy.
6. Ariana has highest tempo, good valence and accousticness, significant loudness and one of the highest speechiness,
   very high energy with lowest danceabilty like dua lipa and good liveliness to be in the top 13 most stremes artists.
'''
)

st.write('b) Line graph')
st.write(
'''
1. Likes, comments, and average track duration in ms are almost same for all the top viewed artists on spotify for 10 tracks.
2. XXTENTACION, Dua lipa, Weekend, Khalid and post malone are outliers with less views but with high streams which means
   that they have a fanbase which is smaller than others who watched the video on youtube, especially XXTENTACION,
   but they listen to their songs a lot on spotify.
3. Bruno mars, Coldplay, Justin bieber and Ed sheeran have the least gap between their streams and views
   and XXXTENTACION has the highest gap in the views and streams and has higher streams than all these 4 artists for top 10 tracks.
'''
)

st.write('''
Conclusion:
1. Post malone and Ed sheeran are most listened artists and Ed sheeran is the most viewed artist for total 10 tracks.
   This isn't a proof of consistency but of total performance.
2. Bruno mars, Coldplay, Justin bieber and Ed sheeran have the least gap in their streams and views and have consistency
   in their top 10 hits on Spotify and Youtube respectively.
''')


st.write("- By Swati Mishra")
st.write("- 20-07-2023")

#----End of Plotting.py file----------------------------------------------------------------
# Coder: Swati Mishra
