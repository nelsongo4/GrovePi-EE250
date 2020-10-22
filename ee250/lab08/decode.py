import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import os
import sys

MAX_FRQ = 2000
SLICE_SIZE = 0.15 #seconds
WINDOW_SIZE = 0.25 #seconds
NUMBER_DIC = {}

LOWER_FRQS = [697, 770, 852, 941]
HIGHER_FRQS = [1209, 1336, 1477, 1633]
FRQ_THRES = 20

def get_max_frq(frq, fft):
    max_frq = 0
    max_fft = 0
    for idx in range(len(fft)):
        if abs(fft[idx]) > max_fft:
            max_fft = abs(fft[idx])
            max_frq = frq[idx]
    return max_frq

def get_peak_frqs(frq, fft):
    #TODO: implement an algorithm to find the two maximum values in a given array
    #fft.sort()
    #fft.reverse()
    #fft_Max = fft[0]
    #fft_secMax = fft[1]
    #frq.sort()
    #frq.reverse()
    #frq_Max = frq[0]
    #frq_secMax = frq[1]
    max_frq = 0
    max_fft = 0 
    sec_max_fft = 0
    sec_max_frq = 0
    for idx in range(len(frq)):
        if abs(frq[idx]) > max_frq:
            sec_max_frq = max_frq
            max_frq = frq[idx]
        elif abs(frq[idx]) > sec_max_frq:
            sec_max_frq = frq[idx]
    for idx1 in range(len(fft)):
        if abs(fft[idx1]) > max_fft:
            sec_max_fft = max_fft
            max_fft = fft[idx1]
        elif abs(fft[idx1]) > sec_max_fft:
            sec_max_fft = fft[idx1]

    #get the high and low frequency by splitting it in the middle (1000Hz)
    low_frq = sec_max_frq
    high_frq = max_frq
    #spliting the FFT to high and low frequencies
    low_frq_fft = sec_max_fft
    high_frq_fft = max_fft
    return (get_max_frq(low_frq, low_frq_fft), get_max_frq(high_frq, high_frq_fft))

def get_number_from_frq(lower_frq, higher_frq):
    #TODO: given a lower frequency and higher frequency pair
    if lower_freq == 697 and higher_freq == 1209:
        value = '1'
    elif lower_freq == 697 and higher_freq == 1336:
        value = '2'
    elif lower_freq == 697 and higher_freq == 1477:
        value = '3'
    elif lower_freq == 770 and higher_freq == 1209:
        value = '4'
    elif lower_freq == 770 and higher_freq == 1336:
        value = '5'
    elif lower_freq == 770 and higher_freq == 1477:
        value = '6'
    elif lower_freq == 852 and higher_freq == 1209:
        value = '7'
    elif lower_freq == 852 and higher_freq == 1336:
        value = '8'
    elif lower_freq == 852 and higher_freq == 1477:
        value = '9'
    elif lower_freq == 941 and higher_freq == 1209:
        value = '*'
    elif lower_freq == 941 and higher_freq == 1336:
        value = '0'
    elif lower_freq == 941 and higher_freq == 1477:
        value = '#'
    else:
        value = '?'

    #      return the corresponding key otherwise return '?' if no match is found
    return value

def main(file):
    print("Importing {}".format(file))
    audio = AudioSegment.from_mp3(file)

    sample_count = audio.frame_count()
    sample_rate = audio.frame_rate
    samples = audio.get_array_of_samples()

    print("Number of channels: " + str(audio.channels))
    print("Sample count: " + str(sample_count))
    print("Sample rate: " + str(sample_rate))
    print("Sample width: " + str(audio.sample_width))

    period = 1/sample_rate                     #the period of each sample
    duration = sample_count/sample_rate         #length of full audio in seconds

    slice_sample_size = int(SLICE_SIZE*sample_rate)   #get the number of elements expected for [SLICE_SIZE] seconds

    n = slice_sample_size                            #n is the number of elements in the slice

    #generating the frequency spectrum
    k = np.arange(n)                                #k is an array from 0 to [n] with a step of 1
    slice_duration = n/sample_rate                   #slice_duration is the length of time the sample slice is (seconds)
    frq = k/slice_duration                          #generate the frequencies by dividing every element of k by slice_duration

    max_frq_idx = int(MAX_FRQ*slice_duration)       #get the index of the maximum frequency (2000)
    frq = frq[range(max_frq_idx)]                   #truncate the frequency array so it goes from 0 to 2000 Hz

    start_index = 0                                 #set the starting index at 0
    end_index = start_index + slice_sample_size      #find the ending index for the slice
    output = ''

    print()
    i = 1
    while end_index < len(samples):
        print("Sample {}:".format(i))
        i += 1

        #TODO: grab the sample slice and perform FFT on it
        sample_slice_fft = np.fft.fft(samples[start_index: end_index])/n
        #TODO: truncate the FFT to 0 to 2000 Hz
        sample_slice_fft = sample_slice_fft[range(max_frq_idx)] 
        #TODO: calculate the locations of the upper and lower FFT peak using get_peak_frqs()
        lower_fft,upper_fft = get_peak_frqs(frq,sample_slice_fft)
        #TODO: print the values and find the number that corresponds to the numbers

        #Incrementing the start and end window for FFT analysis
        start_index += int(WINDOW_SIZE*sample_rate)
        end_index = start_index + slice_sample_size

    print("Program completed")
    print("User typed: " + str(output))

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print("Usage: decode.py [file]")
        exit(1)
    main(sys.argv[1])





