from ytmusicapi import YTMusic
import pandas as pd
# Add code to get the CSV documnet from shazam this is the next step.
music_list = pd.read_csv("shazamlibrary.csv", skiprows=1)
print(len(music_list))
music_list.drop_duplicates(subset=['TrackKey'], keep="first", inplace=True)
print(len(music_list))
#YTMusic.setup(filepath='headers_auth.json')
ytmusic = YTMusic('headers_auth.json')
# We do not need to run this again.
# playlistId = ytmusic.create_playlist("Shazam library", "All the songs I have Shazamed")
# print(playlistId)
playlistId = 'PLCnn9u1L6ZhQCoLDS4eo_Z2CwYxyIUCPj'
for i in music_list.values.tolist():
    temp = str(i[2]) + " " +str(i[3])
    search_results = ytmusic.search(temp)
    try:
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
    except:
        print("Song not found")

