
import sys


class UIHelper:
    """Helper class to exit application when the user types exit"""

    @staticmethod
    def ExitIfCommanded(input: str):
        """Function that exist the application when user types exit"""
        if input.lower() == 'exit':
            sys.exit()
