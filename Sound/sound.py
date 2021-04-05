from PlaySound import PlayAudio
from RecordAudio import RecAUD
from ConvertToMP3 import ConvertToMP3

if __name__ == "__main__":
    FILEPATH = "../Audio/test_recording.wav"
    OUTPUT_FILEPATH = "../Audio/test_recording.mp3"
    # guiAUD = RecAUD(filepath=FILEPATH)
    # pa = PlayAudio(filepath=FILEPATH)
    # pa.stream_out()
    convert_to_mp3 = ConvertToMP3(
        input_filepath=FILEPATH, output_filepath=OUTPUT_FILEPATH
    )
