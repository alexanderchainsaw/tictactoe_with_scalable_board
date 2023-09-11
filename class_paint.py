from colorama import Fore, Style


class Paint:
    """Paint class for painting string/fstring objects with different colors"""

    def __init__(self, strng):
        """String object needed for initialization"""
        self.strng = strng

        self.__red = Fore.RED
        self.__green = Fore.GREEN
        self.__yellow = Fore.LIGHTYELLOW_EX
        self.__cyan = Fore.LIGHTCYAN_EX
        self.__magenta = Fore.MAGENTA

        self.__reset = Style.RESET_ALL

    def red(self):
        """Paint object red"""
        return f"{self.__red}{self.strng}{self.__reset}"

    def green(self):
        """Paint object green"""
        return f"{self.__green}{self.strng}{self.__reset}"

    def yellow(self):
        """Paint object yellow"""
        return f"{self.__yellow}{self.strng}{self.__reset}"

    def cyan(self):
        """Paint object cyan"""
        return f"{self.__cyan}{self.strng}{self.__reset}"

    def magenta(self):
        """Paint object magenta"""
        return f"{self.__magenta}{self.strng}{self.__reset}"
