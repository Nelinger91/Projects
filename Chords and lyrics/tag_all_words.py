import json
import pickle
import re
from itertools import repeat


def get_chord_per_word(words_sent, chords_sent):
    num_words = len(words_sent)
    num_chords = len(chords_sent)

    if num_words > num_chords:
        chord_per_word_list = []
        repeat_chord_n_times = num_words // num_chords  # floor

        for chord in chords_sent:
            chord_per_word_list.extend(repeat(chord, repeat_chord_n_times))
        while len(chord_per_word_list) != len(words_sent):
            chord_per_word_list.append(chord_per_word_list[-1])  # add last chord until same length
        return zip(words_sent, chord_per_word_list)

    else:  # num_words <= num_chords
        return zip(words_sent, chords_sent)


def tag_all_words(data):
    corpus = []
    for artist_key, artist_val in data.items():
        for song_key, song_val in artist_val.items():
            chords = song_val[0]
            lyrics = song_val[1]
            if len(chords) == len(lyrics):
                zipped = zip(lyrics, chords)
                for words_sent, chords_sent in zipped:
                    words_sent = words_sent.split()
                    chords_sent = chords_sent.split()
                    chord_per_word_list = get_chord_per_word(words_sent, chords_sent)
                    corpus.extend(chord_per_word_list)
    return corpus


def get_json_data():
    json_path = r"./data/all_artists_songs.json"
    with open(json_path, 'r') as fp:
        data = json.load(fp)
    return data


def save_corpus(corpus):
    with open(r"./data/corpus.pickle", 'wb') as fp:
        pickle.dump(corpus, fp)


def clean_chords_and_lowercase_word(corpus):
    pattern = re.compile(r"\b[A-G](b|#)?(m|maj)?7?\b")
    return [(word.lower(), chord) for word, chord in corpus if pattern.match(chord)]  # reminder to mention lowercase


if __name__ == '__main__':
    data = get_json_data()
    corpus = tag_all_words(data)
    corpus = clean_chords_and_lowercase_word(corpus)
    save_corpus(corpus)
