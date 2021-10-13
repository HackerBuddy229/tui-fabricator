from TuiFabricator import TuiFabricator
from QueryDescriptor import QueryDescriptor
from QueryResponse import QueryResponse


class ExitHelper()

class BasicUtilityClass:

    @staticmethod
    def say_hi(args):
        amount_of_hi = args[0]
        print("hi" * amount_of_hi)

    @staticmethod
    def say_by():
        print("by")

    @staticmethod
    def say_fuck(args):
        who_is_an_asshole = args[0]
        why = args[1]

        print("fuck", who_is_an_asshole, "because of", why)


class BasicProgram:

    def __init__(self):
        self.descriptor = QueryDescriptor()
        self.descriptor.showPrompt = True

        self.responses = [
            QueryResponse("hi", 1, [int], BasicUtilityClass.say_hi),
            QueryResponse("by", 0, [], BasicUtilityClass.say_by),
            QueryResponse("fuck", 2, [None, None], BasicUtilityClass.say_fuck),
            QueryResponse("exit", 0, [None, None], BasicUtilityClass.say_fuck)
        ]

        self.tui = TuiFabricator(self.descriptor, self.responses)

    def run(self):
        self.tui.query()


BasicProgram().run()
