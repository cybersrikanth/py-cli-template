from Config.Views import Views

class View:
    views:Views

    def __init__(self) -> None:
        self.views = Views()

    def printWelcome(self) -> None:
        print(self.views.welcomeText)

    def printSuccess(self, text:str) -> None:
        print(self.views.successPrefix, text)

    def printError(self, text:str) -> None:
        print(self.views.errorPrefix, text)