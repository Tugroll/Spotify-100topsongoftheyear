
from SoupManager import SoupManager
from spotioauth import SpotiSongs

sp = SpotiSongs()
sp_manager = SoupManager()


sp.create_play_list()
sp.add_song_to_playlist(sp_manager.scraping_songs_as_list())





#print(all_movies[0])
#with open("movie.txt", "w",encoding="utf-8") as file:
