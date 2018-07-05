import os
import json

all_artist_dict = {}

for file_name in os.listdir("."):
    with open(file_name, 'r') as json_data:
        data = json.load(json_data)
        all_artist_dict.update(data)

num_of_songs = 0
for k in all_artist_dict:
    for k2 in all_artist_dict[k]:
        num_of_songs += 1

with open("all_artists_songs.json", 'w') as fp:
    json.dump(all_artist_dict, fp)
    print "Merged all json files in dir {0}\n" \
          "Number of songs is {1}".format(os.getcwd(), num_of_songs)
