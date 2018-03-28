"""
Script créant un jeu de données des pistes contenues dans différentes playlists.
Pour chaque chanson, ses caractéristiques audio sont ajoutées.
"""
import json
import spotipy
import spotipy.util as util
import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials

# Dictionnaire de playlist
playlists = [
    # Classique
    ## Classical Essentials - 101 titres
    {"Genre": "Classique", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWWEJlAGA9gs0"},
    ## Piano 100: Spotify Picks - 100 titres
    {"Genre": "Classique", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXah8e1pvF5oE"},
    # Jazz
    ## Jazz Collection - 50 titres
    {"Genre": "Jazz", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWZx4L0CjnaL9"},
    ## Late Night Jazz - 58 titres
    {"Genre": "Jazz", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4wta20PHgwo"},
    ## Jazz Classics - 70 titres
    {"Genre": "Jazz", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXbITWG1ZJKYt"},
    # Blues
    ## Acoustic Blues - 64 titres
    {"Genre": "Blues", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX2iUghHXGIjj"},
    # Electro
    ## New Electro - 50 titres
    {"Genre": "Electro", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWTIfBdh7WtFL"},
    ## Dance Hits - 157 titres
    {"Genre": "Electro", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0BcQWzuB7ZO"},
    # Rock
    ## Légendes du Rock - 50 titres
    {"Genre": "Rock", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWXTHBOfJ8aI7"},
    ## Indie Rock Club - 50 titres
    {"Genre": "Rock", "URL":" https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX35DWKgAk2B5"},
    ## Rock Classics - 130 titres
    {"Genre": "Rock", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWXRqgorJj26U"},
    # Indie
    ## Indie Station - 50 titres
    {"Genre": "Indie", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX924zU1IARaD"},
    ## Hot Alternative - 50 titres
    {"Genre": "Indie", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWTRqg6ucMOrz"},
    # Pop
    ## Pop collection - 50 titres
    {"Genre": "Pop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWYX0SFpLcPgx"},
    ## Today's Top Hits - 50 titres
    {"Genre": "Pop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M"},
    ## Melting Pop - 50 titres
    {"Genre": "Pop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWYfb7VzTqlBj"},
    ## Hit Rewind - 55 titres
    {"Genre": "Pop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0s5kDXi1oC5"},
    # Metal
    ## Metal Essentials - 69 titres
    {"Genre": "Metal", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWWOaP4H0w5b0"},
    ## Masters of Metal - 50 titres
    {"Genre": "Metal", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX6BrB0kUwSdM"},
    # Hip-Hop
    ## Rap Collection - 35 titres
    {"Genre": "Hip-Hop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSCuekGD3tIW"},
    ## Classiques du Rap US - 70 titres
    {"Genre": "Hip-Hop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXawlg2SZawZf"},
    ## Classiques du Rap Français - 58 titres
    {"Genre": "Hip-Hop", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSrqNVMcxGKc"},
    # Folk
    ## Classic Acoustic - 86 titres
    {"Genre": "Folk", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX504r1DvyvxG"},
    ## Essential Folk - 94 titres
    {"Genre": "Folk", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWVmps5U8gHNv"},
    # RnB
    ## Alternative R&B - 54 titres
    {"Genre": "RnB", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSfMe9z89s9B"},
    ## R&B now - 40 titres
    {"Genre": "RnB", "URL": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWYfb7VzTqlBj"}
]

myid = 'id'
mysecret = 'secretid'
client_credentials_manager = SpotifyClientCredentials(client_id=myid, client_secret=mysecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def get_playlists():
    df = pd.DataFrame()
    list_songs = []
    for playlist in playlists:
        print("############### " + str(playlist['Genre']) + " ###############")
        list_songs = get_playlist_tracks("spotify", str(playlist['URL']))
        #with open('exportliste.json', 'w') as outfile:
        #    json.dump(list_songs, outfile)
        for song in list_songs:
            artist = (str(song['track']['artists'][0]['name']))
            title = (str(song['track']['name']))
            popularity = (str(song['track']['popularity']))
            uri = (str(song['track']['uri']))
            print(str(artist) + " - " + str(title))

            # Requête des caractéristiques musicales
            audio_features = sp.audio_features(uri)[0]

            df = df.append({"artiste": artist, "titre": title, "popularite": popularity, "uri": uri, "genre": str(playlist['Genre']), **audio_features}, ignore_index=True)
            #with open('export.json', 'w') as outfile:
            #    json.dump(song, outfile)
    return df


def main():
    # Noms ordonnés des colonnes
    columns = ['artiste', 'titre', 'genre', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

    df = get_playlists()

    df = df[columns]
    df.to_excel('export_full.xlsx')
    print(df.groupby('genre').count())

if __name__ == "__main__":
    main()
