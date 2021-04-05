from RecordAudio import RecAUD
from PlaySound import PlayAudio

if __name__ == "__main__":
    FILEPATH = "../Audio/test_recording.wav"
    # guiAUD = RecAUD(filepath=FILEPATH)
    pa = PlayAudio(filepath=FILEPATH)
    pa.stream_out()
