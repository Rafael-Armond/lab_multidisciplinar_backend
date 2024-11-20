from typing import Dict, Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')

class BaseMapper(Generic[T], ABC):
  @abstractmethod
  def convertFromJsonToDto(self, json: Dict) -> T:
    pass
  
  @abstractmethod
  def convertFromDtoToJson(self, object: T) -> Dict:
    pass
