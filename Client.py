import socket, pickle

class Packet:
    def __init__(self):
        self.Type:str
        self.Data:object
        self.Response:str

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect(("localhost", 5000))

InitPacket = Packet()
InitPacket.Type = "Connect"
Client.send(pickle.dumps(InitPacket))

RecvPacket:Packet = pickle.loads(Client.recv(1024))

while True:
    SendPacket:Packet = Packet()
    SendPacket.Type = "Update"
    Client.send(pickle.dumps(SendPacket))

    RecvPacket:Packet = pickle.loads(Client.recv(1024))