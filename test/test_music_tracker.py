from lib.music_tracker import MusicTracker
import pytest

def test_empty_list_initialised():
    checklist = MusicTracker()
    assert checklist.tracks == []

def test_add_tracks_raises_exception_when_argument_not_string():
    checklist = MusicTracker()
    with pytest.raises(Exception) as error:
        checklist.add_tracks(2)
    error_message = str(error.value)
    assert error_message == "this is not a valid track name"

def test_add_tracks_adds_track_to_list():
    checklist = MusicTracker()
    checklist.add_tracks("Track 1")
    assert "Track 1" in checklist.tracks

def test_add_tracks_raises_exception_when_track_already_in_list():
    checklist = MusicTracker()
    checklist.add_tracks("Track 1")
    with pytest.raises(Exception) as error:
        checklist.add_tracks("Track 1")
    error_message = str(error.value)
    assert error_message == "Track already in list"

def test_add_tracks_adds_multiple_tracks_to_list():
    checklist = MusicTracker()
    checklist.add_tracks("Track 1")
    assert "Track 1" in checklist.tracks
    checklist.add_tracks("Track 2")
    assert "Track 2" in checklist.tracks
    checklist.add_tracks("Track 3")
    assert "Track 3" in checklist.tracks

def test_list_tracks_raises_exception_when_list_empty():
    checklist = MusicTracker()
    with pytest.raises(Exception) as error:
        checklist.list_tracks()
    error_message = str(error.value)
    assert error_message == "tracks list is empty"

def test_list_tracks_returns_correct_list_when_one_track_added():
    checklist = MusicTracker()
    checklist.add_tracks("Track 1")
    assert "Track 1" in checklist.tracks
    result = checklist.list_tracks()
    assert result == ["Track 1"]

def test_list_tracks_returns_correct_list_when_multiple_tracks_added():
    checklist = MusicTracker()
    checklist.add_tracks("Track 1")
    assert "Track 1" in checklist.tracks
    checklist.add_tracks("Track 2")
    assert "Track 2" in checklist.tracks
    checklist.add_tracks("Track 3")
    assert "Track 3" in checklist.tracks
    result = checklist.list_tracks()
    assert result == ["Track 1", "Track 2", "Track 3"]

def test_add_tracks_raises_exception_when_argument_is_empty_string():
    checklist = MusicTracker()
    with pytest.raises(Exception) as error:
        checklist.add_tracks("")
    error_message = str(error.value)
    assert error_message == "this is not a valid track name"