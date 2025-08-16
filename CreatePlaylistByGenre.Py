from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import re


    
def show_tracks(results):
    # https://open.spotify.com/playlist/6WyM2sciZkovIERqDnudsH?si=a8f7d6f560f14ac3
    kpop_pid = '6WyM2sciZkovIERqDnudsH'
    liked_pid = '683tiJ0R8rdq67LQiGfanb'


    ids = []
    for item in results['items']:
        track = item['track']
        artist_id = track['artists'][0]['id']
        artist = sp.artist(artist_id)
        genres = artist.get('genres', [])
        print(f"  Genres: {genres}")
        ids.append(track['id'])





        # genres = artist['genres']
        # if len(genres) == 0:
        #     genres = ['N/A']
        
        # pattern = re.compile(r'k-pop', re.IGNORECASE)
        # for genre in genres:
        #     if pattern.search(genre):
                
        #         # print("{}".format(track['id']), genres)
        #         ids.append(track['id'])
        #         break

    # if len(ids) != 0:
    #     sp.playlist_add_items(liked_pid, ids)
    
    

# Initialize SpotifyOAuth with your credentials and scope
scope = ["playlist-modify-public", "playlist-modify-private", "user-library-read", "user-library-modify"]
sp_oauth = SpotifyOAuth(client_id='3a5b3c1533024e4a80ef5ada0654090f',
                        client_secret='38a1baa26b514c0d9437f5b6838f5039',
                        redirect_uri='https://example.com/',
                        scope=scope)



# Get the token
token_info = sp_oauth.get_cached_token()

# Create a Spotify instance with the access token
sp = Spotify(auth=token_info['access_token'])

if sp_oauth.is_token_expired(token_info):
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    sp = Spotify(auth=token_info['access_token'])

# Fetch current user information
user_info = sp.current_user()
user_id = user_info['id']

results = sp.current_user_saved_tracks()
show_tracks(results)

while results['next']:
    results = sp.next(results)
    show_tracks(results)
