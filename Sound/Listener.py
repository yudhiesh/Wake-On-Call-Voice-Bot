import argparse
import os
import time
import wave
import pyaudio


class Listener:
    def __init__(self) -> None:
        self.chunk = 2048
        self.pyaudio_ = pyaudio.PyAudio()
        self.format_ = pyaudio.paInt16
        self.device_settings = (
            self.pyaudio_.get_default_input_device_info()
        )  # Set Frames
        self.channels = self.device_settings["maxInputChannels"]
        self.record_seconds = 2
        self.sample_rate = 8000
        self.stream = self.pyaudio_.open(
            format=self.format_,
            channels=self.channels,  # type: ignore
            rate=self.sample_rate,
            input=True,
            output=False,
            frames_per_buffer=self.chunk,
        )

    def save_audio(self, file_name, frames):
        print(f"Saving file to {file_name}")
        self.stream.stop_stream()
        self.stream.close()

        self.pyaudio_.terminate()

        # save audio file
        # open the file in 'write bytes' mode
        wf = wave.open(file_name, "wb")
        # set the channels
        wf.setnchannels(self.channels)
        # set the sample format
        wf.setsampwidth(self.p.get_sample_size(self.format_))
        # set the sample rate
        wf.setframerate(self.sample_rate)
        # write the frames as bytes
        wf.writeframes(b"".join(frames))
        # close the file
        wf.close()


class Interactive:
    def __init__(self, args) -> None:
        self.index = 0
        self.args = args

    def record(self):
        try:
            while True:
                listener = Listener()
                frames = []
                print("begin recording....")
                input(
                    "press enter to continue. the recoding will be {} seconds. press ctrl + c to exit".format(
                        self.args.seconds
                    )
                )
                time.sleep(0.2)  # so the mic don't pick up clicking sound
                for _ in range(
                    int(
                        (listener.sample_rate / listener.chunk)
                        * listener.record_seconds
                    )
                ):
                    data = listener.stream.read(
                        listener.chunk, exception_on_overflow=False
                    )
                    frames.append(data)
                save_path = os.path.join(
                    self.args.interactive_save_path, "{}.wav".format(self.index)
                )
                listener.save_audio(save_path, frames)
                self.index += 1
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
        except Exception as error:
            print(str(error))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
    Script to collect data for wake word training..
    To record environment sound run set seconds to None. This will
    record indefinitely until ctrl + c.
    To record for a set amount of time set seconds to whatever you want.
    To record interactively (usually for recording your own wake words N times)
    use --interactive mode.
    """
    )
    parser.add_argument(
        "--sample_rate", type=int, default=8000, help="the sample_rate to record at"
    )
    parser.add_argument(
        "--seconds",
        type=int,
        default=None,
        help="if set to None, then will record forever until keyboard interrupt",
    )
    parser.add_argument(
        "--save_path",
        type=str,
        default=None,
        required=False,
        help="full path to save file. i.e. /to/path/sound.wav",
    )
    parser.add_argument(
        "--interactive_save_path",
        type=str,
        default=None,
        required=False,
        help="directory to save all the interactive 2 second samples. i.e. /to/path/",
    )
    parser.add_argument(
        "--interactive",
        default=False,
        action="store_true",
        required=False,
        help="sets to interactive mode",
    )

    args = parser.parse_args()

    if args.interactive:
        if args.interactive_save_path is None:
            raise Exception("need to set --interactive_save_path")
        interactive = Interactive(args)
        interactive.record()
    else:
        if args.save_path is None:
            raise Exception("need to set --save_path")
