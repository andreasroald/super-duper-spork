import pygame
from sprites import *
from levels import *

class Room_1:
    # Initialize the room 1 class
    def __init__(self):
        self.level = level_1
        self.npc_list = pygame.sprite.Group()

        # Room 1 NPCs
        gjertsen = NPC(150, 150, npc_face_1, "hey b0ss")

        self.npc_list.add(gjertsen)

class Room_2:
    # Initialize the room 1 class
    def __init__(self):
        self.level = level_2
        self.npc_list = pygame.sprite.Group()


room_1 = Room_1()
room_2 = Room_2()
