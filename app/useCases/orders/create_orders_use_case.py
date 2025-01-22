from app.main import socketio


class CreateOrdersUseCase:
    def execute(self, data):
        socketio.emit("new_order", data, to=None)
        print("Novo pedido realizado")
        return "Novo Pedido"
