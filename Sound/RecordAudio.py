import tkinter as tk
import wave

import pyaudio

from CheckFile import CheckFileIsValid


class RecAUD:
    """
    Records audio and saves it to the filepath that is provided
    @param:
    filepath: str
    File path of the audio file
    """

    def __init__(
        self,
        filepath=str,
        chunk: int = 2048,
        pyaudio_format: int = pyaudio.paInt16,
        rate: int = 44100,
        pyaudio_: pyaudio.PyAudio = pyaudio.PyAudio(),
    ):

        # Start Tkinter and set Title
        self.main = tk.Tk()
        self.collections = []
        self.main.geometry("500x300")
        self.main.title("Record")
        self.chunk = chunk
        self.format_ = pyaudio_format
        self.rate = rate
        self.pyaudio_ = pyaudio_
        self.frames = []
        self.st = 1
        self.device_settings = pyaudio_.get_default_input_device_info()  # Set Frames
        self.input_device_index = self.device_settings["index"]
        self.channels = self.device_settings["maxInputChannels"]
        self.stream = self.pyaudio_.open(  # type: ignore
            rate=self.rate,
            format=self.format_,
            channels=self.channels,  # type: ignore
            input_device_index=self.input_device_index,  # type: ignore
            input=True,
            output=False,
            frames_per_buffer=self.chunk,
        )
        self.filepath = filepath
        CheckFileIsValid().is_valid(self.filepath)

        self.buttons = tk.Frame(self.main, padx=120, pady=20)

        # Pack Frame
        self.buttons.pack(fill=tk.BOTH)

        # Start and Stop buttons
        self.start_recording = tk.Button(
            self.buttons,
            width=10,
            padx=10,
            pady=5,
            text="Start Recording",
            command=lambda: self.start_record(),
        )
        self.start_recording.grid(row=0, column=0, padx=50, pady=5)
        self.stop_recording = tk.Button(
            self.buttons,
            width=10,
            padx=10,
            pady=5,
            text="Stop Recording",
            command=lambda: self.stop(),
        )
        self.stop_recording.grid(row=1, column=0, columnspan=1, padx=50, pady=5)

        tk.mainloop()

    def start_record(self) -> None:
        self.st = 1
        self.frames = []
        stream = self.pyaudio_.open(
            format=self.format_,
            channels=self.channels,  # type: ignore
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )
        while self.st == 1:
            data = stream.read(self.chunk)
            self.frames.append(data)
            print("* recording")
            self.main.update()

        stream.close()

        wf = wave.open(self.filepath, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.pyaudio_.get_sample_size(self.format_))
        wf.setframerate(self.rate)
        wf.writeframes(b"".join(self.frames))
        wf.close()

    def stop(self) -> None:
        self.st = 0
