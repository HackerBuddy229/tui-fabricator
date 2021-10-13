from UserResponse import UserResponse
from ArgumentHandler import ArgumentHandler


class TuiFabricator:
    _descriptor = None
    _responses = []

    def __init__(self, query_descriptor, query_responses):
        self._descriptor = query_descriptor
        self._responses = query_responses

    def query(self):
        # Present menu?
        if self._descriptor.showMenu:
            self._show_menu()

        # get key
        response = UserResponse()
        key = response.get_key()

        if key is None:
            print("Error")
            return
            # TODO: Add error handling here

        # check key validity / get query response
        selected_response = self._try_fetch_query_response(key)
        if selected_response is None:
            print("Error")
            return
            # TODO: Add error handling here

        # check arg validity[n.o/types]
        raw_args = response.get_args()
        if raw_args is None or len(raw_args) != selected_response.num_args:
            print("Error")
            return
            # TODO: Add error handling here

        args = ArgumentHandler.transform(selected_response.arg_types, raw_args)

        # execute if all is correct

        selected_response.f(args)


    def query_repeat(self, exit_descriptor):
        do_continue = True
        while do_continue:
            self.query()
            # TODO: Fix exit condition

    def _show_menu(self):
        pass
        # TODO: write this^^^

    def _try_fetch_query_response(self, key):
        for response in self._responses:
            if response.key == key:
                return response
        return None
