import ligotools
import numpy as np
import os
import matplotlib.pyplot as plt
from ligotools import readligo as rl
from ligotools.readligo import dq2segs
from scipy.signal import butter
from scipy.interpolate import interp1d

# Test 1 Function chan_dict

def test_no_cbc_hw_inj():
    #Define Function and Load in H1 data (for self look at ifo and the names)
    strain, time, chan_dict = rl.loaddata(
        'data/L-L1_LOSC_4_V2-1126259446-32.hdf5',
        'H1'
    )
    # load in direct segment and define slice
    segment_list = rl.dq_channel_to_seglist(chan_dict['NO_CBC_HW_INJ'])
    slc = segment_list[0]

    #perform test
    assert slc.start == 0
    assert slc.stop == 131072

# Test 2 Testing Dq2segs Function

def test_dq2segs():
    # Simple test: 3 seconds on, 2 seconds off, 2 seconds on
    channel = np.array([1, 1, 1, 0, 0, 1, 1])
    gps_start = 1000000000
    
    segments = dq2segs(channel, gps_start)
    
    # Check segment times
    assert segments[0] == (1000000000, 1000000003), f"First segment wrong: {segments[0]}"
    assert segments[1] == (1000000005, 1000000007), f"Second segment wrong: {segments[1]}"
    