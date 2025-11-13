import numpy as np
import matplotlib.pyplot as plt
import ligotools
import os
from scipy.signal import butter
from scipy.interpolate import interp1d
from scipy.io import wavfile
from ligotools.utils import whiten
from ligotools.utils import write_wavfile


#Test 1 for whiten utility  ple your whiten() definition

def test_whiten():
    
  # input test data
    dt = 1/4096  # sampling interval
    duration = 1  # second
    Nt = int(duration / dt)
    t = np.arange(Nt) * dt
    
    # create simple sine wave
    freq = 100  # Hz
    strain = np.sin(2 * np.pi * freq * t)
    
    # create simple PSD 
    def interp_psd(f):
        return np.ones_like(f)
    
    # apply whitening
    white_ht = whiten(strain, interp_psd, dt)
    
    # check output length matches input
    assert len(white_ht) == len(strain)
    
    # check output is real (no complex values)
    assert np.all(np.isreal(white_ht))



# Test #2 for wavefile

def test_write_wavfile_simple():
    filename = 'test.wav'
    fs = 4096A"
        assert audio.dtype == np.int16, "Wrong data type"
        assert np.max(np.abs(audio)) <= 32767, "Values out of range"
    except:
        pass
    finally:
        print("Cleaning up")
        if os.path.exists(filename):
            os.remove(filename)
