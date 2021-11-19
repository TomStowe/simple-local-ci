
"""
    Defines the logger used for displaying the CI status
"""
class Logger:
    # Colour Constants
    successColour = "\033[92m"
    notificationColour = "\033[96m"
    interruptedColour = "\033[94m"
    warningColour = "\033[93m"
    errorColour = "\033[91m"
    endColour = "\033[0m"
    
    # How many spaces to pad before each message
    padding = 3
    
    # The longest printed message possible (default is no name + RUNNING (inc spaces))
    longestPossibleMessage = 13
    
    """
        The constructor for the logger
        noColour: A bool to determine whether no colour should be used in the logging messages
    """
    def __init__(self, noColour = True):
        if (noColour):
            self.successColour = ""
            self.notificationColour = ""
            self.interruptedColour = ""
            self.warningColour = ""
            self.variable = ""
            self.errorColour = ""
            self.endColour = ""
    
    """
        Initialises the printer to allow for formatting to be done properly
        jobs: The list of jobs to be done
    """
    def setupLogPrinter(self, jobs):
        # Iterate over the jobs names, and get the longest length
        self.longestNameLength = int(0)
        for job in jobs:
            if (len(job.name) > self.longestNameLength):
                self.longestNameLength = len(job.name)
                
        # Update the longest possible message for main message printing
        self.longestPossibleMessage += self.longestNameLength

    """
        Print a main testing message
        message: The message to print
    """
    def printMainTestingMessage(self, message: str):
        dashes = "-" * (((self.longestPossibleMessage - len(message) - 2) // 2) + self.padding)
        
        print(f"{self.notificationColour}{dashes} {message} {dashes}{self.endColour}")
        
    """
        Print a message that the test is running
        name: The name of the test that is being run
    """
    def printRunningMessage(self, name: str):
        self.__printMessage(self.warningColour, name, "RUNNING", "\r")
        
    """
        Print a message that the test has been interrupted
        name: The name of the test that is being run
    """
    def printInterruptedMessage(self, name: str):
        self.__printMessage(self.interruptedColour, name, "INTERRUPTED")
        
    """
        Print a message that the test has failed
        name: The name of the test that is being run
    """
    def printErrorMessage(self, name: str):
        self.__printMessage(self.errorColour, name, "FAILURE")
        
    """
        Print a message that the test has timed out
        name: The name of the test that is being run
    """
    def printTimeoutMessage(self, name: str):
        self.__printMessage(self.errorColour, name, "TIMEOUT")
        
    """
        Print a message that the test has been a success
        name: The name of the test that is being run
    """
    def printSuccessMessage(self, name: str):
        self.__printMessage(self.successColour, name, "SUCCESS")
        
    """
        Generic message printer
        colour: The colour of the text to print
        name: The name of the test that is being printed
        text: The text to print
        end (default=None): What to include at the end of the print statement
    """
    def __printMessage(self, colour: str, name: str, text: str, end=None):
        # Pad the name if necessary
        name += " " * (self.longestNameLength - len(name))
        messagePadding = " " * self.padding
        
        print(f"{colour}{messagePadding}{name} - {text}{self.endColour}\t", end=end)

if __name__ == "__main__":
    logger = Logger()
    logger.setupLogPrinter([])
    logger.printMainTestingMessage("Testing Logger Started")
    logger.printRunningMessage("Test Name")
    logger.printInterruptedMessage("Test Name")
    logger.printErrorMessage("Test Name")
    logger.printTimeoutMessage("Test Name")
    logger.printSuccessMessage("Test Name")
    logger.printMainTestingMessage("Testing Logger Complete")