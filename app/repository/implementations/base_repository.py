from typing import TypeVar, Generic, List, Optional
from app.repository.interfaces.ibase_repository import IBaseRepository
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(IBaseRepository, Generic[T]):
    def __init__(self, session: Session, model: T):
        self.session: Session = session
        self.model = model

    def create(self, entity: T) -> T:
        try:
            with self.session as session:
                session.add(entity)
                session.commit()
                session.refresh(entity)
            return entity
        except Exception as e:
            self.session.rollback()
            raise RuntimeError(f"Erro ao atualizar entidade: {e}")

    def read(self, entity_id: int) -> Optional[T]:
        with self.session as session:
            return session.query(self.model).get(entity_id)

    def update(self, entity: T) -> T:
        try:
            with self.session as session:
                session.merge(entity)
                session.commit()
            return entity
        except Exception as e:
            self.session.rollback()
            raise RuntimeError(f"Erro ao atualizar entidade: {e}")

    def delete(self, entity_id: int) -> None:
        with self.session as session:
            entity = session.query(self.model).get(entity_id)
            if entity:
                session.delete(entity)
                session.commit()
            else:
                raise ValueError(f"Entity with ID {entity_id} not found.")

    def read_all(self) -> List[T]:
        with self.session as session:
            return session.query(self.model).all()
