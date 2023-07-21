from colorama import Fore, Style


class Paint:
    """Paint class for painting string/fstring objects with different colors"""

    def __init__(self, strng):
        """String object needed for initialization"""
        self.strng = strng

        self._red = Fore.RED
        self._green = Fore.GREEN
        self._yellow = Fore.LIGHTYELLOW_EX
        self._cyan = Fore.LIGHTCYAN_EX
        self._magenta = Fore.MAGENTA

        self.reset = Style.RESET_ALL

    def red(self):
        """Paint object red"""
        return f"{self._red}{self.strng}{self.reset}"

    def green(self):
        """Paint object green"""
        return f"{self._green}{self.strng}{self.reset}"

    def yellow(self):
        """Paint object yellow"""
        return f"{self._yellow}{self.strng}{self.reset}"

    def cyan(self):
        """Paint object cyan"""
        return f"{self._cyan}{self.strng}{self.reset}"

    def magenta(self):
        """Paint object magenta"""
        return f"{self._magenta}{self.strng}{self.reset}"
