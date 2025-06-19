# How the player is represented in the map
class Player():
    def __init__(self, pos, combat_state):
        self._pos = pos
        self._combat_state = combat_state # This is the player combat object, and is saved through this

    def get_pos(self):
        return self._pos
    
    def get_combat_state(self):
        return self._combat_state
    
    def set_pos(self, new_pos):
        self._pos = new_pos