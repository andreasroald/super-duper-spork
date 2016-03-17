import pygame
import random
import levels
from rooms import *
from sprites import *
from resources import *
from settings import *

# Create game class
class Game:
    # Initialize the game class
    def __init__(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        # Converting sprite alpha levels
        for x in resource_lists:
            for y in x:
                y.convert_alpha()


    # Functions that create the different layers
    def create_layer_1(self, level):
        levels.level_x = 0
        levels.level_y = 0
        for rows in level:
            for cols in rows:
                if cols == 1:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=grass_1)
                    self.layer_1.add(w)
                if cols == 2:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=grass_2)
                    self.layer_1.add(w)
                if cols == 3:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=planks_1)
                    self.layer_1.add(w)
                if cols == 4:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=red_sand_1)
                    self.layer_1.add(w)
                if cols == 5:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=red_sand_2)
                    self.layer_1.add(w)
                if cols == 6:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=metal_floor_1)
                    self.layer_1.add(w)

                levels.level_x += 40
            levels.level_x = 0
            levels.level_y += 40

    def create_layer_2(self, level):
        levels.level_x = 0
        levels.level_y = 0
        for rows in level:
            for cols in rows:
                if cols == -1:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=void)
                    self.layer_2.add(w)
                if cols == 1:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=rock_wall_1)
                    self.layer_2.add(w)
                if cols == 2:
                    w = Wall(levels.level_x, levels.level_y, 160, 80, image=desk_1)
                    self.layer_2.add(w)
                if cols == 3:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=office_chair_bottom)
                    self.layer_2.add(w)
                if cols == 4:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=flower_pot)
                    self.layer_2.add(w)
                if cols == 5:
                    w = Wall(levels.level_x, levels.level_y, 80, 120, image=bed)
                    self.layer_2.add(w)

                levels.level_x += 40
            levels.level_x = 0
            levels.level_y += 40

    def create_layer_3(self, level):
        levels.level_x = 0
        levels.level_y = 0
        for rows in level:
            for cols in rows:
                if cols == 1:
                    w = Wall(levels.level_x, levels.level_y, 160, 160, image=tree_1)
                    self.layer_3.add(w)

                if cols == 2:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_top)
                    self.layer_3.add(w)
                if cols == 3:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_left)
                    self.layer_3.add(w)
                if cols == 4:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_bottom)
                    self.layer_3.add(w)
                if cols == 5:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_right)
                    self.layer_3.add(w)

                if cols == 6:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_tlcorner)
                    self.layer_3.add(w)
                if cols == 7:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_trcorner)
                    self.layer_3.add(w)
                if cols == 8:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_blcorner)
                    self.layer_3.add(w)
                if cols == 9:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_brcorner)
                    self.layer_3.add(w)

                if cols == 10:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_lt)
                    self.layer_3.add(w)
                if cols == 11:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_tr)
                    self.layer_3.add(w)
                if cols == 12:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_lb)
                    self.layer_3.add(w)
                if cols == 13:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_br)
                    self.layer_3.add(w)

                if cols == 14:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=office_chair_top)
                    self.layer_3.add(w)
                if cols == 15:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=plant_1)
                    self.layer_3.add(w)
                if cols == "d":
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=door)
                    self.doors.add(w)

                levels.level_x += 40
            levels.level_x = 0
            levels.level_y += 40

    # Function that runs when a new room is entered
    def new_room(self):
        self.layer_1.empty()
        self.layer_2.empty()
        self.layer_3.empty()

        self.create_layer_1(self.current_room.level[0])
        self.create_layer_2(self.current_room.level[1])
        self.create_layer_3(self.current_room.level[2])

    # Starting a new game
    def new(self):
        self.current_room = room_1

        self.layer_1 = pygame.sprite.Group()
        self.layer_2 = pygame.sprite.Group()
        self.layer_3 = pygame.sprite.Group()
        self.text_boxes = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()

        self.new_room()

        self.player = Player(self.layer_2, self.current_room.npc_list, self.game_display)

        self.run()

    # Game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    # Game loop - Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if self.player.in_conversation:
                        self.player.in_conversation = False
                        self.player.talking_with = None
                    else:
                        self.player.test_for_npc()

    # Game loop - Update
    def update(self):
        self.current_room.npc_list.update()
        self.player.update()

        if pygame.sprite.spritecollide(self.player, self.doors, False):
            self.current_room

    # Game loop - Rendering/Drawing
    def draw(self):
        #self.game_display.fill(dark_gray)

        self.layer_1.draw(self.game_display)
        self.layer_2.draw(self.game_display)

        self.player.draw(self.game_display)
        for draw_npcs in self.current_room.npc_list:
            draw_npcs.draw(self.game_display)

        self.layer_3.draw(self.game_display)

        if self.player.in_conversation:
            self.text_boxes.empty()
            self.talk_box = Text_Box(self.player.talking_with.face, self.player.talking_with.lines)
            self.text_boxes.add(self.talk_box)
            self.text_boxes.draw(self.game_display)

        pygame.display.update()
        pygame.display.set_caption(title + " running at " + str(int(self.clock.get_fps())) + " frames per second")

game = Game()

while game.running:
    game.new()

pygame.quit()
quit()
