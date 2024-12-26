from app.domain.models.base_model import BaseModel

# Esse model eu vou usar somente para lançar na fila (mensageria)
class Shipment(BaseModel):
  def __init__(self, product, amount):
    self.product = product
    self.amount = amount
  
  
  