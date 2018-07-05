import json

json_path = r"./data/all_artists_songs.json"


def remove_empty_songs():
    with open(json_path, 'r') as fp:
        data = json.load(fp)

    for artist_key, artist_val in data.items():
        for song_key, song_val in artist_val.items():
            chords = song_val[0]
            lyrics = song_val[1]
            if not chords or not lyrics:
                del data[artist_key][song_key]
        if not data[artist_key]:
            del data[artist_key]

    with open(json_path, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


if __name__ == '__main__':
    remove_empty_songs()
