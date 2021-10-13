class TuiOption:
    key = ""
    num_args = 0
    arg_types = []
    f = None

    def __init__(self, key, num_args, arg_types, f):
        self.key = key
        self.num_args = num_args
        self.arg_types = arg_types
        self.f = f
