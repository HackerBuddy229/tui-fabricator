class UserResponse:

    _raw_input = ""
    _split_input = []

    def __init__(self, prompt=""):
        # get input with prompt
        self._raw_input = input(prompt)

    def get_key(self):
        if self._raw_input == "":
            return None

        # if input is not null then slit it by space-characters and fetch index 0
        self._split_input = self._raw_input.split()
        return self._split_input[0]

    def get_args(self):
        # return all list items that are not the key
        return self._split_input[1:]
