class CheckFileIsValid:
    """
    Checks if the file passed in as an argument is a .wav file.
    If it is not will raise an Exception.
    """

    @staticmethod
    def is_valid(filepath: str, check_for: str) -> None:
        if filepath.lower().endswith(check_for) is False:
            raise ValueError(f"File is not a {check_for} file!")
