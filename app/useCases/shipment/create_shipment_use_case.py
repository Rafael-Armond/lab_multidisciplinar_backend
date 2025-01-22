from app.main import socketio


class CreateShipmentUseCase:
    def execute(self, data):
        print("Enviando remessas ", data)
        socketio.emit("new_shipment", data, to=None)
        return "Remessa enviada ao cliente"
