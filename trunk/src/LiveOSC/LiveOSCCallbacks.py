"""
# Copyright (C) 2007 Rob King (rob@re-mu.org)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For questions regarding this module contact
# Rob King <rob@e-mu.org> or visit http://www.e-mu.org

This file contains all the current Live OSC callbacks. 

"""
import Live
from _LiveAPICore import *

class LiveOSCCallbacks:
   
    def __init__(self, oscServer):
        
        if oscServer:
            self.oscServer = oscServer
            self.callbackManager = oscServer.callbackManager
            self.oscClient = oscServer.oscClient
        else:
            return

        self.callbackManager.add(self.tempoCB, "/live/tempo")
        self.callbackManager.add(self.timeCB, "/live/time")
        self.callbackManager.add(self.nextCueCB, "/live/next/cue")
        self.callbackManager.add(self.prevCueCB, "/live/prev/cue")
        self.callbackManager.add(self.playCB, "/live/play")
        self.callbackManager.add(self.playContinueCB, "/live/play/continue")
        self.callbackManager.add(self.playSelectionCB, "/live/play/selection")
        self.callbackManager.add(self.playClipCB, "/live/play/clip")
        self.callbackManager.add(self.playSceneCB, "/live/play/scene")
        self.callbackManager.add(self.stopCB, "/live/stop")
        self.callbackManager.add(self.stopClipCB, "/live/stop/clip")
        self.callbackManager.add(self.stopTrackCB, "/live/stop/track")
        self.callbackManager.add(self.nameSceneCB, "/live/name/scene")
        self.callbackManager.add(self.nameTrackCB, "/live/name/track")
        self.callbackManager.add(self.nameClipCB, "/live/name/clip")
        self.callbackManager.add(self.armTrackCB, "/live/arm")
        self.callbackManager.add(self.disarmTrackCB, "/live/disarm")
        self.callbackManager.add(self.muteTrackCB, "/live/mute")
        self.callbackManager.add(self.unmuteTrackCB, "/live/unmute")
        self.callbackManager.add(self.soloTrackCB, "/live/solo")
        self.callbackManager.add(self.unsoloTrackCB, "/live/unsolo")
        self.callbackManager.add(self.volumeCB, "/live/volume")
        self.callbackManager.add(self.panCB, "/live/pan")
        self.callbackManager.add(self.sendCB, "/live/send")
        self.callbackManager.add(self.pitchCB, "/live/pitch")


    def tempoCB(self, msg):
        """Called when a /live/tempo message is received.

        Messages:
        /live/tempo                 Request current tempo, replies with /live/tempo (float tempo)
        /live/tempo (float tempo)   Set the tempo, replies with /live/tempo (float tempo)
        """
        if len(msg) == 3:
            tempo = msg[2]
            LiveUtils.setTempo(tempo)
        self.oscServer.sendOSC("/live/tempo", LiveUtils.getTempo())
        
    def timeCB(self, msg):
        """Called when a /live/time message is received.

        Messages:
        /live/time                 Request current song time, replies with /live/time (float time)
        /live/time (float time)    Set the time , replies with /live/time (float time)
        """
        if len(msg) == 3:
            time = msg[2]
            LiveUtils.currentTime(time)
        self.oscServer.sendOSC("/live/time", LiveUtils.currentTime())
        
    def nextCueCB(self, msg):
        """Called when a /live/next/cue message is received.

        Messages:
        /live/next/cue              Jumps to the next cue point
        """
        LiveUtils.jumpToNextCue()
        
    def prevCueCB(self, msg):
        """Called when a /live/prev/cue message is received.

        Messages:
        /live/prev/cue              Jumps to the previous cue point
        """
        LiveUtils.jumpToPrevCue()
        
    def playCB(self, msg):
        """Called when a /live/play message is received.

        Messages:
        /live/play              Starts the song playing
        """
        LiveUtils.play()
        
    def playContinueCB(self, msg):
        """Called when a /live/play/continue message is received.

        Messages:
        /live/play/continue     Continues playing the song from the current point
        """
        LiveUtils.continuePlaying()
        
    def playSelectionCB(self, msg):
        """Called when a /live/play/selection message is received.

        Messages:
        /live/play/selection    Plays the current selection
        """
        LiveUtils.playSelection()
        
    def playClipCB(self, msg):
        """Called when a /live/play/clip message is received.

        Messages:
        /live/play/clip     (int track, int clip)   Launches clip number clip in track number track
        """
        if len(msg) == 4:
            track = msg[2]
            clip = msg[3]
            LiveUtils.launchClip(track, clip)
            
    def playSceneCB(self, msg):
        """Called when a /live/play/scene message is received.

        Messages:
        /live/play/scene    (int scene)     Launches scene number scene
        """
        if len(msg) == 3:
            scene = msg[2]
            LiveUtils.launchScene(scene)
    
    def stopCB(self, msg):
        """Called when a /live/stop message is received.

        Messages:
        /live/stop              Stops playing the song
        """
        LiveUtils.stop()
        
    def stopClipCB(self, msg):
        """Called when a /live/stop/clip message is received.

        Messages:
        /live/stop/clip     (int track, int clip)   Stops clip number clip in track number track
        """
        if len(msg) == 4:
            track = msg[2]
            clip = msg[3]
            LiveUtils.stopClip(track, clip)

    def stopTrackCB(self, msg):
        """Called when a /live/stop/track message is received.

        Messages:
        /live/stop/track     (int track, int clip)   Stops track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.stopTrack(track)

    def nameSceneCB(self, msg):
        """Called when a /live/name/scene message is received.

        Messages:
        /live/name/scene                            Rerurns a a series of all the scene names in the form /live/name/scene (int scene, string name)
        /live/name/scene    (int scene)             Returns a single scene's name in the form /live/name/scene (int scene, string name)
        /live/name/scene    (int scene, string name)Sets scene number scene's name to name

        """        
        #Requesting all scene names
        if len(msg) == 2:
            sceneNumber = 0
            for scene in LiveUtils.getScenes():
                self.oscServer.sendOSC("/live/name/scene", (sceneNumber, scene.name))
                sceneNumber = sceneNumber + 1
            return
        #Requesting a single scene name
        if len(msg) == 3:
            sceneNumber = msg[2]
            self.oscServer.sendOSC("/live/name/scene", (sceneNumber, LiveUtils.getScene(sceneNumber).name))
            return
        #renaming a scene
        if len(msg) == 4:
            sceneNumber = msg[2]
            name = msg[3]
            LiveUtils.getScene(sceneNumber).name = name
            
    def nameTrackCB(self, msg):
        """Called when a /live/name/track message is received.

        Messages:
        /live/name/track                            Rerurns a a series of all the track names in the form /live/name/track (int track, string name)
        /live/name/track    (int track)             Returns a single track's name in the form /live/name/track (int track, string name)
        /live/name/track    (int track, string name)Sets track number track's name to name

        """        
        #Requesting all track names
        if len(msg) == 2:
            trackNumber = 0
            for track in LiveUtils.getTracks():
                self.oscServer.sendOSC("/live/name/track", (trackNumber, track.name))
                trackNumber = trackNumber + 1
            return
        #Requesting a single track name
        if len(msg) == 3:
            trackNumber = msg[2]
            self.oscServer.sendOSC("/live/name/track", (trackNumber, LiveUtils.getTrack(trackNumber).name))
            return
        #renaming a track
        if len(msg) == 4:
            trackNumber = msg[2]
            name = msg[3]
            LiveUtils.getTrack(trackNumber).name = name

    def nameClipCB(self, msg):
        """Called when a /live/name/clip message is received.

        Messages:
        /live/name/clip                                      Rerurns a a series of all the clip names in the form /live/name/clip (int track, int clip, string name)
        /live/name/clip    (int track, int clip)             Returns a single clip's name in the form /live/name/clip (int clip, string name)
        /live/name/clip    (int track, int clip, string name)Sets clip number clip in track number track's name to name

        """        
        #Requesting all clip names
        if len(msg) == 2:
            trackNumber = 0
            clipNumber = 0
            for track in LiveUtils.getTracks():
                for clipSlot in track.clip_slots:
                    if clipSlot:
                        self.oscServer.sendOSC("/live/name/clip", (trackNumber, clipNumber, clipSlot.clip.name))
                    clipNumber = clipNumber + 1
                clipNumber = 0
                trackNumber = trackNumber + 1
            return
        #Requesting a single scene name
        if len(msg) == 4:
            trackNumber = msg[2]
            clipNumber = msg[3]
            self.oscServer.sendOSC("/live/name/scene", (trackNumber, clipNumber, LiveUtils.getClip(trackNumber, clipNumber).name))
            return
        #renaming a scene
        if len(msg) == 5:
            trackNumber = msg[2]
            clipNumber = msg[3]
            name = msg[4]
            LiveUtils.getClip(trackNumber, clipNumber).name = name
    
    def armTrackCB(self, msg):
        """Called when a /live/arm message is received.

        Messages:
        /live/arm     (int track)   Arms track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.armTrack(track)
            
    def disarmTrackCB(self, msg):
        """Called when a /live/disarm message is received.

        Messages:
        /live/disarm     (int track)   Disarms track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.disarmTrack(track)
            
    def muteTrackCB(self, msg):
        """Called when a /live/mute message is received.

        Messages:
        /live/mute     (int track)   Mutes track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.muteTrack(track)
            
    def unmuteTrackCB(self, msg):
        """Called when a /live/unmute message is received.

        Messages:
        /live/unmute     (int track)   Unmutes track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.unmuteTrack(track)
            
    def soloTrackCB(self, msg):
        """Called when a /live/solo message is received.

        Messages:
        /live/solo     (int track)   Solos track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.soloTrack(track)
            
    def unsoloTrackCB(self, msg):
        """Called when a /live/unsolo message is received.

        Messages:
        /live/unsolo     (int track)   Unsolos track number track
        """
        if len(msg) == 3:
            track = msg[2]
            LiveUtils.unsoloTrack(track)
            
    def volumeCB(self, msg):
        """Called when a /live/volume message is received.

        Messages:
        /live/volume     (int track)                            Returns the current volume of track number track as: /live/volume (int track, float volume(0.0 to 1.0))
        /live/volume     (int track, float volume(0.0 to 1.0))  Sets track number track's volume to volume
        """
        if len(msg) == 4:
            track = msg[2]
            volume = msg[3]
            LiveUtils.trackVolume(track, volume)
        if len(msg) >= 3:
            track = msg[2]
            self.oscServer.sendOSC("/live/volume", (track, LiveUtils.trackVolume(track)))
            
    def panCB(self, msg):
        """Called when a /live/pan message is received.

        Messages:
        /live/pan     (int track)                            Returns the pan of track number track as: /live/pan (int track, float pan(-1.0 to 1.0))
        /live/pan     (int track, float pan(-1.0 to 1.0))     Sets track number track's pan to pan

        """
        if len(msg) == 4:
            track = msg[2]
            pan = msg[3]
            LiveUtils.trackPan(track, pan)
        if len(msg) >= 3:
            track = msg[2]
            self.oscServer.sendOSC("/live/pan", (track, LiveUtils.trackPan(track)))
            
    def sendCB(self, msg):
        """Called when a /live/send message is received.

        Messages:
        /live/send     (int track, int send)                              Returns the send level of send (send) on track number track as: /live/send (int track, int send, float level(0.0 to 1.0))
        /live/send     (int track, int send, float level(0.0 to 1.0))     Sets the send (send) of track number (track)'s level to (level)

        """
        if len(msg) == 5:
            track = msg[2]
            send = msg[3]
            level = msg[4]
            LiveUtils.trackSend(track, volume)
        if len(msg) >= 4:
            track = msg[2]
            send = msg[3]
            self.oscServer.sendOSC("/live/volume", LiveUtils.trackSend(track, send))
            
    def pitchCB(self, msg):
        """Called when a /live/pitch message is received.

        Messages:
        /live/pitch     (int track, int clip)                                               Returns the pan of track number track as: /live/pan (int track, int clip, int coarse(-48 to 48), int fine (-50 to 50))
        /live/pitch     (int track, int clip, int coarse(-48 to 48), int fine (-50 to 50))  Sets clip number clip in track number track's pitch to coarse / fine

        """
        if len(msg) == 6:
            track = msg[2]
            clip = msg[3]
            coarse = msg[4]
            fine = msg[5]
            LiveUtils.clipPitch(track, clip, coarse, fine)
        if len(msg) >=4:
            track = msg[2]
            clip = msg[3]
            self.oscServer.sendOSC("/live/pitch", LiveUtils.clipPitch(track, clip))
