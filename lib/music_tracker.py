class MusicTracker:
    def __init__(self):
        self.tracks = []

    def add_tracks(self, track):
        if type(track) != str or track == "" or track.isspace() == True:
            raise Exception("this is not a valid track name")
        for word in track.split():
            if word.isalnum is False:
                raise Exception("this is not a valid track name")
        if track in self.tracks:
            raise Exception("Track already in list")
        else:
            self.tracks.append(track)

    def list_tracks(self):
        if self.tracks == []:
            raise Exception("tracks list is empty")
        else:
            return self.tracks