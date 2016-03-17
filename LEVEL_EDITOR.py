import pygame
from resources import *

# colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Wall class
class Wall(pygame.sprite.Sprite):
    # Initialize the wall class
    def __init__(self, x, y, w=40, h=40, color=black, image=None, id=0):
        pygame.sprite.Sprite.__init__(self)
        if image is None:
            self.image = pygame.Surface((w, h))
            self.image.fill(color)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = id

# Editor class
class Editor:
    # Initialize the Editor
    def __init__(self):
        pygame.init()

        # Init the display
        self.display_width = 800
        self.display_height = 660
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("LEVEL EDITOR v2")

        # Framerate
        self.clock = clock = pygame.time.Clock()
        self.FPS = 60

        self.running = True

    # Make text object
    def text_object(self, msg, color, size):

        if size == "small":
            self.text_surface = self.smallfont.render(msg, False, color)
        elif size == "medium":
            self.text_surface = self.medfont.render(msg, False, color)
        elif size == "large":
            self.text_surface = self.largefont.render(msg, False, color)
        elif size == "huge":
            self.text_surface = self.hugefont.render(msg, False, color)

        return self.text_surface, self.text_surface.get_rect()

    # Render the text object
    def render_text(self, msg, color, y_displace=0, x_displace=0,  size="small"):
        self.text_surface, self.text_rect = self.text_object(msg, color, size)
        self.text_rect.x = (self.display_width / 2) + x_displace
        self.text_rect.y = (self.display_height / 2) + y_displace
        self.game_display.blit(self.text_surface, self.text_rect)

    # get coordinates of each tile
    def get_coordinates(self):

        coord_list = []

        for x in range(0, 15):
            for y in range(0, 20):
                coord_list.append((y*40, x*40))
        return coord_list

    # Starting a new game
    def new(self):
        self.coordinates = self.get_coordinates()
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        # Font variables
        self.font_file = "C:/Users/Admin/Documents/python/pygame/RPG-LevelEditor/8-Bit-Madness.ttf"
        self.smallfont = pygame.font.Font(self.font_file, 25)
        self.medfont = pygame.font.Font(self.font_file, 50)
        self.largefont = pygame.font.Font(self.font_file, 75)
        self.hugefont = pygame.font.Font(self.font_file, 150)

        self.guide = pygame.image.load("sprites/editor_guide.png")
        self.view_guide = True

        self.layer_1 = pygame.sprite.Group()
        self.layer_2 = pygame.sprite.Group()
        self.layer_3 = pygame.sprite.Group()
        self.current_layer = self.layer_1
        self.layer_num = 1
        self.view_l1 = True
        self.view_l2 = True
        self.view_l3 = True

        # Layer 1 tiles
        self.grass_1 = {
            "image": grass_1,
            "layer": self.layer_1,
            "name": "grass_1",
            "hotkey": pygame.K_1,
            "id": 1
        }
        self.grass_2 = {
            "image": grass_2,
            "layer": self.layer_1,
            "name": "grass_2",
            "hotkey": pygame.K_2,
            "id": 2
        }
        self.planks_1 = {
            "image": planks_1,
            "layer": self.layer_1,
            "name": "planks_1",
            "hotkey": pygame.K_3,
            "id": 3
        }
        self.red_sand_1 = {
            "image": red_sand_1,
            "layer": self.layer_1,
            "name": "red_sand_1",
            "hotkey": pygame.K_4,
            "id": 4
        }
        self.red_sand_2 = {
            "image": red_sand_2,
            "layer": self.layer_1,
            "name": "red_sand_2",
            "hotkey": pygame.K_5,
            "id": 5
        }
        self.metal_floor_1 = {
            "image": metal_floor_1,
            "layer": self.layer_1,
            "name": "metal_floor_1",
            "hotkey": pygame.K_6,
            "id": 6
        }
        self.layer_1_list = [self.grass_1, self.grass_2, self.planks_1,
                             self.red_sand_1, self.red_sand_2, self.metal_floor_1]

        # Layer 2 tiles
        self.void = {
            "image": void,
            "layer": self.layer_2,
            "name": "void",
            "hotkey": pygame.K_0,
            "id": -1
        }
        self.rock_wall_1 = {
            "image": rock_wall_1,
            "layer": self.layer_2,
            "name": "rock_wall_1",
            "hotkey": pygame.K_1,
            "id": 1
        }
        self.desk_1 = {
            "image": desk_1,
            "layer": self.layer_2,
            "name": "desk_1",
            "hotkey": pygame.K_2,
            "id": 2
        }
        self.office_chair_bottom = {
            "image": office_chair_bottom,
            "layer": self.layer_2,
            "name": "office_chair_bottom",
            "hotkey": pygame.K_3,
            "id": 3
        }
        self.flower_pot = {
            "image": flower_pot,
            "layer": self.layer_2,
            "name": "flower_pot",
            "hotkey": pygame.K_4,
            "id": 4
        }
        self.bed = {
            "image": bed,
            "layer": self.layer_2,
            "name": "bed",
            "hotkey": pygame.K_5,
            "id": 5
        }
        self.layer_2_list = [self.rock_wall_1, self.void, self.desk_1,
                             self.office_chair_bottom, self.flower_pot, self.bed]

        # Layer 3 tiles
        self.tree_1 = {
            "image": tree_1,
            "layer": self.layer_3,
            "name": "tree_1",
            "hotkey": pygame.K_1,
            "id": 1
        }

        self.metal_wall_top = {
            "image": metal_wall_top,
            "layer": self.layer_3,
            "name": "metal_wall_top",
            "hotkey": pygame.K_F1,
            "id": 2
        }
        self.metal_wall_left = {
            "image": metal_wall_left,
            "layer": self.layer_3,
            "name": "metal_wall_left",
            "hotkey": pygame.K_F2,
            "id": 3
        }
        self.metal_wall_bottom = {
            "image": metal_wall_bottom,
            "layer": self.layer_3,
            "name": "metal_wall_bottom",
            "hotkey": pygame.K_F3,
            "id": 4
        }
        self.metal_wall_right = {
            "image": metal_wall_right,
            "layer": self.layer_3,
            "name": "metal_wall_right",
            "hotkey": pygame.K_F4,
            "id": 5
        }

        self.metal_wall_tlcorner = {
            "image": metal_wall_tlcorner,
            "layer": self.layer_3,
            "name": "metal_wall_tlcorner",
            "hotkey": pygame.K_F5,
            "id": 6
        }
        self.metal_wall_trcorner = {
            "image": metal_wall_trcorner,
            "layer": self.layer_3,
            "name": "metal_wall_trcorner",
            "hotkey": pygame.K_F6,
            "id": 7
        }
        self.metal_wall_blcorner = {
            "image": metal_wall_blcorner,
            "layer": self.layer_3,
            "name": "metal_wall_blcorner",
            "hotkey": pygame.K_F7,
            "id": 8
        }
        self.metal_wall_brcorner = {
            "image": metal_wall_brcorner,
            "layer": self.layer_3,
            "name": "metal_wall_brcorner",
            "hotkey": pygame.K_F8,
            "id": 9
        }

        self.metal_wall_90deg_lt = {
            "image": metal_wall_90deg_lt,
            "layer": self.layer_3,
            "name": "metal_wall_90deg_lt",
            "hotkey": pygame.K_F9,
            "id": 10
        }
        self.metal_wall_90deg_tr = {
            "image": metal_wall_90deg_tr,
            "layer": self.layer_3,
            "name": "metal_wall_90deg_tr",
            "hotkey": pygame.K_F10,
            "id": 11
        }
        self.metal_wall_90deg_lb = {
            "image": metal_wall_90deg_lb,
            "layer": self.layer_3,
            "name": "metal_wall_90deg_lt",
            "hotkey": pygame.K_F11,
            "id": 12
        }
        self.metal_wall_90deg_br = {
            "image": metal_wall_90deg_br,
            "layer": self.layer_3,
            "name": "metal_wall_90deg_br",
            "hotkey": pygame.K_F12,
            "id": 13
        }

        self.office_chair_top = {
            "image": office_chair_top,
            "layer": self.layer_3,
            "name": "office_chair_top",
            "hotkey": pygame.K_2,
            "id": 14
        }
        self.plant_1 = {
            "image": plant_1,
            "layer": self.layer_3,
            "name": "plant_1",
            "hotkey": pygame.K_3,
            "id": 15
        }

        self.layer_3_list = [self.tree_1, self.metal_wall_top, self.metal_wall_left,
                             self.metal_wall_bottom, self.metal_wall_right, self.metal_wall_tlcorner,
                             self.metal_wall_trcorner, self.metal_wall_blcorner, self.metal_wall_brcorner,
                             self.metal_wall_90deg_lt, self.metal_wall_90deg_tr, self.metal_wall_90deg_lb,
                             self.metal_wall_90deg_br, self.office_chair_top, self.plant_1]

        self.current_block = self.grass_1
        self.did_layer_switch = False

        self.preview_blocks = pygame.sprite.Group()
        self.preview = self.current_block

        self.output_level = [
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        ]

        self.run()

    # Game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

    # Game loop - Events
    def events(self):
        # Keyboard & Quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                # Toggling guide view
                if event.key == pygame.K_SPACE:
                    if self.view_guide:
                        self.view_guide = False
                    else:
                        self.view_guide = True

                # Clearing current layer
                if event.key == pygame.K_ESCAPE:
                    self.current_layer.empty()

                # Layer view switching
                if event.key == pygame.K_LSHIFT:
                    if self.view_l1 and self.view_l2 and self.view_l3:
                        if self.current_layer == self.layer_1:
                            self.view_l1 = True
                            self.view_l2 = False
                            self.view_l3 = False
                        elif self.current_layer == self.layer_2:
                            self.view_l1 = False
                            self.view_l2 = True
                            self.view_l3 = False
                        elif self.current_layer == self.layer_3:
                            self.view_l1 = False
                            self.view_l2 = False
                            self.view_l3 = True
                    else:
                        self.view_l1 = True
                        self.view_l2 = True
                        self.view_l3 = True

                # Layer switching
                if event.key == pygame.K_UP and self.layer_num < 3:
                    self.layer_num += 1
                    self.did_layer_switch = True

                    self.view_l1 = True
                    self.view_l2 = True
                    self.view_l3 = True

                if event.key == pygame.K_DOWN and self.layer_num > 1:
                    self.layer_num -= 1
                    self.did_layer_switch = True

                    self.view_l1 = True
                    self.view_l2 = True
                    self.view_l3 = True

                # Tile switching
                if self.current_layer == self.layer_1:
                    for x in self.layer_1_list:
                        if event.key == x["hotkey"]:
                            self.current_block = x

                if self.current_layer == self.layer_2:
                    for x in self.layer_2_list:
                        if event.key == x["hotkey"]:
                            self.current_block = x

                if self.current_layer == self.layer_3:
                    for x in self.layer_3_list:
                        if event.key == x["hotkey"]:
                            self.current_block = x

                # Printing the level
                if event.key == pygame.K_RETURN:

                    # Layer 1 printing
                    for x in self.coordinates:
                        for w in self.layer_1:
                            if w.rect[0] == x[0] and w.rect[1] == x[1]:
                                self.output_level[int(x[1]/40)][int(x[0]/40)] = w.id

                    print("LAYER 1:")
                    for z in self.output_level:
                        print("{0},".format(z))
                    print("\n")
                    # Resetting output_level
                    self.output_level = [
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                    ]

                    # Layer 2 printing
                    for x in self.coordinates:
                        for w in self.layer_2:
                            if w.rect[0] == x[0] and w.rect[1] == x[1]:
                                self.output_level[int(x[1]/40)][int(x[0]/40)] = w.id

                    print("LAYER 2:")
                    for z in self.output_level:
                        print("{0},".format(z))
                    print("\n")
                    # Resetting output_level
                    self.output_level = [
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                    ]

                    # Layer 3 printing
                    for x in self.coordinates:
                        for w in self.layer_3:
                            if w.rect[0] == x[0] and w.rect[1] == x[1]:
                                self.output_level[int(x[1]/40)][int(x[0]/40)] = w.id

                    print("LAYER 3:")
                    for z in self.output_level:
                        print("{0},".format(z))
                    print("\n")
                    # Resetting output_level
                    self.output_level = [
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
                    ]

        # Mouse events
        # Tile placement
        if self.click[0]:
            for x in self.coordinates:
                if x[0] < self.mouse_x < x[0]+40:
                    if x[1] < self.mouse_y < x[1]+40:
                        for y in self.current_block["layer"]:
                            if y.rect[0] == x[0] and y.rect[1] == x[1]:
                                self.current_block["layer"].remove(y)

                        w = Wall(x[0], x[1], image=self.current_block["image"],
                                 id=self.current_block["id"])

                        self.current_block["layer"].add(w)

        # Tile erasing
        if self.click[2]:
            for x in self.coordinates:
                if x[0] < self.mouse_x < x[0]+40:
                    if x[1] < self.mouse_y < x[1]+40:
                        for w in self.current_block["layer"]:
                            if w.rect[0] == x[0] and w.rect[1] == x[1]:
                                self.current_block["layer"].remove(w)
                                break


    # Game loop - Update
    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.preview = self.current_block

        # Update current layer based on layer num
        if self.layer_num == 1:
            self.current_layer = self.layer_1
        elif self.layer_num == 2:
            self.current_layer = self.layer_2
        elif self.layer_num == 3:
            self.current_layer = self.layer_3

        # Update selected block if layer got changed
        if self.current_layer == self.layer_1 and self.did_layer_switch:
            self.current_block = self.layer_1_list[0]

        elif self.current_layer == self.layer_2 and self.did_layer_switch:
            self.current_block = self.layer_2_list[0]

        elif self.current_layer == self.layer_3 and self.did_layer_switch:
            self.current_block = self.layer_3_list[0]

        self.did_layer_switch = False

    # Game loop - Rendering/Drawing
    def draw(self):
        self.game_display.fill(white)

        if self.view_l1:
            self.layer_1.draw(self.game_display)
        if self.view_l2:
            self.layer_2.draw(self.game_display)
        if self.view_l3:
            self.layer_3.draw(self.game_display)

        if self.view_guide:
            self.game_display.blit(self.guide, (0, 0))

        pygame.draw.rect(self.game_display, black, (0, 600, 800, 60))
        self.render_text("TILE: {0}".format(self.current_block["name"].upper()),
                         white, x_displace=-385, y_displace=275)

        if not self.view_l1 or not self.view_l2 or not self.view_l3:
            self.render_text("LAYER: {0}".format(self.layer_num),
                             red, x_displace=-385, y_displace=300)
        else:
            self.render_text("LAYER: {0}".format(self.layer_num),
                             white, x_displace=-385, y_displace=300)

        self.game_display.blit(self.preview["image"], (750, 610))

        pygame.display.update()

# Creating the game window
e = Editor()

while e.running:
    e.new()

pygame.quit()
quit()
