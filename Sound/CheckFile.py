class CheckFileIsValid:
    """
    Checks if the file passed in as an argument is a .wav file.
    If it is not will raise an Exception.
    """

    @staticmethod
    def is_valid(filepath: str) -> None:
        if filepath.lower().endswith(".wav") is False:
            raise ValueError("File is not a .wav file!")
