from app.main import socketio


class CreateShipmentUseCase:
    def execute(self, data):
        print("Teste 123: ", data)
        socketio.emit("new_shipment", data, to=None)
        return "Remessa enviada ao cliente"
