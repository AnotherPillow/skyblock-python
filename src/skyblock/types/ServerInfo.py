from typing import List
import json

class ServerInfo:
    def __init__(self, online: bool, players_online: str, max_players: str, player_list: List[str]):
        self.online = online
        self.players_online = players_online
        self.max_players = max_players
        self.player_list = player_list

    def dict(self):
        return {
            'online': self.online,
            'players_online': self.players_online,
            'max_players': self.max_players,
            'player_list': self.player_list,
        }

    def __str__(self):
        return json.dumps(self.dict())
    
    def __iter__(self):
        return iter(self.dict().items())
    
    def __getitem__(self, key):
        return self.dict()[key]