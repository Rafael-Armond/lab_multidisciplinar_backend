from models.user import User

class Respository:
  def __init__(self, session):
    self.__session = session
  
  def insert_user(self, username: str, role: str, created_at: str):
    with self.__session as session:
      new_user = User(username=username, role=role, created_at=created_at)
      session.add(new_user)
      session.commit()
      print(f"Usuário '{username}' adicionado com sucesso.")
      
