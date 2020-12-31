import numpy as np
import random

def generate_playlists(pd_tracks, pd_playlists, nums_playlists_to_test = 100):
  choose_playlist = random.choices(np.arange(pd_playlists.shape[0]), k = nums_playlists_to_test)

  playlist_id = []

  for playlist_index in choose_playlist:
    if pd_tracks[pd_tracks['playlist_id'] == pd_playlists.iloc[playlist_index]['playlist_id']].shape[0] >= 50:
      playlist_id.append(pd_playlists.iloc[playlist_index]['playlist_id'])

  track_id_test = {}

  for list_id in playlist_id:
    track_id_test[list_id] = list(pd_tracks[pd_tracks['playlist_id'] == list_id]['track_id'])

  return track_id_test

def generate_testcases(track_id_test, fraction = 5):
  track_id_for_test = {}
  for key in track_id_test:
    all_tracks = track_id_test[key]
    n = len(all_tracks)
    nums_songs_to_test = n // fraction
    track_id_for_test[key] = all_tracks[:nums_songs_to_test]

  return track_id_for_test