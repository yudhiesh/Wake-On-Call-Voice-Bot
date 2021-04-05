import tkinter as tk
import wave

import pyaudio
from CheckFile import CheckFileIsValid


class PlayAudio:
    """
    Play audio from the filepath provided
    @param:
    filepath: str
    File path of the audio file
    """

    def __init__(
        self,
        filepath: str,
        format_: int = pyaudio.paInt16,
        frames_per_buffer: int = 2048,
    ):
        self.filepath = filepath
        CheckFileIsValid().is_valid(self.filepath)
        self.format_ = format_
        self.frames_per_buffer = frames_per_buffer
        self.pyaudio_ = pyaudio.PyAudio()
        self.device_settings = (
            self.pyaudio_.get_default_input_device_info()
        )  # Set Frames
        self.input_device_index = self.device_settings["index"]
        self.wave_file = wave.open(self.filepath)
        self.output_device_info = self.pyaudio_.get_default_output_device_info()
        self.output_device_index = self.output_device_info["index"]

    def stream_out(self) -> None:
        out = self.pyaudio_.open(
            rate=self.wave_file.getframerate(),
            channels=self.wave_file.getnchannels(),
            format=self.format_,
            output=True,
            output_device_index=self.output_device_index,  # type: ignore
        )
        output_audio = self.wave_file.readframes(5 * self.wave_file.getframerate())
        out.write(output_audio)
