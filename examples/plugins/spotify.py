#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This illustrates how to use SoCo plugins
# an example plugin is provided in soco.plugins.example.ExamplePlugin

import time

from soco import SoCo, SonosDiscovery
from soco.plugins import SoCoPlugin
from soco.plugins.spotify import SpotifyTrack
import sys

def main():
    soco = SoCo("192.168.178.25")

    # get a plugin by name (eg from a config file)
    myplugin = SoCoPlugin.from_name('soco.plugins.spotify.Spotify',
                                    soco)

    # do something with your plugin
    print('Testing: ' + myplugin.name)

    st = SpotifyTrack(sys.argv[1])

    track_info = soco.get_current_track_info()
    playlist_pos = track_info['playlist_position']
    queue_id = myplugin.add_track_to_queue(st, int(playlist_pos) + 1)

    soco.play_from_queue(queue_id - 1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: %s spotify-track-uri" % sys.argv[0])

    main()
