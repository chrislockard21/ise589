"""
Let's make a song playlist. Each playlist contains a bunch of songs and/or albums

The following functionality is to be coded into each class
1) There are 4 classes: Song, Album, Artist and Playlist with the init method
2) A Song has a title, artist, album it belongs to and track_number; An Album has a title, artist, year, track list of songs;
3) An Artist has a name, albums list and songs list; A Playlist has a name and a songs list
4) Songs can be inserted to an album with each song having a track number
5) Songs can be inserted or deleted from a Playlist
6) Each song and album must be associated with an artist

"""

#define 4 classes and associated methods
class Song:
    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number

        artist.add_song(self)

class Album:
    def __init__(self, title, artist, year):
        self.title = title
        # This is an artist object
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, title, artist=None):
        track_number = len(self.tracks) + 1
        song = Song(title, self.artist, self, track_number)
        self.tracks.append(song)

    def __str__(self):
        response = ''
        for song in self.tracks:
            response = response + str(song.track_number) + ':' + song.title + '\n'
        return response

class Artist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

#Make a Band, album object - add song tracks to the album
band1 = Artist("Bob's Awesome Band")
album = Album("Bob's First Single", band1, 2013)
album.add_track("A Ballad about Lecturing")
album.add_track("A Ballad about Lecture+Programming (dance remix)")
album.add_track("A Third Song to Cry For")

band2 = Artist("Star's Band")
album2 = Album("Star's First Single", band2, 2018)
album2.add_track("A Karoake Song on Car Racing")
album2.add_track("A Poetic Song")
album2.add_track("Down to Earth")

album3 = Album("Bob's Second Attempt", band1, 2017)
album3.add_track("Really Bad")
album3.add_track("Done Bad (dance remix)")
album3.add_track("A fifth Song to Cry For")

#write code to print the album contents
print('Current songs in the album:')

for song in album.tracks:
    print(song.track_number, song.title)

#write code to print the album contents using the __str__ method
print(album2)

#write code to print the playlist contents
s1 = Song('Python is really hard', band1, album, 1)
s2 = Song('Python is easy', band2, album2, 2)

starly_playlist = Playlist("Starly's favorate playlist")
starly_playlist.add_song(s1)
starly_playlist.add_song(s2)

print('Current songs in the playlist:')

for song in starly_playlist.songs:
    print(song.track_number, song.title)
