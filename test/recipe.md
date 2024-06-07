## 1. user story
As a user
So that I can keep --track of my music listening # initialise empty list
I want to --add tracks #function_name I've listened to and --see a list of them. #return a list

## 2. Design the class

```python

class MusicTracker:
    # User-facing properties:
    #   list of the tracks
    pass

    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   None
        # Side effects:
        #   initialise empty list called tracks
        pass

    def add_tracks(self, track):
        # Parameters:
        #   track - a string
        # Returns:
        #   None
        # Side effects:
        #   add track to list called tracks
        pass

    def list_tracks(self):
        # Parameters:
        #   None
        # Returns:
        #   list called tracks
        # Side effects:
        #   None
        pass

```

## 3. Examples of tests

```python

"""
Given a new instance of the class MusicTracker is instantiated
ensure an empty list called tracks is initialised
"""
checklist = MusicTracker() #empty list is initialised

"""
Given a new instance of the class MusicTracker is instantiated
raise an exception when add_tracks() is called where track isn't a string type
"""
checklist = MusicTracker()
checklist.add_tracks(2) => exception raised "this is not a valid track name"

"""
Given a new instance of the class MusicTracker is instantiated
and a track is added using add_tracks()
an exception is raised if track is already in the list
"""
checklist = MusicTracker()
checklist.add_tracks("Track 1") #track added to list
checklist.add_tracks("Track 1") => exception is raised "Track already in list"

"""
Given a new instance of the class MusicTracker is instantiated
and a track is added using add_tracks()
ensure track has been added to the list called tracks
"""
checklist = MusicTracker()
checklist.add_tracks("Track 1") #track added to list

"""
Given a new instance of the class MusicTracker is instantiated
and multiple tracks are added using add_tracks()
ensure all tracks are added to the list called tracks
"""
checklist = MusicTracker()
checklist.add_tracks("Track 1") #track added to list
checklist.add_tracks("Track 2") #track added to list
checklist.add_tracks("Track 3") #track added to list

"""
Given a new instance of the class MusicTracker is instantiated
raise exception when list_tracks() is called when list is empty
"""
checklist = MusicTracker()
checklist.list_tracks() => exception is raised "tracks list is empty"

"""
Given a new instance of the class MusicTracker is instantiated
and a track is added using add_tracks()
ensure list_tracks() returns correct list
"""
checklist = MusicTracker()
checklist.add_tracks("Track 1") #track added to list
checklist.list_tracks() => ["Track 1"]

"""
Given a new instance of the class MusicTracker is instantiated
and multiple tracks are added using add_tracks()
ensure list_tracks() returns correct list
"""
checklist = MusicTracker()
checklist.add_tracks("Track 1") #track added to list
checklist.add_tracks("Track 2") #track added to list
checklist.add_tracks("Track 3") #track added to list
checklist.list_tracks() => ["Track 1", "Track 2", "Track 3"]