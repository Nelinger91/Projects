import pickle
import logging
import json
import os.path
from textblob.classifiers import NaiveBayesClassifier
from tag_all_words import tag_all_words, clean_chords_and_lowercase_word

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

classifier_pickle_file = "words_to_chords_text_blob_classifier.pickle"

###### Testing Function ######


def get_json_data():
    json_path = r"./data/all_artists_songs.json"
    with open(json_path, 'r') as fp:
        data = json.load(fp)
    return data


def test_the_predictor(data, clf=None):
    tagged_words = clean_chords_and_lowercase_word(tag_all_words(data))  # data passed should look like all_artists_songs.json

    if not clf:
        with open(classifier_pickle_file, 'rb') as fp:
            clf = pickle.load(fp)

    success_counter = 0

    for word, chord in tagged_words:
        predicted_chord = clf.classify(word)
        print "Actual Chord: {0}    |   Predicted chord: {1}".format(chord, predicted_chord)
        # TODO we could also print the word here for evaluation in front of the lyircs
        if predicted_chord == chord:
            success_counter += 1

    # evaluate success
    print "Chord prediction success rate: {0}".format(success_counter / len(tagged_words))


###### Learning Function ######


def get_classifier():

    if not os.path.exists(classifier_pickle_file):

        # Load data if not trained yet
        logger.info("Classifier pickle file not found, reading data")
        with open(r"data/corpus.pickle", 'rb') as fp:
            data = pickle.load(fp)
        logger.info("Loaded data")

        logger.info("Learning classifier")
        clf = NaiveBayesClassifier(data)
        logger.info("Finished learning classifier")

        logger.info("Saving classifier")
        with open(classifier_pickle_file, 'wb') as fp:
            pickle.dump(clf, fp)

        # Load classifier if trained and pickled file exists
    else:
        with open(classifier_pickle_file, 'rb') as fp:
            clf = pickle.load(fp)
        logger.info("Loaded classifier")
        return clf


if __name__ == '__main__':
    classifier = get_classifier()
    data = get_json_data()
    test_the_predictor(data, classifier)
