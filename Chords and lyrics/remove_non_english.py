import enchant
import json

json_path = r"./data/all_artists_songs.json"
english_dict = enchant.Dict("en_US")


def remove_non_english():
    with open(json_path, 'r') as fp:
        data = json.load(fp)

    for artist_key, artist_val in data.items():
        for song_key, song_val in artist_val.items():
            lyrics = song_val[1]
            for row in lyrics:
                keep_check = True
                for word in row.split():
                    if not english_dict.check(word):
                        del data[artist_key][song_key]
                        keep_check = False
                        break
                if not keep_check:
                    break  # get out of lyrics

    with open(json_path, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


if __name__ == '__main__':
    remove_non_english()
