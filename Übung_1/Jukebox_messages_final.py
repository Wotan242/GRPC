import Jukebox_pb2
from Jukebox_pb2 import Jukebox
import Jukebox_pb2_grpc

jukebox_1 = Jukebox()

artist_1 = Jukebox.Artist()
artist_1.name = "AC/DC"

album_11 = Jukebox.Artist.Album()
album_11.name = "Highway to Hell"
album_11.year = 1979
album_11.genre = album_11.genre_list.rock;
album_11.lineup["Vocals"] = "Bon Scott"
album_11.lineup["Lead Guitar"] = "Angus Young"
album_11.title.append("Highway To Hell")
album_11.title.append("Touch To Much")

album_12 = Jukebox.Artist.Album()
album_12.name = "Back in Black"
album_12.year = 1980
album_12.genre = album_12.genre_list.rock;
album_12.lineup["Vocals"] = "Brian Johnson"
album_12.lineup["Lead Guitar"] = "Angus Young"
album_12.title.append("Hells Bells")
album_12.title.append("You Shook Me All Night Long")

artist_1.album.append(album_11)
artist_1.album.append(album_12)


artist_2 = Jukebox.Artist()
artist_2.name = "Beatles"

album_21 = Jukebox.Artist.Album()
album_21.name = "Help!"
album_21.year = 1965
album_21.genre = album_21.genre_list.pop;
album_21.lineup["Vocals"] = "John Lennon"
album_21.lineup["Lead Guitar"] = "Paul McCartney"
album_21.title.append("Help!")
album_21.title.append("Yesterday")


album_22 = Jukebox.Artist.Album()
album_22.name = "Let It Be"
album_22.year = 1970
album_22.genre = album_22.genre_list.pop;
album_22.lineup["Vocals"] = "John Lennon"
album_22.lineup["Lead Guitar"] = "Paul McCartney"
album_22.title.append("Let It Be")
album_22.title.append("Get Back")

artist_2.album.append(album_21)
artist_2.album.append(album_22)

jukebox_1.artist.append(artist_1)
jukebox_1.artist.append(artist_2)



print(jukebox_1)
