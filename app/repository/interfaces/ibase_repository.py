from typing import TypeVar, Generic, List, Optional
from abc import ABC, abstractmethod

T = TypeVar('T')

class IBaseRepository(ABC, Generic[T]):
  @abstractmethod
  def create(self, entity: T) -> T:
    pass

  @abstractmethod
  def read(self, entity_id: int) -> Optional[T]:
    pass

  @abstractmethod
  def update(self, entity: T) -> T:
    pass

  @abstractmethod
  def delete(self, entity_id: int) -> None:
    pass

  @abstractmethod
  def read_all(self) -> List[T]:
    pass
