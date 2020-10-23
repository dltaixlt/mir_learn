import librosa
import numpy as np

fname = 'mirex06train/train1.wav'
x, sr = librosa.load(fname)

tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')

print(tempo)