from ast import For
from colorama import Fore

class Views:
    
    welcomeText: str
    horizontalLineChar: str
    successPrefix: str
    errorPrefix: str

    def __init__(self) -> None:
        self.addConfigs()


    def addConfigs(self) -> None:
        self.welcomeText = """
__          __  _                          
\ \        / / | |                         
 \ \  /\  / /__| | ___ ___  _ __ ___   ___ 
  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \
   \  /\  /  __/ | (_| (_) | | | | | |  __/
    \/  \/ \___|_|\___\___/|_| |_| |_|\___|
                                           
                                           
        """
        self.horizontalLineChar = "-"
        self.successPrefix = Fore.GREEN + "+" + Fore.RESET
        self.errorPrefix = Fore.RED + "-" + Fore.RESET