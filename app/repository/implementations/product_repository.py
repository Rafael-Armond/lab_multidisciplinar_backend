from sqlalchemy.orm import Session
from app.domain.models.base_model import BaseModel
from app.repository.implementations.base_repository import BaseRepository


class ProductRepository(BaseRepository):
  def __init__(self, session: Session, model: BaseModel):
    super().__init__(session, model)