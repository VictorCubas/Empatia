import pygame
#import game_constants

TEXT_COLOR = (255, 255, 255)

def get_hud(game, player, messages):
    hud = pygame.Surface((800, 100))
    name_bar = pygame.Surface((800, 130))
    
    # Add items to hud
    hud.blit(get_killbar(player.kills), (0, 0))
    hud.blit(get_healthbar(player.health / player.max_health), (100, 0))
    hud.blit(get_message_box(messages), (600, 0))
    hud.blit(get_weapon(str(player.current_weapon)), (400, 0))

    # Add name bar    
    small_font = pygame.font.Font('resources/font/steelfish bd.otf', 30)
    name_text = small_font.render(player.name, True, (255,255,255))
    name_bar.blit(name_text, (10, -3))
    
    name_bar.blit(hud, (0, 30))
    pygame.draw.line(name_bar, (0,255,0), (0,30), (800, 30))
    pygame.draw.line(name_bar, (0,255,0), (0,0), (800, 0))
    return name_bar
    
def get_healthbar(health_percentage):
    width = 200
    height = 100
    small_font = pygame.font.Font('resources/font/steelfish bd.otf', 30)
    
    
    healthbar = pygame.Surface((width, height))
    healthbar.fill((0,0,0))
    
    color = (min(255, int(255*(1 - health_percentage))), 
             max(int(255 * health_percentage), 0), 0)
             
    health_text = small_font.render("health", True, (255,255,255))
    pygame.draw.rect(healthbar, color, pygame.Rect(0,height * .5, health_percentage * width, height * .5))
    healthbar.blit(health_text, ((width - health_text.get_rect().width) / 2, 10))
    stroke(healthbar, color)
    return healthbar
    
def get_message_box(messages):
    width = 400
    height = 100
    messages = list(messages)
    messages.reverse()
    message_font = pygame.font.Font('resources/font/steelfish bd.otf', 30)
    message_box = pygame.Surface((width, height))
    for index, message in enumerate(messages):
        message_text = message_font.render(message, True, TEXT_COLOR)
        message_box.blit(message_text, (10, index * message_text.get_rect().height))
    stroke(message_box, (0, 255, 0))
    return message_box
    
def get_killbar(kills):
    width = 100
    height = 100
    small_font = pygame.font.Font('resources/font/steelfish bd.otf', 30)
    big_font = pygame.font.Font('resources/font/steelfish bd.otf', 60)
    kill_text = small_font.render("kills", True, (255,255,255))
    kill_count = big_font.render(str(kills), True, (255,255,255))
    killbar = pygame.Surface((width, height))
    killbar.blit(kill_text, ((width - kill_text.get_rect().width) / 2, 3))
    killbar.blit(kill_count, ((width - kill_count.get_rect().width) / 2, 24)) 
    stroke(killbar, (0,255,0))
    return killbar
    
def get_weapon(weapon_number):
    width = 100
    height = 100
    weapon = pygame.Surface((width, height))
    if game_constants.WEAPONS[weapon_number] == 'light':
        img = pygame.image.load('resources/images/caltrops_big.gif').convert_alpha()
    elif game_constants.WEAPONS[weapon_number] == 'normal':
        img = pygame.image.load('resources/images/star_big.gif').convert_alpha()
    else:
        img = pygame.image.load('resources/images/ball_big.gif').convert_alpha()
    weapon.blit(img, (0, 0))  
    return weapon
    
def stroke(surface, color, width = 1):
    width = surface.get_rect().width
    height = surface.get_rect().height
    pygame.draw.line(surface, color, (0, 0), (width - 1, 0))
    pygame.draw.line(surface, color, (width - 1, 0), (width - 1, height - 1))
    pygame.draw.line(surface, color, (0, height - 1), (width - 1, height - 1))
    pygame.draw.line(surface, color, (0, 0), (0, height - 1))
    
