import numpy as np
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from  comtypes import CLSCTX_ALL

class VolumeController:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume= cast(interface, POINTER(IAudioEndpointVolume))
        self.minVol, self.maxVol = self.volume.GetVolumeRange()[0:2]
        
    def set_volume_by_distance(self, length, min_dist=30, max_dist=200):
        vol =  np.interp(length, [min_dist, max_dist], [self.minVol, self.maxVol])
        self.volume.SetMasterVolumeLevel(vol, None)
        return vol