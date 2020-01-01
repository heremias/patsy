#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:13:51 2019

@author: heremias
"""
import numpy as np
import simpleaudio as sa
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("k", type=str, help="the key")

args = parser.parse_args()

if args.quiet:
    print(args.k)
elif args.verbose:
    print("Key is in {}".format(args.k))
    input()
else:
    print("Key in {}".format(args.k))
 
keys = {
"a": 440,
"bf": 466,
"b": 494,
"c": 523,
"df": 554,
"d": 587,
"ef": 622,
"e": 659,
"f": 698,
"fs": 740,
"g": 784,
"af": 831
}

hz = keys.get(args.k)

print(hz)

def piano(hz):
    
# =============================================================================
#     first = ("q","w","e","t","y","u","i")
#     second = ("a","s","d","f","g","h","j","k")
#     third = ("z","x","c","v","b","n","m",",",".")
#     up = ("tab")
#     down = ("shift")
# =============================================================================
    
    frequency = hz  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)
    
    # Generate a 440 Hz sine wave
    notes = np.sin(frequency * t * 2 * np.pi)
    
    # Ensure that highest value is in 16-bit range
    audio = notes * (2**15 - 1) / np.max(np.abs(notes))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    
    # Wait for playback to finish before exiting
    play_obj.wait_done()


# =============================================================================
# fd = sys.stdin.fileno()
# 
# oldterm = termios.tcgetattr(fd)
# newattr = termios.tcgetattr(fd)
# newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
# termios.tcsetattr(fd, termios.TCSANOW, newattr)
# 
# oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
# fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
# =============================================================================

note = input("> ")
try:
    while 1:
        try:
            #c = sys.stdin.read(1)
            if note == "a":
                #print("Got character", repr(c))
                freq = hz
                print(freq)
                piano(freq)
                note = input("> ")
            elif note == "q":
               # print("Got character", repr(c))
                freq = hz*2
                piano(freq)
                note = input("> ")
            elif note == "z":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "s":
                #print("Got character", repr(c))
                freq = hz*1.1227
                piano(freq)
                note = input("> ")
            elif note == "w":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "x":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "d":
                #print("Got character", repr(c))
                freq = hz*1.1886
                piano(freq)
                note = input("> ")
            elif note == "c":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "e":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "f":
                #print("Got character", repr(c))
                freq = hz*1.3340
                piano(freq)
                note = input("> ")
            elif note == "v":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "r":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "g":
                #print("Got character", repr(c))
                freq = hz*1.497
                piano(freq)
                note = input("> ")
            elif note == "b":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "t":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "h":
                #print("Got character", repr(c))
                freq = hz*1.586
                piano(freq)
                note = input("> ")
            elif note == "n":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "y":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "j":
                #print("Got character", repr(c))
                freq = hz*1.781
                piano(freq)
                note = input("> ")
            elif note == "m":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "u":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "k":
                #print("Got character", repr(c))
                freq = hz*2
                piano(freq)
                note = input("> ")
            elif note == ",":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            elif note == "i":
                #print("Got character", repr(c))
                freq = hz/2
                piano(freq)
                note = input("> ")
            else:
                print("Got character", repr(note))
        except IOError: pass
finally:
    print("done")