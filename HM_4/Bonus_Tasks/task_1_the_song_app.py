"""
The Song List App
You will create a simple application that will allow a user to create a list of favorite
songs, play the songs, and view other data about the songs. It'll be like
Spotify/iTunes/etc, but worse.
This app will have two classes, Song and List, and a list can contain many songs.
"""
import datetime
import random
import gc
from random import randrange


all_songs = []


class Song():
    def __init__(self, title, artist, duration, lyrics):
        self.many_songs = []
        self.title = title
        self.artist = artist
        self.duration = duration
        self.lyrics = lyrics

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def get_lyrics(self):
        return self.lyrics

    def play_a_song(self):
        return print(self.lyrics)

    def friendly_duration(self):
        return datetime.timedelta(seconds=self.duration)

    def add_song(self):
        new_entry = self.title + " " + self.artist + " " + str(self.duration) + " " + self.lyrics
        all_songs.append(new_entry)
        return all_songs


my_new_song = Song("Song1", "Kondio", 777, "Bla_Bla_Bla")
# print(my_new_song.title)
# print(my_new_song.artist)
# print(my_new_song.friendly_duration())
# #print(my_new_song.lyrics)
my_new_song.add_song()
# my_new_song.play_a_song()
# print(all_songs)

nov_hit = Song("Song2", "Painer_planetka", 888, "Top_top_maaane")
nov_hit.add_song()
# nov_hit.play_a_song()
#print(all_songs)

zemi_taz_tupalka = Song("Song3", "Bate_Encho", 999, "Zai4enceto bqqqlo cql deeen si igralooo")
zemi_taz_tupalka.add_song()
print(all_songs)


class List():
    @staticmethod
    def play_all():
        #need to get all instance of a Song class :)
        print("Playing all favorite songs: ")
        for obj in gc.get_objects():
            if isinstance(obj, Song):
                Song.play_a_song(obj)

    @staticmethod
    def shuffle():
        shuffledList = random.sample(all_songs, k=len(all_songs))
        print("\nPrinting all shuffled songs: ")
        for emp in shuffledList:
            print(emp)

    @staticmethod
    def duration():
        all_duration = []
        for obj in gc.get_objects():
            if isinstance(obj, Song):
                all_duration.append(Song.get_duration(obj))
        return print(f"The total duration of your favorite songs is : {sum(all_duration)}")


my_new_list = List()
my_new_list.play_all()
my_new_list.shuffle()
my_new_list.duration()


