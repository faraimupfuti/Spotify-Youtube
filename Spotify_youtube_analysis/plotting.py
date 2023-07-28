'''
Steamlit dashboard to show Python Pandas and Matplotlib charts data analysis and visualization
on musicality, top views and streams of top 13 most streamed artists worldwide for their top 10 tracks from Youtube and Spotify
'''

# imports
import streamlit as st
import pandas as pd

# page title
st.set_page_config(page_title="Spotify_Youtube Kaggle Data Plots")
st.title("Spotify_Youtube.csv Kaggle data analysis on worldwide most streamed artists to compare their music style and popularity: Matplotlib Plots 📈")

# file uploads
container = st.container()

st.write("DataFrame source: Spotify_Youtube.csv")
# st.subheader("Choose one csv file to upload")
# uploaded_file1 = st.file_uploader('Choose a CSV file', type=['csv'], key="1")
# if uploaded_file1:
#     st.markdown("----")
#     df2 = pd.read_csv(uploaded_file1)
#     st.dataframe(df2)

df = pd.read_csv('Spotify_youtube_analysis/Spotify_Youtube.csv')
st.dataframe(df)

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
st.write("Showing Danceability, Energy and Liveness of the top 13 most streamed artists worldwide:")
st.image("Spotify_youtube_analysis/dance.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write('''
Analysis: Among most streamed artists,
1) Justin B and Imagine D have the highest liveness despite having tracks in different genre.
2) Maroon 5, Imagine D and Dua L have the highest energy in their tracks.
3) Dua L and XXXTENTACION have surpassed Maroon 5, Ed Sheeran, Bruno and Ariana G for danceability in their tracks.
''')

st.write("Showing Loudness and Speechiness of the top 13 most streamed artists worldwide:")
st.image("Spotify_youtube_analysis/loudness.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write('''
Analysis: Among most streamed artists,
1) Billie E is an exception in loudness in her tracks. 
2) Ariana, Khalid, Justin B and XXXTENTACION have very high speechiness in their tracks compared to other top streamed artists.
''')

st.write("Showing Valence, Acousticness and Instrumentalness of the top 13 most streamed artists worldwide:")
st.image("Spotify_youtube_analysis/valence.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write('''
Analysis: Among most streamed artists,
1) Bruno M, Maroon 5 and Dua L have the highest valence in their songs.
2) No one uses Intrumentalness in their songs, except Imagine D, Coldplay and Khalid with some instrumentation
   and Billie E with highest as their tracks are a bit similar in genre.
3) Billie E is an exception in accousticness.
''')

st.write("Showing Tempo and Key of the top 13 most streamed artists worldwide:")
st.image("Spotify_youtube_analysis/tempo.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write('''\x1B[3m
Analysis: Among most streamed artists,
1) Almost everyone is similar in tempo, but Ariana uses highest tempo in her songs and Ed Sheeran uses lowest.
2) Imagine D and XXXTENTACION use high key comapared to other artists. XXXTENTACION tracks might be similar in genre to Imagine D.
3) Bruno, Khalid and The Weekend use lowest key in their tracks.
\x1B[0m''')

st.write("**Line graph**")
st.write("Showing Views, Stream, Likes, Comments and Duration_in_milliseconds of the top 10 most streamed artists worldwide:")
st.image("Spotify_youtube_analysis/views_streams.png", caption = None, width=1000, use_column_width=10, clamp=False, channels = "RGB", output_format="auto")
st.write('''\x1B[3m
Analysis: Among most streamed artists,
1) Almost everyone is similar in Likes, Comments and Duration_in_milliseconds of their top 10 tracks.
2) Post Malone is the most streamed with third lowest views for their total 10 tracks.
   Ed sheeran is the most viewed and secong highest streamed artist.
3) XXXTENTACION is the least viewed.
\x1B[0m''')

# Reports
st.write("Final Analysis reports")
st.write("a) Bar graphs")
st.write(
'''
1. XXXTENTACION has least views with very high share of energy and highest danceability,
   but has one of the highest streams equal to Dua lipa. He has second highest loudness,
   but less than billie and has one of the highest speechiness in his tracks.
2. Bille E has lowest streams with lowest valence in her songs, but with highest loudness, significant speechiness, and
   highest accousticness and instrumentalness with significant danceability and energy is one of the top 13 streamed artist.
3. Dua lipa with highest danceabilty, highest energy, average liveness, significant speechiness and average loudness,
   highest valence equal to maroon 5 and greater than bruno, justin and ed sheeran,
   lowest accousticness and no instrumentalness in her tracks, is one of the top 13 streamed artists.
4. Bruno, Maroon 5 and dua lipa have the highest valence in their songs.
5. Imagine dragons have highest liveness and second highest energy.
6. Ariana has highest tempo, good valence and accousticness, significant loudness and one of the highest speechiness,
   very high energy with lowest danceabilty like dua lipa and good liveliness to be in the top 13 most stremes artists.
'''
)

st.write('b) Line graph')
st.write(
'''
1. Likes, comments, and average track duration in ms are almost same for all the top 10 streamed artists on spotify for 10 tracks.
2. XXTENTACION, Dua lipa, Weekend, Khalid and post malone are outliers with less views but with high streams which means
   that they have a fanbase which is smaller than others who watched the video on youtube, especially XXTENTACION,
   but they listen to their songs a lot on spotify or their songs are popular but their videos are not consistently popular.
3. Bruno mars, Coldplay, Justin bieber and Ed sheeran have the least gap between their streams and views, but XXXTENTACION has
   the highest gap in the views and streams and has higher streams than all these 4 artists for top 10 tracks.
'''
)

st.write('''
Final Conclusion:
1. Post malone and Ed sheeran are most listened artists and Ed sheeran is the most viewed artist for total 10 tracks.
2. Bruno mars, Coldplay, Justin bieber and Ed sheeran have the least gap in their streams and views showing consistent
   appreciation for both videos and streams in their top 10 hits on Spotify and Youtube respectively.
3. The views and streams analysed are based on total performance of top 10 tracks, and are not about the consistency.
4. An artist can have extreme success on spotify streams, but very less on their youtube videos."
5. It's important to have good combination of valence, energy and liveness in one's tracks with significant accousticness
   to achieve consistency in views and streams.
6. However, having high energy, high loudness, and high danceability can give you very high streams for certain songs
   compared to other artists like in case of XXXTENTACION, but it can't ensure consistency in high views.
''')

st.write('''
- Posted by - Swati Mishra
- Posted on - 20-07-2023
- Tech stack used - Python, Pandas, Maplotlib, Streamlit cloud, VScode version control, GitHub repository
''')

#----End of Plotting.py file----------------------------------------------------------------
# Coder: Swati Mishra
