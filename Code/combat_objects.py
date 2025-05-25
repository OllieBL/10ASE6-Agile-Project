from abc import ABC, abstractmethod


class CombatObject(ABC):
    def __init__(self, health, speed, damage, inventory, combat_object_type, board_position):
        self._health = health
        self._speed = speed
        self._damage = damage
        self._inventory = inventory
        self._combat_object_type = combat_object_type
        self._board_position = board_position

    @abstractmethod
    def attack(self):
        pass


    def change_health(self, health_change):
        self._health += health_change
    

    def get_health(self):
        return self._health

    def get_speed(self):
        return self._speed

    def get_damage(self):
        return self._damage

    def get_inventory(self):
        return self._inventory
    
    def get_combat_object_type(self):
        return self._combat_object_type
    
    def get_board_position(self):
        return self._board_position

class Player(CombatObject):
    def __init__(self, health, speed, damage, inventory, object_type, spells):
        super().__init__(health, speed, damage, inventory, object_type)
        self._spells = spells

    def attack(self):
        pass