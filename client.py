from logging.config import IDENTIFIER
from os import wait
import socket
import json
import sys
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class player():
    def __init__(self) -> None:
        self.id = 1
        self.score = 0
        self.address = None
    
    def server_connect(self, socket, addr='12345', id='thedude'):
        self.id = id
        self.address = addr
        print("looking for match...")
        thedict = {"code" : 1, "address" : addr, "id" : id}
        data = json.dumps(thedict)
        socket.sendall(bytes(data, encoding="utf-8"))
        
        rdata = socket.recv(1024)  
        if rdata:
            rdata = rdata.decode("utf-8")     
            rdata = json.loads(rdata)

            if rdata.get("response"):
                print("sucessfully connected to server!")
                
    def search_match(self, socket, timeout=100):
        deltat = time.time()
        x = 0
        match = False
        while True:
            print(f"looking for game... (elapsed {x}s)")
            dic = {"code" : 3, "address" : self.address, "id" : self.id}
            data = json.dumps(dic)
            socket.sendall(bytes(data, encoding="utf-8"))

            data = socket.recv(1024)
            if data:
                data = data.decode("utf-8")
                data = json.loads(data)

                if data.get("code") == 2: #match found!!!
                    opp = data.get("opponent")
                    print(f"match found! opponent is {opp['id']}" )
                    match = True

                    accept = input("accept this match? (y/n) ")
                    if accept == 'y' or accept == 'Y':
                        #accept the match- start the contract
                        print("match accepted!")
                        sdata = {"code" : 7, "address" : self.address, "id" : self.id, "opponent": opp, "note": "accept match"}
                        sdata = json.dumps(sdata)
                        socket.sendall(bytes(sdata, encoding="utf-8"))

                        self.search_match(socket)     
                    
                    elif accept  == 'n' or accept == 'N':
                        #decline match
                        print("match declined. re-entering the queue")
                        sdata = {"code" : 5, "address" : self.address, "id" : self.id, "opponent": opp, "note": "cancel match"}
                        sdata = json.dumps(sdata)
                        socket.sendall(bytes(sdata, encoding="utf-8"))

                        self.search_match(socket)
                         

                

            


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    p = player()
    addr = input("testaddres: ")
    id =  input("testid: ")
    p.server_connect(s, addr, id)
    time.sleep(.1)
    p.search_match(s)

#print(f"Received {data!r}")