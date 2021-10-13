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
        response = UserResponse(self._descriptor.prompt)
        key = response.get_key()

        if key is None:
            self._default_error_handler("No key provided!")
            return

        # check key validity / get query response
        selected_response = self._try_fetch_query_response(key)
        if selected_response is None:
            self._default_error_handler("Key did not match alternatives!")
            return

        # check arg validity[n.o/types]
        raw_args = response.get_args()
        if raw_args is None or len(raw_args) != selected_response.num_args:
            self._default_error_handler("Argument error!")
            return

        args = ArgumentHandler.transform(selected_response.arg_types, raw_args)

        # execute if all is correct
        if selected_response.num_args > 0:
            selected_response.f(args)
        else:
            selected_response.f()

    def query_repeat(self, exit_condition):
        while exit_condition[0]:
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

    def _default_error_handler(self, msg):
        print("ERROR:", msg)
        self.query()
