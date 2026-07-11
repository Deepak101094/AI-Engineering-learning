from abc import ABC, abstractmethod


class LLMService(ABC):
     """
    Contract for every AI provider.
    """
     
     @abstractmethod

     def ask(self, message):
        """
        Generate a complete response.
        """

        pass
     
     @abstractmethod
     def stream(self, message):         
        """
        Stream the response.
        """

        pass