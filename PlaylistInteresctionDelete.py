import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
    # Local Variables
    scope = ["playlist-modify-public", "playlist-modify-private", "user-library-read", "user-library-modify"]  # Example scope
    client_id = 'client_id'
    client_secret = 'client_secret'
    redirect_uri = 'https://example.com/'
    ex_trackIDs = ['3TGVhrnSc5VX2S3oA6dSTX', 
                   '6XxH22AeVCpz1vhwOYi5Sh', '0X214IiDWGaV68nzAnyGZW', '2bxVJeXMKGHijMD563Oqcr', '0bUvouwMaAA1xxtugiFXdF', '6fdr24Ns8PoBQ8wGwuupRr', '6DsPM0HMAXN5x4pzBR6bbo', '7tLTr44W3ztd9oOTWn6BFW', '7nbneCy1O9Zn5FNulhS6RD', '3OgRWuUOktuBGTING1oPld', '0pdvvP1vP8zWRHeBCHdFbG', '0OzZ01QOAnSXkYMZaaVUqi', '2ezzmll94GbaXehnUx6j2h', '1kfN7kA80uCKvZ2kQsXQHt', '1ZmFzNZ4wKaSwlJ9HGyFFt', '5IiAyeg16Rk5holAyjwpLO', '0X8D1aF2WJ88zYLqnftV8S', '6tCdBWL2AKhu3UMWkx1hlw', '7FJ03CSYlQWBIVOLrmDp3g', '250euDUWOcW2g5MFtTfhaD', '2R6zg6SWygSvY4wzv8BXId', '1b1U08Eqbx8f0QYyPTzqcU', '19gqxgVjSI8EyYWYyFUxQr', '7wc0wpRkVCVtF84g4YbCpH', '0gVtTa42rQFm2gW1uGSxKu', '4XBdxiVOSVzNmFcteVbQlt', '6ukhs32GxwnQBLR1Wwkuc3', '1iKkaI98zLjSH07G0rkt1e', '4dkRgyXF4JAqAjknCjuRbX', '4PGiHolWSgCIT0BmpO2VA2', '777im5SEYd0DoWvvcu2Yi3', '5bbNH85pbTNcwFcWMffmx4', '5SASWhvrGoHq7QK06Gh17I', '5mGJ1Bcc4SvHGufcTEJ1WE', '10T8nAM0CsCWjpDu3uH9U8', '0rA4Qzu2P7gOhnbdxUngNh', '679TnTjA1ad756mFFq91ZK', '4Yi0uhIDlK22MvHd5z677B', '3kzo68M2MvjbtEdYxa9EW0', '22yUER14ZEhGkhu4dFcNrW', '3okcBYUuR2VRbygL9kYb5k', '1sZjhTODX6sWuFFTTp5cb6', '1w7rP4pnAMKrqzUvXzYm4N', '30Hv12DkcIJcM2GWzNRmpV', '0xXaabBmxaTsxxNcf1a0Yn', '6R5tskH1NnCIZAz97qDFxp', '46OUNIkdTF8qRXlU6vTXIU', '65SsbtgsqPYv1p4Rq93fC9', '4rV50yTt1Me3sFhExrScR1', '7yahqANoaeBiBRlMZQacCN', '3VuJ5dbE0XEhdOgiaHDvNs', '3cvr7I6DJxIq3GL4UAU8p4', '4mCY3ezfbTUKYcS92pHq7K', '087cCCXpfcn8ChAssj7aMh', '3nZw1QmonyEBhwBWaodKxi', '4xWzZiZk6NWAO62h5sMm0N', '6f0ZXMKGBj9aABis7jrVPW', '48nIqwRQyLtqEcGzJWykLL', '0zdGcBMexiugXnCdfVgAo8', '0tYvtz8jKAyC12by9Lmp6L', '6eWgNJspumvHtUmx8pQlFM', '6tG0VmXVdfWz8C4q7fRC5E', '51i2k5wwoVJETU1Ki8Omjp', '3RGz1UbLFkDdxgs0JFFsnD', '4pETpGeHgZsouWPmvEUWXX', '6w96J5dviReX67Jg4cteYv', '1FIFWiHNLtohEAnuFgNgJf', '4n7npue0fQKKmgC1CcHmao', '6oosMYrpIekDxg67SV60Va', '4BWm9gWCP3ZUBWTgLN0FcS', '2Rp7GcV93L34g2GjU78uHB', '3sOa8FKNA94D9g96alv1IM'] 
    len(ex_trackIDs)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    # TODO: Add functionality that takes in user input and allows for dynamic playlist selection
    playlists = sp.user_playlists('31hg4cfdyrrwmlnvvbpjwo3zj4wa')
    liked_playlistID = str(playlists['items'][0]['id'])
    liked_playlistName = str(playlists['items'][0]['name'])
    test_playlistID = str(playlists['items'][1]['id'])
    test_playlistName = str(playlists['items'][1]['name'])          
    dnb_playlistID = str(playlists['items'][2]['id'])
    dnb_playlistName = str(playlists['items'][2]['name'])

    # (pname, tracks, ids) = playlist_track_traversal(dnb_playlistID, sp=sp)
    # print("dnb tracks: " + str(tracks))
    # (pname, tracks, ids) = playlist_track_traversal(playlist_id=None, sp=sp)
    # print("liked tracks: " + str(tracks))
    # sp.current_user_saved_tracks_delete(tracks=[track_id])

    # TESTING STUFF
    # print("test: " + str(test_playlistName))
    # print("dnb: " + str(dnb_playlistName))
    # print("liked: " + str(liked_playlistName))

    # sp.playlist_add_items(test_playlistID, ex_trackIDs)
    # (pname, tracks, ids) = playlist_track_traversal(sp=sp)
    # print(ids)
    # print_playlist_tracks(a, b, True)
    remove_playlist_from_playlist(playlist_toBeRemovedFromID=liked_playlistID, playlist_toBeRemovedID=dnb_playlistID, sp=sp)

    # COPY LIKED SONGS TO NEW PLAYLIST (MAKE THIS A FUNCTION OR SOMETHING)
    # playlist = sp.user_playlist_create(sp.current_user()['id'], 'Liked Songs (COPY)', public=False)
    # print("length of liked songs: " + str(len(tracks)))
    # for i in range(0, len(tracks), 5):
    #     seg = tracks[i:i+5]
    #     sp.user_playlist_add_tracks(sp.current_user()['id'], playlist['id'], seg) 
    

def remove_playlist_from_playlist(playlist_toBeRemovedFromID=None, playlist_toBeRemovedID=None, sp=None):
    """
    Deletes any overlapping songs from playlist with 

    Args:
        playlist_name (string): name of playlist
        track_names -> List[string]: playlist track names
        before (boolean): flag that denotes whether or not this function is called before or after the playlist deletion

    Returns:
        Output of calling main deletion function
    """
    # init playlist information
    (playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, 
     playlist_toBeRemovedFromTrackIDs) = playlist_track_traversal(playlist_toBeRemovedFromID, sp)
    
    (playlist_toBeRemovedName, playlist_toBeRemovedTrackNames, 
     playlist_toBeRemovedTrackIDs) = playlist_track_traversal(playlist_toBeRemovedID, sp)
    

    print_playlist_tracks(playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, True)

    playlist_toBeRemovedTrackNames = list(set(playlist_toBeRemovedFromTrackNames).intersection(set(playlist_toBeRemovedTrackNames)))
    playlist_toBeRemovedTrackIDs = list(set(playlist_toBeRemovedFromTrackIDs).intersection(set(playlist_toBeRemovedTrackIDs)))
    
    print_playlist_tracks(None, playlist_toBeRemovedTrackNames, True)

    if len(playlist_toBeRemovedTrackIDs) > 100:
        oldIndex = -1
        index = 99
        firstPass = True
        while index < len(playlist_toBeRemovedTrackIDs):
            if firstPass:
                sp.playlist_remove_all_occurrences_of_items(playlist_toBeRemovedFromID, playlist_toBeRemovedTrackIDs[:index])
                oldIndex = index
                index += 99
            else:
                sp.playlist_remove_all_occurrences_of_items(playlist_toBeRemovedFromID, playlist_toBeRemovedTrackIDs[oldIndex:oldIndex+99])
                oldIndex = index
                index += 99
    else:
        print("poop")
        if playlist_toBeRemovedFromID == None:
            for track_id in playlist_toBeRemovedTrackIDs:
                sp.current_user_saved_tracks_delete(tracks=[track_id])
        else:
            sp.playlist_remove_all_occurrences_of_items(playlist_toBeRemovedFromID, playlist_toBeRemovedTrackIDs)
    
    # reupdate names and tracks in older playlist
    (playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, playlist_toBeRemovedFromTrackIDs) = playlist_track_traversal(playlist_toBeRemovedFromID, sp)
    
    print_playlist_tracks(playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, False)


def print_playlist_tracks(playlist_name, tracks_names, before):
    """
    Helper function that prints out track names and handles logic for labels (pre/post change)

    Args:
        playlist_name (string): name of playlist
        track_names -> List[string]: playlist track names
        before (boolean): flag that denotes whether or not this function is called before or after the playlist deletion

    Returns:
        Output of calling main deletion function
    """
    max = 21
    if playlist_name == None:
        print("SONG TO BE REMOVED")
    elif before:
        print(f"SONGS IN {playlist_name} BEFORE: ")
    else: 
        print(f"SONGS IN {playlist_name} AFTER: ")
    

    if len(tracks_names) != 0:   
        print('-' * max)
        for x in range(len(tracks_names)):
            print(str(x + 1) + " ", end=' ')
            try:
                print(tracks_names[x])
            except UnicodeEncodeError:
                print("ENCODING ERROR: UNABLE TO PRINT NAME")
                continue
            if len(tracks_names[x]) > max:
                max = len(tracks_names[x])
        print('-' * max)
    print("TOTAL TRACKS: " + str(len(tracks_names)))
    print('\n')


def playlist_track_traversal(playlist_id=None, sp=None):
    """
    Traverses a given playlist to return its name, tracks, and track ids

    Args:
        playlist_id (string): The ID of the playlist per standard of spotipy API
        sp: spotify Auth object


    Returns:
        (name -> (str), tracks -> (List[string]), ids -> (List[string])): a tuple containing the name, tracks, and ids of the given playlist
    """

    tracks = sp.current_user_saved_tracks() if playlist_id == None else sp.playlist_tracks(playlist_id) 
    index = 0
    offset = 0
    song_num = 1
    track_names = []
    track_ids = []

    while index < len(tracks['items']):
        if playlist_id == None:
            if index == 19:
                offset += 19
                tracks = sp.current_user_saved_tracks(offset=offset)
                index = 0
        else:
            if index == 99:
                offset += 99
                tracks = sp.playlist_tracks(playlist_id=playlist_id, offset=offset)
                index = 0
            
        track_names.append(tracks['items'][index]['track']['name'])
        track_ids.append(tracks['items'][index]['track']['id'])
        index += 1
        song_num += 1

    if playlist_id != None:
        return(sp.playlist(playlist_id)['name'], track_names, track_ids)
    else:
        return("Liked Songs", track_names, track_ids)


# if __name__ == "__main__":
#     main()