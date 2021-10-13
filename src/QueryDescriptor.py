class QueryDescriptor:
    showMenu = False

    showPrompt = False
    prompt = "?>"

    @staticmethod
    def with_show_menu(do_prompt, prompt="?>"):
        q = QueryDescriptor()
        q.showMenu = True

        q.showPrompt = do_prompt
        q.prompt = prompt

    @staticmethod
    def prompt_only(prompt="?>"):
        q = QueryDescriptor()
        q.showPrompt = True
        q.prompt = prompt

