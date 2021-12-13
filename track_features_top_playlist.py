import spotipy
import csv
import boto3
from datetime import datetime
from connection.refresh import refresh
from config.playlists import spotify_playlists

spotify = spotipy.Spotify(auth_manager=refresh())
spotify.set_auth(refresh())

def gather_data(PLAYLIST):
    final_data_dictionary = {
        'Country': [],
        'Title': [],
        'Artist': [],
        'Release Date': [],
        'Popularity': [],
        'Danceability': [],
        'Energy': [],
        'Loudness': [],
        'Speechiness': [],
        'Acousticness': [],
        'Instrumentalness': [],
        'Tempo': []
    }
    with open("/tmp/" + PLAYLIST + ".csv", 'w', encoding="utf-8") as file:
        header = list(final_data_dictionary.keys())
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        playlist_tracks = spotify.playlist_items(spotify_playlists()[PLAYLIST])
        for song in playlist_tracks['items']:
            if song['track']:
                track_features = spotify.audio_features(song['track']['uri'])
                writer.writerow({'Country': PLAYLIST,
                                 'Title': song['track']['name'],
                                 'Artist': song['track']['artists'][0]['name'],
                                 'Release Date': song['track']['album']['release_date'],
                                 'Popularity': song['track']['popularity'],
                                 'Danceability': track_features[0]['danceability'],
                                 'Energy': track_features[0]['energy'],
                                 'Loudness': track_features[0]['loudness'],
                                 'Speechiness': track_features[0]['speechiness'],
                                 'Acousticness': track_features[0]['acousticness'],
                                 'Instrumentalness': track_features[0]['instrumentalness'],
                                 'Tempo': track_features[0]['tempo']
                                 })
    s3_resource = boto3.resource('s3')
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/' + PLAYLIST + '.csv'
    response = s3_resource.Object('spotify-analysis-data-1', filename).upload_file("/tmp/" + PLAYLIST + ".csv")

    return "response"

def lambda_handler(event, context):
    for playlist_name in spotify_playlists().keys():
        gather_data(playlist_name)

if __name__ == '__main__':
    for playlist_name in spotify_playlists().keys():
        data = gather_data(playlist_name)





