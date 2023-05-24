import socket, pickle, threading

Users = []

class User:
    def __init__(self) -> None:
        self.Client:socket.socket
        self.Address:tuple
        self.Thread:threading.Thread

class Packet:
    def __init__(self):
        self.Type:str
        self.Data:object
        self.Response:str

def UserThread(user:User):
    InitPacket:Packet = pickle.loads(user.Client.recv(1024))
    if InitPacket.Type == "Connect":
        RespPacket = Packet()
        RespPacket.Type = "Connect"
        RespPacket.Response = "OK"
        user.Client.send(pickle.dumps(RespPacket))

    while True:
        try:
            Data = user.Client.recv(1024)
            if Data == "" or Data == None: raise Exception()
            IncomingPacket:Packet = pickle.loads(Data)
        except:
            print("Disconnected", user.Address)
            Users.remove(user)
            break

        
        ResponsePacket:Packet = Packet()

        ResponsePacket.Type = "Update"

        user.Client.send(pickle.dumps(ResponsePacket))


Address = ("localhost",5000)
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(Address)

Server.listen(10) # Max Clients


print("Listening on", Address)
while True:
    _Client, _Address = Server.accept()
    print("Incoming connection from", _Address)

    user = User()
    user.Client = _Client
    user.Address = _Address
    user.Thread = threading.Thread(target=UserThread, args=[user])
    user.Thread.start()

    Users.append(user)
