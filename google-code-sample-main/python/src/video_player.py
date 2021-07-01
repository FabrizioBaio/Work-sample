"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.videoplaying = False
        self.videopaused = False
        self.currentvideo = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        array = [0]*len(self._video_library.get_all_videos())
        for video in self._video_library.get_all_videos():
            videotags = ""
            first = True
            for tag in video.tags:
                if first:
                    videotags = tag
                    first = False
                else:
                    videotags = videotags + " " + tag
            toadd = f"{video.title} ({video.video_id}) [{videotags}]"


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        passed = False
        for video in self._video_library.get_all_videos():
            if video.video_id == video_id:
                if self.videoplaying == True:
                    print(f"Stopping video: {self.currentvideo.title}")
                elif self.videopaused == True:
                    print(f"Stopping video: {self.currentvideo.title}")
                    self.videopaused = False
                self.videoplaying = True
                self.currentvideo = video
                print(f"Playing video: {video.title}")
                passed = True
        if passed != True:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self.videoplaying == True:
            print(f"Stopping video: {self.currentvideo.title}")
            self.videoplaying = False
            self.currentvideo = None
        elif self.videopaused == True:
            print(f"Stopping video: {self.currentvideo.title}")
            self.videopaused = False
            self.currentvideo = None
        else:
            print("Cannot stop video: No video is currently playing")
        

    def play_random_video(self):
        """Plays a random video from the video library."""

        if len(self._video_library.get_all_videos()) == 0:
            print("No videos available")

        randint = random.randint(0, len(self._video_library.get_all_videos()) - 1)
        counter = 0
        for video in self._video_library.get_all_videos():
            if counter == randint:
                videotoplay = video
            counter = counter + 1
        self.play_video(videotoplay.video_id)
            

    def pause_video(self):
        """Pauses the current video."""

        if self.videoplaying == True:
            print(f"Pausing video: {self.currentvideo.title}")
            self.videoplaying = False
            self.videopaused = True

        elif self.videopaused == True:
            print(f"Video already paused: {self.currentvideo.title}")

        else:
            print("Cannot pause video: No video is currently playing")
            

    def continue_video(self):
        """Resumes playing the current video."""
        
        if self.videopaused:
            print(f"Continuing video: {self.currentvideo.title}")
            self.videopaused = False
            self.videoplaying = True

        else:
            if self.videoplaying:
                print("Cannot continue video: Video is not paused")

            else:
                print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""

        if self.videoplaying == True:
            print(f"Currently playing: {self.currentvideo.title, self.currentvideo.video_id, self.currentvideo.tags}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
