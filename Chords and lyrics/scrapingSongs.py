from bs4 import BeautifulSoup as soup
import urllib2
import enchant
import json
import logging
import subprocess
import sys
import time

logger = logging.getLogger()
if len(sys.argv) == 1:
    handler = logging.StreamHandler()
else:
    handler = logging.FileHandler("letter_{0}.log".format(sys.argv[1]))
formatter = logging.Formatter('[%(asctime)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


BEGINING = 17
END_SUB = -4

# Scrape all pages in ultimate guitar, for all the bands through a-z in all pages.
# dict is a dictionary that stores songs chords and lyrics

def check(l):
    print "wow, {0}".format(l)


def get_chords_lyrics_by_letter_and_page(letter):
    url = 'https://www.ultimate-guitar.com'
    bands = '/bands/'

    htm = '.htm'
    englishDict = enchant.Dict("en_US")

    artists_dict = None
    page_num = 0
    overall_songs = 0
    try:
        # Iterating all the letters
        logger.info("iterating over letter: {letter}".format(letter=letter))

        artists_dict = {}
        num_of_songs_saved = 0
        # Getting the number of pages for the specific letter
        currUrl = url + bands + letter + '1' + htm
        time.sleep(0.2)
        req = urllib2.Request(currUrl, headers={'User-Agent': "Magic Browser"})
        uClient = urllib2.urlopen(req)
        htmlPage = uClient.read()
        uClient.close()
        soupPage = soup(htmlPage, 'html.parser')
        ys = soupPage.findAll('a', {'class', "ys"})
        pos = len(ys) - 2
        numOfPages = int(ys[pos].string)

        # iterating page number
        for page_num in range(2, numOfPages):
            save_json_file(artists_dict, letter, page_num, num_of_songs_saved)
            artists_dict = {}
            chords_and_lyrics = {}
            num_of_songs_saved = 0

            if overall_songs > 420:
                exit(0)

            # the url of band that start with letter (let) and number (i)
            logger.info("iterating over page: {page_num}".format(page_num=page_num))
            currUrl = url + bands + letter + str(page_num) + htm
            time.sleep(0.2)
            req = urllib2.Request(currUrl, headers={'User-Agent': "Magic Browser"})
            uClient = urllib2.urlopen(req)
            htmlPage = uClient.read()
            uClient.close()
            soupPage = soup(htmlPage, 'html.parser')
            # the trClass is made of all the links to the artists in the current page
            trClass = soupPage.findAll({'class', 'tr'})
            # end is the number of artists in the page
            end = len(trClass)

            # iterating artist
            for artist_num_in_page in range(BEGINING, end + END_SUB):
                # getting the link for the artist page, very similliar to how we iterate page number
                # we iterate artist links (link), enter the url, and artistTrClass saves all the link for their songs
                textBeforeSplit = str(trClass[artist_num_in_page].a)
                artist_name = textBeforeSplit.split(">")[1].split(" Tabs")[0]
                logger.info("iterating over artist: {artist_name}".format(artist_name=artist_name))
                artists_dict[artist_name] = chords_and_lyrics
                link = textBeforeSplit.split("\"")[1]
                currUrl = url + link
                time.sleep(0.2)
                req = urllib2.Request(currUrl, headers={'User-Agent': "Magic Browser"})
                uClient = urllib2.urlopen(req)
                htmlPage = uClient.read()
                uClient.close()
                artistPage = soup(htmlPage, 'html.parser')
                artistTrClass = artistPage.find_all("tr", {"class": ["tr tr__lg", "tr__lg"]})
                artistSize = len(artistTrClass)

                # iterating songs
                for artist_song_num in range(0, artistSize):
                    if len(chords_and_lyrics) > 10:
                        break

                    songLinkBefore = str(artistTrClass[artist_song_num].a)
                    # we parse  and collect data only if song type is "Chords" and doesn't require premium account
                    typeCheck = str(artistTrClass[artist_song_num].b)
                    if typeCheck != '<b>Chords</b>' or songLinkBefore.startswith("<a 'event'"):
                        continue
                    # songName is the key in the dictionary
                    songName = songLinkBefore.split(">")[1].split("<")[0]
                    # logger.info("iterating over song: {songName}".format(songName=songName))
                    songLink = songLinkBefore.split("\"")[1]
                    if chords_and_lyrics.get(songName):
                        continue

                    # each dictionary key is made of 2 arrays,array[0]= chordsArray, array[1] = lyricsArray
                    chords_and_lyrics[songName] = [[], []]

                    if songLink:
                        # entering to a song link
                        time.sleep(0.2)
                        req = urllib2.Request(songLink, headers={'User-Agent': "Magic Browser"})
                        uClient = urllib2.urlopen(req)
                        songPage = uClient.read()
                        uClient.close()
                        songSoup = soup(songPage, 'html.parser')
                        songInfo = songSoup.findAll("pre", {"class": "js-tab-content"})
                        # Avoiding guitar PRO- links available only to premium. TODO duplicate...
                        if len(songInfo) > 0:
                            num_of_songs_saved += 1
                            overall_songs += 1
                            song = songInfo[0]
                            songString = str(song)
                            lines = songString.split("\n")
                            # Here we iterate for the lines in the sheet chords of the song.
                            # Only when we see a combination of a line starting with chords,
                            # and the next line starting with a known english word we keep those
                            # in the dictionary. They can be reached by using the songName as a key.
                            for line_num in range(0, len(lines) - 1):
                                line = lines[line_num]
                                nextLine = lines[line_num + 1]
                                nextLineWords = nextLine.split()
                                if len(nextLineWords) == 0:
                                    continue
                                wordForDict = nextLineWords[0]
                                if '<span>' in line and englishDict.check(wordForDict):
                                    line = line.replace('<span>', ' ')
                                    line = line.replace("</span>", " ")
                                    line = line.replace("\r", "")
                                    nextLine = nextLine.replace("\r", "")
                                    chords_and_lyrics[songName][0].append(line)
                                    chords_and_lyrics[songName][1].append(nextLine)
        if not letter:
            letter = "z"
        save_json_file(artists_dict, letter, page_num, num_of_songs_saved)

        uClient.close()
    except Exception as e:
        logger.error("Exception thrown, msg: \n{msg}".format(msg=e.message))
        save_json_file(artists_dict, letter, page_num, num_of_songs_saved)


def save_json_file(artists_dict, letter, page_num, counter):
    if artists_dict:
        file_name = "{letter}_{page_num}_chords_and_lyrics".format(letter=letter, page_num=page_num)
        logger.info("Saving json {0} with num of songs {1}".format(file_name, counter))
        with open(file_name, 'w') as fp:
            json.dump(artists_dict, fp, sort_keys=True, indent=4)



if __name__ == '__main__':
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    # process_list = []
    # for letter in alphabet:
    #     p = Process(target=get_chords_lyrics_by_letter_and_page, args=letter)
    #     p.start()
    #     process_list.append(p)
    #
    # for p in process_list:
    #     p.join()
    # get_chords_lyrics_by_letter_and_page("a")

    if len(sys.argv) == 1:
        for letter in alphabet:
            args = [sys.executable, __file__, letter]
            subprocess.Popen(args)
    else:
        letter = sys.argv[1]
        get_chords_lyrics_by_letter_and_page(letter)
