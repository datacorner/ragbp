__author__ = "Benoit CAYLA"
__email__ = "admin@datacorner.fr"
__license__ = "MIT"

from abc import ABC, abstractmethod
from ragfmk.framework.sets.nearest import nearest

class IVStore:
   
    @abstractmethod
    def init():
        pass

    @property
    @abstractmethod
    def ready(self) -> bool:
        pass
    
    @abstractmethod
    def getNearest(self, vPrompt, k) -> nearest:
        pass
    
    @abstractmethod
    def add(self, item):
        pass