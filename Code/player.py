class Player():
    def __init__(self, location, combat_state):
        self._location = location
        self._combat_state = combat_state

    def get_location(self):
        return self._location
    
    def get_combat_state(self):
        return self._combat_state