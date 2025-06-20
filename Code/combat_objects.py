# Class that represents all objects on the board that can interact in combat
class CombatObject():
    def __init__(self, health, damage, combat_object_type, board_position, image):
        self._health = health 
        self._damage = damage
        self._combat_object_type = combat_object_type # used to determnine whether the target of something is a player or an enemy
        self._board_position = board_position
        self._image = image


    def attack(self):
        pass


    def change_health(self, health_change):
        self._health += health_change
    
    def get_image(self):
        return self._image

    def get_health(self):
        return self._health

    def get_damage(self):
        return self._damage
    
    def get_combat_object_type(self):
        return self._combat_object_type
    
    def get_board_position(self):
        return self._board_position
    
    def set_image(self, image):
        self._image = image

    def set_damage(self, damage):
        self._damage = damage
    
    def set_combat_object_type(self, combat_object_type):
        self._combat_object_type = combat_object_type
    
    def set_board_position(self, board_position):
        self._board_position = board_position

# How the player is represented in combat
class CombatPlayer(CombatObject):
    def __init__(self, health, damage, object_type, board_position, image):
        super().__init__(health, damage, object_type, board_position, image)

    # Allows player to do directional attacks, checks which enemies are in the line and damages them
    def attack(self, direction, enemies):
        for i in enemies:
            if direction == 0 and i.get_board_position()[0] > self._board_position[0] and i.get_board_position()[1] == self._board_position[1]:
                i.change_health(-self._damage)
            if direction == 1 and i.get_board_position()[1] > self._board_position[1] and i.get_board_position()[0] == self._board_position[0]:
                i.change_health(-self._damage)
            if direction == 2 and i.get_board_position()[0] < self._board_position[0] and i.get_board_position()[1] == self._board_position[1]:
                i.change_health(-self._damage)
            if direction == 3 and i.get_board_position()[1] < self._board_position[1] and i.get_board_position()[0] == self._board_position[0]:
                i.change_health(-self._damage)

    def get_image(self):
        return super().get_image()
    
    def get_health(self):
        return super().get_health()
    
    def get_damage(self):
        return super().get_damage()
    
    def get_board_position(self):
        return super().get_board_position()
    
    def get_combat_object_type(self):
        return super().get_combat_object_type()
    
    def set_image(self, image):
        return super().set_image(image)
    
    def set_damage(self, damage):
        return super().set_damage(damage)
    
    def set_board_position(self, board_position):
        return super().set_board_position(board_position)
    
    def set_combat_object_type(self, combat_object_type):
        return super().set_combat_object_type(combat_object_type)

# How the enemies are represented in combat
class Enemy(CombatObject):
    def __init__(self, health, damage, combat_object_type, board_position, image):
        super().__init__(health, damage, combat_object_type, board_position, image)

    def attack(self, target):
        target.change_health(-self._damage)

    def get_board_position(self):
        return super().get_board_position()
    
    def set_board_position(self, board_position):
        super().set_board_position(board_position)
    
    def get_image(self):
        return super().get_image()
    
    def set_image(self, image):
        super().set_image(image)

    # How enemies decide on their movement, runs by checking the distance to the player for every distance, removing any that collide with other enemies, then returning the result
    def decide_movement(self, player_board_position, allies, player):
        enemy_movement = []
        distance_checker = []

        
        distance_checker.append(abs((self._board_position[0] - 1) - player_board_position[0]) ** 2 + abs(self._board_position[1] - player_board_position[1]) ** 2)
        enemy_movement.append([self._board_position[0] - 1, self._board_position[1]])
        distance_checker.append(abs((self._board_position[0] + 1) - player_board_position[0]) ** 2 + abs(self._board_position[1] - player_board_position[1]) ** 2)
        enemy_movement.append([self._board_position[0] + 1, self._board_position[1]])
        distance_checker.append(abs(self._board_position[0] - player_board_position[0]) ** 2 + abs((self._board_position[1] - 1) - player_board_position[1]) ** 2)
        enemy_movement.append([self._board_position[0], self._board_position[1] - 1])
        distance_checker.append(abs(self._board_position[0] - player_board_position[0]) ** 2 + abs((self._board_position[1] + 1)- player_board_position[1]) ** 2)
        enemy_movement.append([self._board_position[0], self._board_position[1] + 1])

        for i in allies:
            continuous_checker = 0 
            for j in range(len(enemy_movement)):
                if i == enemy_movement[j-continuous_checker]:
                    enemy_movement.pop(j)
                    distance_checker.pop(j)
                    continuous_checker += 1

        if distance_checker == []:
            enemy_movement = [self.get_board_position()]
            distance_checker = [0]

        if self._board_position == player_board_position:
            self.attack(player)
            enemy_movement = [self.get_board_position()]
            distance_checker = [0]


        self._board_position = enemy_movement[distance_checker.index(min(distance_checker))]
        return self._board_position
