import argparse

class Args:
    
    parser:argparse.ArgumentParser

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.configParser()
    
    def configParser(self) -> None:
        # Add your own arguments here
        self.parser.add_argument("-t", "--target", type=str, help="Target IP address")
        self.parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
    
    def getArgs(self):
        return self.parser.parse_args()