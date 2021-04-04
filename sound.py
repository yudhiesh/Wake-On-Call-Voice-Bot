import pyaudio

audio = pyaudio.PyAudio()

devices = audio.get_device_count()

print(f"Number of devices: {devices}")
print(audio.get_default_input_device_info())
print(audio.get_default_output_device_info())
print(audio.get_device_info_by_index(0))
