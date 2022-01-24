from abc import ABC , abstractmethod

class Page(ABC): # subclass of ABC
    """This is an abstract class
    """
    @abstractmethod
    def serve(self):
        pass