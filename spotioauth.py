import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = "wwww"
spotify_client_secret = "wwwww"
spotify_client_url = "http://example.com"

class SpotiSongs:

    def __init__(self):
        self.new_playlist = ""
        self.sp = spotipy.Spotify(auth_manager= SpotifyOAuth(
            client_id=spotify_client_id,
            client_secret=spotify_client_secret,
            redirect_uri=spotify_client_url,
            scope="playlist-modify-private"
            )
        )

    def create_play_list(self):
        user_id = self.sp.current_user()["id"]
        playlist_name = "Top 100 Songs Of The Date"
        playlist_description = "Amazing Songs"
        self.new_playlist = self.sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description,
                                               public=False)

    def add_song_to_playlist(self,all_songs):
        for item in all_songs:
            results = self.sp.search(q=item, type="track", limit=1)
            if results["tracks"]["items"]:
                track_uri = results["tracks"]["items"][0]["uri"]
                self.sp.playlist_add_items(self.new_playlist["id"], [track_uri])
                print(f"{item} başarıyla playliste eklendi.")
            else:
                print(f"{item} bulunamadı.")

