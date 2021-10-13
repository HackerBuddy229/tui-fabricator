class UserResponse:

    _raw_input = ""
    _split_input = []

    def __init__(self, prompt=""):
        self._raw_input = input(prompt)

    def get_key(self):
        self._split_input = self._raw_input.split(" ")[0]
        return self._split_input

    def get_args(self):
        return self._split_input[1:]
