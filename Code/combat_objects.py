from abc import ABC, abstractmethod


class CombatObject(ABC):
    def __init__(self, health, speed, damage, inventory, combat_object_type, board_position, image):
        self._health = health
        self._speed = speed
        self._damage = damage
        self._inventory = inventory
        self._combat_object_type = combat_object_type
        self._board_position = board_position
        self._image = image

    @abstractmethod
    def attack(self):
        pass


    def change_health(self, health_change):
        self._health += health_change
    
    def get_image(self):
        return self._image

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
    
    def set_image(self, image):
        self._image = image

    def set_speed(self, speed):
        self._speed = speed

    def set_damage(self, damage):
        self._damage = damage

    def set_inventory(self, inventory):
        self._inventory = inventory
    
    def set_combat_object_type(self, combat_object_type):
        self._combat_object_type = combat_object_type
    
    def set_board_position(self, board_position):
        self._board_position = board_position

class Player(CombatObject):
    def __init__(self, health, speed, damage, inventory, object_type, board_position, image, spells):
        super().__init__(health, speed, damage, inventory, object_type, board_position, image)
        self._spells = spells

    def attack(self):
        pass

    def get_image(self):
        return super().get_image()
    
    def get_speed(self):
        return super().get_speed()
    
    def get_health(self):
        return super().get_health()
    
    def get_damage(self):
        return super().get_damage()
    
    def get_inventory(self):
        return super().get_inventory()
    
    def get_board_position(self):
        return super().get_board_position()
    
    def get_combat_object_type(self):
        return super().get_combat_object_type()
    
    def set_speed(self, speed):
        return super().set_speed(speed)
    
    def set_image(self, image):
        return super().set_image(image)
    
    def set_damage(self, damage):
        return super().set_damage(damage)
    
    def set_inventory(self, inventory):
        return super().set_inventory(inventory)
    
    def set_board_position(self, board_position):
        return super().set_board_position(board_position)
    
    def set_combat_object_type(self, combat_object_type):
        return super().set_combat_object_type(combat_object_type)
    
class Enemy(CombatObject):
    def __init__(self, health, speed, damage, inventory, combat_object_type, board_position, image):
        super().__init__(health, speed, damage, inventory, combat_object_type, board_position, image)

    def attack(self):
        pass

    def get_board_position(self):
        return super().get_board_position()
    
    def set_board_position(self, board_position):
        super().set_board_position(board_position)
    
    def get_image(self):
        return super().get_image()
    
    def set_image(self, image):
        super().set_image(image)

    def decide_movement(self, player_board_position):
        enemy_movement = []
        distance_checker = []

        
        distance_checker.append(abs((self._board_position[0] - 1) - player_board_position[0]) ** 2 + abs(self._board_position[1] - player_board_position))
        distance_checker.append(abs((self._board_position[0] + 1) - player_board_position[0]) ** 2 + abs(self._board_position[1] - player_board_position))
        distance_checker.append(abs(self._board_position[0] - player_board_position[0]) ** 2 + abs((self._board_position[1] - 1) - player_board_position))
        distance_checker.append(abs(self._board_position[0] - player_board_position[0]) ** 2 + abs((self._board_position[1] + 1)- player_board_position))

        return min(distance_checker)
