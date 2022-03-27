import socket
from threading import Thread
from queue import Queue
from enum import Enum
import sys
import json
from typing import Dict

class player():
    def __init__(self, addr, id):
        self.addr = addr
        self.id = id
        self.score = 0
        self.client = None
    
    def to_dict(self):
        dic = dict(address=self.addr, id=self.id, score= self.score)
        return dic

class MatchServer(object):
    def __init__(self, host, port) -> None:
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))


        self.playerqueue = []
        self.pendingmatch = []
 
    def listen(self):
        self.sock.listen(5)
        while True:
            client, addr = self.sock.accept()
            Thread(target = self.listen_new_player,args = (client,addr)).start()

    def check_chain_score(self, player, debugscore=0):
        #send player.address to blockchain to query their score
        return debugscore
    
    def listen_new_player(self, client, addr):
        #initial connection message
        # {"address" : addr, "id" : player01}
        while True:
            data = client.recv(1024)
            p = None

            if data:
                data = data.decode("utf-8")
                data = json.loads(data)
                
                p = player(data.get("address"), data.get("id"))
                p.score = self.check_chain_score(p) #get scores from blockchain  
                p.client = client

                if data.get("code") == 1: #Initial conn data
                    print(f"player {p.id} with score {p.score} @ {p.addr} connected!")

                    #send back response- successful conn
                    rdata = {"code" : 3, "response" : True}
                    response = json.dumps(rdata)
                    client.sendall(bytes(response, encoding="utf-8"))
                
                if data.get("code") == 1: #match search ping
                    ### MATCHMAKING
                    self.match_player(p, client)
                
                if data.get("code") == 10: #quit
                    print(f"player {p.id} @ {p.addr} disconnected!")
                    self.playerqueue.remove(p)
                    client.close()


        
    ### MATCHMAKING
    def match_player(self, player, client):
        if not player in self.playerqueue:
            self.playerqueue.insert(0, player)

        for opponent in self.playerqueue:
            #match found??
            if player.score == opponent.score and player != opponent:
                print(f"round {player.score} match found: {player.id} vs {opponent.id}")

                self.playerqueue.remove(player)
                self.playerqueue.remove(opponent)

                
                ## SEND INFO TO CURRENT PLAYER
                dic = {"code": 2, "opponent": opponent.to_dict()}
                data = json.dumps(dic)
                client.sendall(bytes(data, encoding="utf-8"))
                
                #SEND INFO TO CURRENT OPPONENT
                dic = {"code": 2, "opponent": player.to_dict()}
                data = json.dumps(dic)
                opponent.client.sendall(bytes(data, encoding="utf-8"))
            
            
          
### MAIN

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    print("server booting...")
    MatchServer(HOST,PORT).listen()