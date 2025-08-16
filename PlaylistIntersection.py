import spotipy
from spotipy.oauth2 import SpotifyOAuth

# TODO: FIX NAMING CONVENTIONS RETARD

def main():
    # Local Variables
    scope = ["playlist-modify-public", "playlist-modify-private"]  # Example scope
    client_id = '3a5b3c1533024e4a80ef5ada0654090f'
    client_secret = '38a1baa26b514c0d9437f5b6838f5039'
    redirect_uri = 'https://example.com/'
    ex_trackIDs = ['3TGVhrnSc5VX2S3oA6dSTX', 
                   '6XxH22AeVCpz1vhwOYi5Sh', '0X214IiDWGaV68nzAnyGZW', '2bxVJeXMKGHijMD563Oqcr', '0bUvouwMaAA1xxtugiFXdF', '6fdr24Ns8PoBQ8wGwuupRr', '6DsPM0HMAXN5x4pzBR6bbo', '7tLTr44W3ztd9oOTWn6BFW', '7nbneCy1O9Zn5FNulhS6RD', '3OgRWuUOktuBGTING1oPld', '0pdvvP1vP8zWRHeBCHdFbG', '0OzZ01QOAnSXkYMZaaVUqi', '2ezzmll94GbaXehnUx6j2h', '1kfN7kA80uCKvZ2kQsXQHt', '1ZmFzNZ4wKaSwlJ9HGyFFt', '5IiAyeg16Rk5holAyjwpLO', '0X8D1aF2WJ88zYLqnftV8S', '6tCdBWL2AKhu3UMWkx1hlw', '7FJ03CSYlQWBIVOLrmDp3g', '250euDUWOcW2g5MFtTfhaD', '2R6zg6SWygSvY4wzv8BXId', '1b1U08Eqbx8f0QYyPTzqcU', '19gqxgVjSI8EyYWYyFUxQr', '7wc0wpRkVCVtF84g4YbCpH', '0gVtTa42rQFm2gW1uGSxKu', '4XBdxiVOSVzNmFcteVbQlt', '6ukhs32GxwnQBLR1Wwkuc3', '1iKkaI98zLjSH07G0rkt1e', '4dkRgyXF4JAqAjknCjuRbX', '4PGiHolWSgCIT0BmpO2VA2', '777im5SEYd0DoWvvcu2Yi3', '5bbNH85pbTNcwFcWMffmx4', '5SASWhvrGoHq7QK06Gh17I', '5mGJ1Bcc4SvHGufcTEJ1WE', '10T8nAM0CsCWjpDu3uH9U8', '0rA4Qzu2P7gOhnbdxUngNh', '679TnTjA1ad756mFFq91ZK', '4Yi0uhIDlK22MvHd5z677B', '3kzo68M2MvjbtEdYxa9EW0', '22yUER14ZEhGkhu4dFcNrW', '3okcBYUuR2VRbygL9kYb5k', '1sZjhTODX6sWuFFTTp5cb6', '1w7rP4pnAMKrqzUvXzYm4N', '30Hv12DkcIJcM2GWzNRmpV', '0xXaabBmxaTsxxNcf1a0Yn', '6R5tskH1NnCIZAz97qDFxp', '46OUNIkdTF8qRXlU6vTXIU', '65SsbtgsqPYv1p4Rq93fC9', '4rV50yTt1Me3sFhExrScR1', '7yahqANoaeBiBRlMZQacCN', '3VuJ5dbE0XEhdOgiaHDvNs', '3cvr7I6DJxIq3GL4UAU8p4', '4mCY3ezfbTUKYcS92pHq7K', '087cCCXpfcn8ChAssj7aMh', '3nZw1QmonyEBhwBWaodKxi', '4xWzZiZk6NWAO62h5sMm0N', '6f0ZXMKGBj9aABis7jrVPW', '48nIqwRQyLtqEcGzJWykLL', '0zdGcBMexiugXnCdfVgAo8', '0tYvtz8jKAyC12by9Lmp6L', '6eWgNJspumvHtUmx8pQlFM', '6tG0VmXVdfWz8C4q7fRC5E', '51i2k5wwoVJETU1Ki8Omjp', '3RGz1UbLFkDdxgs0JFFsnD', '4pETpGeHgZsouWPmvEUWXX', '6w96J5dviReX67Jg4cteYv', '1FIFWiHNLtohEAnuFgNgJf', '4n7npue0fQKKmgC1CcHmao', '6oosMYrpIekDxg67SV60Va', '4BWm9gWCP3ZUBWTgLN0FcS', '2Rp7GcV93L34g2GjU78uHB', '3sOa8FKNA94D9g96alv1IM'] 
    len(ex_trackIDs)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    # TODO: Add functionality that takes in user input and allows for dynamic playlist selection
    playlists = sp.user_playlists('31hg4cfdyrrwmlnvvbpjwo3zj4wa')
    dnb_playlistID = "0eMxBsohkRuUrYxKVlRJo2"


    sourceID = "7v27IO8BOQMg9VkSupgQ3B"
    destID = "5OGJRX27nCSQPPObG4UtCn"
    # print_top_100_tracks(sp, test_playlistID)

    copy_tracks_by_artist(sp, source_playlist_id=dnb_playlistID, dest_playlist_id=destID, artist_names=["1991", "Dimension", "Sub Focus", "Culture Shock"])



    # TESTING STUFF
    # sp.playlist_add_items(test_playlistID, ex_trackIDs)
    # remove_playlist_from_playlist(playlist_toBeRemovedFromID=test_playlistID, playlist_toBeRemovedID=dnb_playlistID, sp=sp)


def remove_playlist_from_playlist(playlist_toBeRemovedFromID, playlist_toBeRemovedID, sp):
    (playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, playlist_toBeRemovedFromTrackIDs) = playlist_track_traversal(playlist_toBeRemovedFromID, sp)
    (playlist_toBeRemovedName, playlist_toBeRemovedTrackNames, playlist_toBeRemovedTrackIDs) = playlist_track_traversal(playlist_toBeRemovedID, sp)
    

    print_playlist_tracks(playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, True)

    intersection = set(playlist_toBeRemovedFromTrackNames).intersection(set(playlist_toBeRemovedTrackNames))
    
    print_playlist_tracks(None, list(intersection), True)


    # TODO: fix
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
                sp.playlist_remove_all_occurrences_of_items(playlist_toBeRemovedFromID, playlist_toBeRemovedTrackIDs[oldIndex:99])
                oldIndex = index
                index += 99
    print('\n')
    
    # reupdate names and tracks in older playlist
    (playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, playlist_toBeRemovedFromTrackIDs) = playlist_track_traversal(playlist_toBeRemovedFromID, sp)
    
    print_playlist_tracks(playlist_toBeRemovedFromName, playlist_toBeRemovedFromTrackNames, False)


def print_playlist_tracks(playlist_name, tracks_names, before):
    max = 21
    if playlist_name == None:
        print("SONG TO BE REMOVED")
    elif before:
        print("SONGS IN " + playlist_name + " BEFORE: ")
    else: 
        print("SONGS IN " + playlist_name + " AFTER: ")
    
    print('-' * max)
    for x in range(len(tracks_names)):
        print(str(x + 1) + " " + tracks_names[x])
        if len(tracks_names[x]) > max:
            max = len(tracks_names[x])
    print('-' * max)
    print("TOTAL TRACKS: " + str(len(tracks_names)))
    print('\n')


def playlist_track_traversal(playlist_id=None, sp=None, playlist=None):
    # inline if else - result = value_if_true if condition else value_if_false
    tracks = playlist if playlist_id == None else sp.playlist_tracks(playlist_id) 

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


def print_top_100_tracks(sp, playlist_id):
    """
    Print the first 100 tracks from a Spotify playlist.
    sp: an authenticated spotipy.Spotify client
    playlist_id: the ID or URI of the playlist
    """
    results = sp.playlist_items(
        playlist_id,
        limit=100,    # fetch up to 100
        offset=0,     # start at the beginning
        fields="items(track(name,artists(name))),next"
    )

    tracks = results["items"]

    for idx, item in enumerate(tracks, start=1):
        track = item["track"]
        name = track["name"]
        artists = ", ".join(artist["name"] for artist in track["artists"])
        print(f"{idx}. {name} — {artists}")

def copy_tracks_by_artist(sp, source_playlist_id, dest_playlist_id, artist_names=list):
    """
    Copies tracks from one playlist to another if they contain the given artist.
    
    sp: authenticated Spotify client
    source_playlist_id: ID/URI of the source playlist
    dest_playlist_id: ID/URI of the destination playlist
    artist_name: artist name to match (case-insensitive)
    """
    # make names lowercase
    names = [name.lower() for name in artist_names]


    offset = 0
    added_count = 0

    while True:
        results = sp.playlist_items(
            source_playlist_id,
            limit=100,
            offset=offset,
            fields="items(track(id,name,artists(name))),next"
        )
        
        items = results["items"]
        if not items:
            break

        # Collect matching track URIs
        track_uris = []
        for item in items:
            track = item["track"]
            if track is None:  # sometimes null if removed
                continue
            track_artists = [a["name"].lower() for a in track["artists"]]
            for track_artist in track_artists:
                if track_artist in names:
                    track_uris.append(track["id"])

        # Add them to the destination playlist (if any found in this batch)
        if track_uris:
            sp.playlist_add_items(dest_playlist_id, track_uris)
            added_count += len(track_uris)

        offset += 100
        if results["next"] is None:
            break

    # print(f"✅ Added {added_count} tracks by '{artist_names}' to playlist {dest_playlist_id}")


if __name__ == "__main__":
    main()