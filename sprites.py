from settings import *
from resources import *
import random
import pygame
import math
vec = pygame.math.Vector2

# Function that takes to points and returns the angle between them
def look_at(x1, x2, y1, y2, image, image_original, old_rect):
    angle = math.atan2(x1 - x2, y1 - y2)
    angle_degrees = (180 * angle / math.pi) + 180

    image = pygame.transform.rotate(image_original, int(angle_degrees))
    image_rect = image.get_rect(center=old_rect.center)

    return image, image_rect

# Text rendering functions
def text_object(msg, color, size):

    if size == "small":
        text_surface = smallfont.render(msg, False, color)
    elif size == "medium":
        text_surface = medfont.render(msg, False, color)
    elif size == "large":
        text_surface = largefont.render(msg, False, color)
    elif size == "huge":
        text_surface = hugefont.render(msg, False, color)

    return text_surface, text_surface.get_rect()

def render_text(msg, color, display, y=0, x=0,  size="small"):
    text_surface, text_rect = text_object(msg, color, size)
    text_rect.x = x
    text_rect.y = y
    display.blit(text_surface, text_rect)


# Creating a player class
class Player(pygame.sprite.Sprite):
    # Initialize the player class
    def __init__(self, collide_list, npc_list, display):
        pygame.sprite.Sprite.__init__(self)

        self.image = player_list[0]
        self.image_original = self.image.copy()
        self.image_rect = self.image.get_rect()
        self.rect = self.image_rect.copy()
        self.rect.inflate_ip((-40,-40))
        self.rect.center = (display_width/2, display_height/2)

        self.collide_list = collide_list
        self.npc_list = npc_list

        self.display = display

        self.moving_up = False
        self.moving_left = False
        self.moving_down = False
        self.moving_right = False

        self.up_lock = False
        self.left_lock = False
        self.down_lock = False
        self.right_lock = False

        self.walk_counter = 0
        self.walk_number = 1

        self.in_conversation = False
        self.talking_with = None

    # Player event handling
    def event_handling(self):
        # Movement keys event handling
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not self.up_lock:
            self.moving_up = True
            self.down_lock = True
        else:
            self.moving_up = False
            self.down_lock = False

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.left_lock:
            self.moving_left = True
            self.right_lock = True
        else:
            self.moving_left = False
            self.right_lock = False

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not self.down_lock:
            self.moving_down = True
            self.up_lock = True
        else:
            self.moving_down = False
            self.up_lock = False

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.right_lock:
            self.moving_right = True
            self.left_lock = True
        else:
            self.moving_right = False
            self.left_lock = False

    # Movement and player control
    def movement(self):
        self.old_rect  = self.image_rect.copy()
        self.speed_x = 0
        self.speed_y = 0
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        # Make player accelerate
        if self.moving_up and not self.in_conversation:
            self.speed_y = -5
        if self.moving_left and not self.in_conversation:
            self.speed_x = -5
        if self.moving_down and not self.in_conversation:
            self.speed_y = 5
        if self.moving_right and not self.in_conversation:
            self.speed_x = 5

        # Make diagonal movement as fast as horizontal/vertical
        if self.speed_y != 0 and self.speed_x != 0:
            self.speed_x *= (math.sqrt(2)/2)
            self.speed_y *= (math.sqrt(2)/2)

        # Make player look at mouse
        self.image, self.image_rect = look_at(self.mouse_x, self.rect.center[0], self.mouse_y,
                                              self.rect.center[1], self.image, self.image_original, self.old_rect)

        # X-axis movement
        self.rect.x += self.speed_x

        # Check if the player hit any walls during X-movement
        hit_list = pygame.sprite.spritecollide(self, self.collide_list, False)
        for hits in hit_list:
            if self.speed_x > 0:
                self.rect.right = hits.rect.left
                self.moving_right = False
            else:
                self.rect.left = hits.rect.right
                self.moving_left = False

        # Check if the player hit any NPCs during X-movement
        hit_list = pygame.sprite.spritecollide(self, self.npc_list, False)
        for hits in hit_list:
            if self.speed_x > 0:
                self.rect.right = hits.rect.left
                self.moving_right = False
            else:
                self.rect.left = hits.rect.right
                self.moving_left = False

        # Y-axis movement
        self.rect.y += self.speed_y

        # Check if the player hit any walls during Y-movement
        hit_list = pygame.sprite.spritecollide(self, self.collide_list, False)
        for hits in hit_list:
            if self.speed_y > 0:
                self.rect.bottom = hits.rect.top
                self.moving_down = False
            else:
                self.rect.top = hits.rect.bottom
                self.moving_up = False

        # Check if the player hit any NPCs during Y-movement
        hit_list = pygame.sprite.spritecollide(self, self.npc_list, False)
        for hits in hit_list:
            if self.speed_y > 0:
                self.rect.bottom = hits.rect.top
                self.moving_down = False
            else:
                self.rect.top = hits.rect.bottom
                self.moving_up = False

        # Walking animations
        if self.moving_up or self.moving_left or self.moving_down or self.moving_right:
            if not self.in_conversation:
                self.walk_counter += 1

                if self.walk_counter >= 5:

                    self.walk_counter = 0
                    self.image_original = player_list[self.walk_number]
                    self.walk_number += 1

                    if self.walk_number >= 12:
                        self.walk_number = 1
        else:
            self.image_original = player_list[0]

        # Reposition drawing rect
        self.image_rect.center = self.rect.center

    # NPC interaction
    def test_for_npc(self):
        for in_npc_zone in self.npc_list:
            if self.rect.colliderect(in_npc_zone.talk_zone):
                self.in_conversation = True
                self.talking_with = in_npc_zone

    # Update the player class
    def update(self):
        self.event_handling()
        self.movement()

    # Player draw method
    def draw(self, surf):
        surf.blit(self.image, self.image_rect)

# Creating a NPC class
class NPC(pygame.sprite.Sprite):
    # Initialize the player class
    def __init__(self, x, y, face, lines):
        pygame.sprite.Sprite.__init__(self)

        self.face = face
        self.lines = lines

        self.image = player_list[0]
        self.image_original = self.image.copy()
        self.image_rect = self.image.get_rect()

        self.rect = self.image_rect.copy()
        self.rect.inflate_ip((-40,-40))
        self.rect.center = (x, y)

        self.talk_zone = pygame.Rect((0, 0, 110, 110))
        self.talk_zone.center = self.rect.center

    # Update the player class
    def update(self):
        # Reposition drawing rect & talk zone center
        self.image_rect.center = self.rect.center
        self.talk_zone.center = self.rect.center

    # Player draw method
    def draw(self, surf):
        surf.blit(self.image, self.image_rect)

# Create a wall class
class Wall(pygame.sprite.Sprite):
    # Initialize the wall class
    def __init__(self, x, y, w, h, color=black, image=None):
        pygame.sprite.Sprite.__init__(self)
        if image is None:
            self.image = pygame.Surface((w, h))
            self.image.fill(color)
        else:
            self.image = image

        self.rect = pygame.Rect((0, 0, w, h))
        self.rect.x = x
        self.rect.y = y

# Text box class
class Text_Box(pygame.sprite.Sprite):
    # Initialize the text box class
    def __init__(self, face, text):
        pygame.sprite.Sprite.__init__(self)

        self.face = face
        self.text = text

        self.image = pygame.Surface((610, 160))
        self.image.fill(white)
        pygame.draw.rect(self.image, black, (5, 5, 600, 150))
        if self.face is not None:
            self.image.blit(face, (5, 5))

        render_text(self.text, white, self.image, x=160, y=10, size="medium")

        self.rect = self.image.get_rect()
        self.rect.x = 95
        self.rect.y = 395
