import pydub

from CheckFile import CheckFileIsValid


class ConvertToMP3:
    def __init__(
        self, input_filepath: str, output_filepath: str, convert_to: str = "wav"
    ) -> None:
        self.input_filepath = input_filepath
        CheckFileIsValid().is_valid(filepath=self.input_filepath, check_for=".wav")
        self.output_filepath = output_filepath
        CheckFileIsValid().is_valid(filepath=self.output_filepath, check_for=".mp3")
        self.convert_to = convert_to
        self.sound = pydub.AudioSegment.from_mp3(self.input_filepath)
        self.sound.export(
            out_f=self.output_filepath, format=self.convert_to
        )  # type:ignore
