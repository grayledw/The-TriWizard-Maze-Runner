import pygame

# pygame.init()
#
# running = True
#
# Cup_1 = pygame.image.load('triwizard cup.png')
#
#
# def draw_gryffindor_banner():
#     gryffindor_banner = pygame.image.load('gryffindor_banner_small.png')
#     g_banner_x = 20
#     g_banner_y = 20
#
#     frame.blit(gryffindor_banner, (g_banner_x, g_banner_y))
#
#
# def draw_slytherin_banner():
#     slytherin_banner = pygame.image.load('slytherin_banner_small.png')
#     s_banner_x = 20
#     s_banner_y = 20
#
#     frame.blit(slytherin_banner, (s_banner_x, s_banner_y))

class Cup:
    def __init__(self, frame, image):
        self.frame = frame
        frame_width, frame_height = pygame.display.get_surface().get_size()
        self.x = frame_width/2 - 10
        self.y = frame_height*0.47
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_self(self):
        self.frame.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(self.frame, pygame.Color("green"), self.rect, 5)


# c = Cup()
#
#
# def is_collided_with(Cup_1):
#     if player_1.is_collided_with(Cup_1):
#
#         draw_gryffindor_banner()
#
#         text_x = 750
#         text_y = 750
#         pygame.display.set_mode((text_x, text_y))
#         pygame.display.set_caption('Gryffindor Wins')
#         font = pygame.font.SysFont('Times New Roman', 50, False, False)
#         text = font.render('Gryffindor Wins!', True, yellow, red)
#         textRect = text.get_rect()
#         textRect.center = (text_x // 2, text_y // 2)
#
#         while running:
#             running = True
#             frame.fill(red)
#             frame.blit(text, textRect)
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#
#                 draw_gryffindor_banner()
#
#                 pygame.display.update()
#
#     if player_2.is_collided_with(Cup_1):
#
#         draw_slytherin_banner()
#
#         text_x = 750
#         text_y = 750
#         pygame.display.set_mode((text_x, text_y))
#         pygame.display.set_caption('Slytherin Wins')
#         font = pygame.font.SysFont('Times New Roman', 50, False, False)
#         text = font.render('Slytherin Wins!', True, grey, pygame.Color("green4"))
#         textRect = text.get_rect()
#         textRect.center = (text_x // 2, text_y // 2)
#
#         while running:
#             running = True
#             frame.fill(pygame.Color("green4"))
#             frame.blit(text, textRect)
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#
#                 draw_slytherin_banner()
#
#                 pygame.display.update()
#
#
# while running:
#     running = True
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         frame.fill(pygame.Color('white'))
#
#         tc.draw_self()
#
#         is_collided_with(Cup_1)
#
#         pygame.display.update()
