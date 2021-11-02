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


artist_1.album.append(album_11)





jukebox_1.artist.append(artist_1)




print(jukebox_1)
