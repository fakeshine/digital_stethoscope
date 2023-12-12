import wave
import struct
import time
import serial

comPort = "COM6"
# baudrate = 1000000
baudrate = 57600
nchannels = 1
sampwidth = 4
# sampleRate = 11000
sampleRate = 100
comptype = "NONE"
compname = "not compressed"
duration_seconds = 4

# Open a WAV file for writing
wavFile = wave.open("output.wav", "w")
wavFile.setparams((nchannels, sampwidth, sampleRate, 0, comptype, compname))

# Create a serial port instance
serInstance = serial.Serial(comPort, baudrate, timeout=0)

# Record data for the specified duration
start_time = time.time()
while (time.time() - start_time) < duration_seconds:
    bytes_to_read = serInstance.inWaiting()
    if bytes_to_read > 0:
        # print(f'Bytes to read: {bytes_to_read}')
        # Read the data from the serial port
        data = serInstance.read(bytes_to_read)
        print(f'Data received: {data}')
        # Write the data to the WAV file
        wavFile.writeframes(data)
    else:
        print('No bytes to read')

# Close the WAV file and serial port
wavFile.close()
serInstance.close()

print(f"Recording completed. Saved as 'output.wav'")
