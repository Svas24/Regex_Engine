def tracklist(**albums):
    for artist, songs in albums.items():
        print(artist)
        print('\n'.join([f'ALBUM: {album} TRACK: {track}' for album, track in songs.items()]))

