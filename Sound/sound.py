from play_sound import PlayAudio
from record_audio import RecAUD
from convert_to_mp3 import ConvertToMP3

if __name__ == "__main__":
    FILEPATH = "../Audio/test_recording.wav"
    OUTPUT_FILEPATH = "../Audio/test_recording.mp3"
    # guiAUD = RecAUD(filepath=FILEPATH)
    # pa = PlayAudio(filepath=FILEPATH)
    # pa.stream_out()
    ConvertToMP3(input_filepath=FILEPATH, output_filepath=OUTPUT_FILEPATH)
