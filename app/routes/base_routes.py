from abc import ABC, abstractmethod

class BaseRoutes(ABC):
  @abstractmethod
  def register_routes(self) -> None:
    raise Exception('Not implemented error')