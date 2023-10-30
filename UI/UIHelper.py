
import sys


class UIHelper:

    @staticmethod
    def ExitIfCommanded(input: str):
        if input.lower() == 'exit':
            sys.exit()
