from WizardCup import *
from PlayerClass import *
from Spell import *
from pygame.locals import *
import time


class Game:
    def __init__(self, width, height, player1_image, player2_image, spell_image, wizard_cup_image):
        self.width = width
        self.height = height
        self.frame = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('The TriWizard Maze Run')
        self.frame.fill(pygame.Color('tan'))
        self.cup = Cup(self.frame, wizard_cup_image)

        self.turn_player_one_right = False
        self.turn_player_one_left = False
        self.turn_player_one_forwards = False
        self.turn_player_one_backwards = False

        self.turn_player_two_right = False
        self.turn_player_two_left = False
        self.turn_player_two_forwards = False
        self.turn_player_two_backwards = False

        self.player_one_spells = []
        self.player_two_spells = []

        self.wall_rects = [pygame.Rect(200, 100, 225, 45), pygame.Rect(200, 700, 225, 45), pygame.Rect(1100, 100, 200, 45),
                           pygame.Rect(1100, 700, 200, 45), pygame.Rect(200, 100, 45, 225), pygame.Rect(200, 500, 45, 200),
                           pygame.Rect(1300, 100, 45, 245), pygame.Rect(1300, 500, 45, 245), pygame.Rect(750, 525, 45, 200),
                           pygame.Rect(550, 300, 45, 200), pygame.Rect(950, 300, 45, 200), pygame.Rect(750, 100, 45, 200)]

        self.clock = pygame.time.Clock()

        self.player1_wizard_image = player1_image
        self.player2_wizard_image = player2_image
        self.spell_image = spell_image
        self.wizard_cup_image = wizard_cup_image
        self.player_one = Player(self.player1_wizard_image, self.frame, 50, 700)
        self.player_two = Player(self.player2_wizard_image, self.frame, 1450, 100)

    def run_game(self):
        running = True
        start_time = time.time()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_d:
                        self.turn_player_one_right = True
                    elif event.key == K_a:
                        self.turn_player_one_left = True
                    elif event.key == K_w:
                        self.turn_player_one_forwards = True
                    elif event.key == K_s:
                        self.turn_player_one_backwards = True
                    elif event.key == K_RIGHT:
                        self.turn_player_two_right = True
                    elif event.key == K_LEFT:
                        self.turn_player_two_left = True
                    elif event.key == K_UP:
                        self.turn_player_two_forwards = True
                    elif event.key == K_DOWN:
                        self.turn_player_two_backwards = True
                    elif event.key == K_SPACE:
                        dx, dy = self.player_one.get_x_and_y_movement_increments()
                        self.player_one_spells.append(Spell(dx, dy, int(self.player_one.x), int(self.player_one.y), self.spell_image, self.frame))
                    elif event.key == K_SLASH:
                        dx, dy = self.player_two.get_x_and_y_movement_increments()
                        self.player_two_spells.append(Spell(dx, dy, int(self.player_two.x), int(self.player_two.y), self.spell_image, self.frame))

                elif event.type == pygame.KEYUP:
                    if event.key == K_d:
                        self.turn_player_one_right = False
                    elif event.key == K_a:
                        self.turn_player_one_left = False
                    elif event.key == K_w:
                        self.turn_player_one_forwards = False
                    elif event.key == K_s:
                        self.turn_player_one_backwards = False
                    elif event.key == K_RIGHT:
                        self.turn_player_two_right = False
                    elif event.key == K_LEFT:
                        self.turn_player_two_left = False
                    elif event.key == K_UP:
                        self.turn_player_two_forwards = False
                    elif event.key == K_DOWN:
                        self.turn_player_two_backwards = False

            self.frame.fill(pygame.Color('tan'))

            if self.turn_player_one_right:
                self.player_one.turn_right()
            if self.turn_player_one_left:
                self.player_one.turn_left()
            if self.turn_player_one_forwards:
                self.player_one.forwards(self.wall_rects)
            if self.turn_player_one_backwards:
                self.player_one.backwards(self.wall_rects)
            if self.turn_player_two_right:
                self.player_two.turn_right()
            if self.turn_player_two_left:
                self.player_two.turn_left()
            if self.turn_player_two_forwards:
                self.player_two.forwards(self.wall_rects)
            if self.turn_player_two_backwards:
                self.player_two.backwards(self.wall_rects)

            for spell in self.player_one_spells:
                spell.move()
            for spell in self.player_two_spells:
                spell.move()

            for spell in self.player_one_spells:
                collides_with_player_two = self.player_two.rect.colliderect(spell.rectangle)
                if collides_with_player_two:
                    self.player_two.change_health()
                    self.player_one_spells.remove(spell)
                if not collides_with_player_two:
                    spell.draw()
                if self.player_two.health <= 0:
                    self.frame.fill(pygame.Color("red"))

                    self.draw_gryffindor_banner()

                    pygame.display.set_caption('Gryffindor Wins')
                    font = pygame.font.SysFont('Times New Roman', 50, False, False)
                    text = font.render('Gryffindor Wins!', True, pygame.Color("yellow"), pygame.Color("red"))
                    textRect = text.get_rect()
                    textRect.center = (self.frame.get_width() // 2, self.frame.get_height() // 2)

                    self.frame.blit(text, textRect)

                    pygame.display.update()

                    time.sleep(5)

                    running = False

            for spell in self.player_two_spells:
                collides_with_player_one = self.player_one.rect.colliderect(spell.rectangle)
                if collides_with_player_one:
                    self.player_one.change_health()
                    self.player_two_spells.remove(spell)
                if not collides_with_player_one:
                    spell.draw()
                if self.player_one.health <= 0:
                    self.frame.fill(pygame.Color("green4"))

                    self.draw_slytherin_banner()

                    # pygame.display.set_caption('Slytherin Wins')
                    font = pygame.font.SysFont('Times New Roman', 50, False, False)
                    text = font.render('Slytherin Wins!', True, pygame.Color("grey"), pygame.Color("green4"))
                    textRect = text.get_rect()
                    textRect.center = (self.frame.get_width() // 2, self.frame.get_height() // 2)

                    self.frame.blit(text, textRect)

                    pygame.display.update()

                    time.sleep(5)

                    running = False

            for wall_rect in self.wall_rects:
                for spell in self.player_one_spells:
                    if spell.rectangle.colliderect(wall_rect):
                        self.player_one_spells.remove(spell)

                for spell in self.player_two_spells:
                    if spell.rectangle.colliderect(wall_rect):
                        self.player_two_spells.remove(spell)

            self.maze_grid()

            for spell in self.player_one_spells:
                spell.draw()
            for spell in self.player_two_spells:
                spell.draw()

            self.player_one.draw()
            self.player_two.draw()

            time_since_start = time.time() - start_time
            # show the cup after 10 seconds
            if time_since_start > 30:
                self.cup.draw_self()
                if self.cup.rect.collidepoint(self.player_one.x, self.player_one.y):
                    self.frame.fill(pygame.Color("red"))

                    self.draw_gryffindor_banner()

                    pygame.display.set_caption('Gryffindor Wins')
                    font = pygame.font.SysFont('Times New Roman', 50, False, False)
                    text = font.render('Gryffindor Wins!', True, pygame.Color("yellow"), pygame.Color("red"))
                    textRect = text.get_rect()
                    textRect.center = (self.frame.get_width() // 2, self.frame.get_height() // 2)

                    self.frame.blit(text, textRect)

                    pygame.display.update()
                    time.sleep(5)
                    running = False

                if self.cup.rect.collidepoint(self.player_two.x, self.player_two.y):
                    self.frame.fill(pygame.Color("green4"))

                    self.draw_slytherin_banner()

                    pygame.display.set_caption('Slytherin Wins')
                    font = pygame.font.SysFont('Times New Roman', 50, False, False)
                    text = font.render('Slytherin Wins!', True, pygame.Color("grey"), pygame.Color("green4"))
                    textRect = text.get_rect()
                    textRect.center = (self.frame.get_width() // 2, self.frame.get_height() // 2)

                    self.frame.blit(text, textRect)
                    pygame.display.update()
                    time.sleep(5)
                    running = False

            self.clock.tick(60)
            pygame.display.update()

    def maze_grid(self):
        self.frame.fill(pygame.Color('tan'))

        for wall_rect in self.wall_rects:
            pygame.draw.rect(self.frame, pygame.Color('dark green'), wall_rect)
            #pygame.draw.rect(self.frame, pygame.Color("green"), wall_rect, 5)

    def draw_gryffindor_banner(self):
        gryffindor_banner = pygame.image.load('gryffindor_banner_small.png')
        g_banner_x = 20
        g_banner_y = 20

        self.frame.blit(gryffindor_banner, (g_banner_x, g_banner_y))

    def draw_slytherin_banner(self):
        slytherin_banner = pygame.image.load('slytherin_banner_small.png')
        s_banner_x = 20
        s_banner_y = 20

        self.frame.blit(slytherin_banner, (s_banner_x, s_banner_y))


def main():
    pygame.init()

    width = 1500
    height = 800
    wizard_cup_image = pygame.image.load('triwizard cup.png')
    player1_wizard_image = pygame.transform.scale(pygame.image.load('Player1.png'), (int(width * .0233333), int(height * .09)))
    player2_wizard_image = pygame.transform.scale(pygame.image.load('Player2.png'), (int(width * .0233333), int(height * .09)))
    spell_image = pygame.transform.scale(pygame.image.load('Spell.png'), (int(width * .01555), int(height * .025565)))

    game = Game(width, height, player1_wizard_image, player2_wizard_image, spell_image, wizard_cup_image)
    game.run_game()


game_rules = input('Control Player 1(Gryffindor) using the "W" & S keys to go forward and backward\n'
                    ' and the "A" & "D" keys to turn left and right. Use the Q key to shoot a spell. \n'
                    ' Control PLayer 2 (Slytherin) using the up and down arrow keys to go forward and backward\n'
                    ' and the left and right arrow keys to turn left and right. Use the / key\n'
                    ' The objective of the game is to either get the Triwizard Cup at the top of the maze,\n'
                    ' or defeat the other player in a spell fight.\n'
                    ' Click ENTER to begin.\n')
if game_rules == '':
    main()





'''''
        pygame.draw.rect(self.frame, pygame.Color('dark green'), (50, 50, 600, 700), 5)
        s_bottom_left = pygame.Surface((300, 300))
        s_bottom_left.fill(pygame.Color('tan'))
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (0, 250), (50, 250), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (0, 250), (50, 250), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (100, 250), (300, 250), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (0, 200), (100, 200), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (100, 250), (100, 300), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (150, 200), (250, 200), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (50, 150), (50, 50), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (0, 0), (150, 0), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (150, 0), (150, 100), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (50, 150), (50, 150), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (50, 50), (100, 50), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (150, 200), (150, 150), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (200, 150), (200, 50), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (100, 100), (150, 100), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (200, 50), (300, 50), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (250, 100), (250, 200), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (300, 50), (300, 200), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (50, 150), (150, 150), 5)
        pygame.draw.line(s_bottom_left, pygame.Color('dark green'), (250, 0), (300, 0), 5)
        self.frame.blit(s_bottom_left, (50, 450))
        s_bottom_right = pygame.transform.flip(s_bottom_left.copy(), True, False)
        self.frame.blit(s_bottom_right, (350, 450))

        s_top_left = pygame.Surface((250, 200))
        s_top_left.fill(pygame.Color('tan'))
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (50, 50), (100, 50), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (50, 100), (50, 200), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (50, 200), (150, 200), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (250, 0), (250, 50), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (200, 50), (200, 100), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (200, 100), (250, 100), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (250, 150), (250, 200), 5)
        pygame.draw.line(s_top_left, pygame.Color('dark green'), (150, 100), (150, 150), 5)
        self.frame.blit(s_top_left, (50, 50))
        s_top_right = pygame.transform.flip(s_top_left.copy(), True, False)
        self.frame.blit(s_top_right, (400, 50))

        s_middle_left = pygame.Surface((300, 200))
        s_middle_left.fill(pygame.Color('tan'))
        pygame.draw.line(s_middle_left, pygame.Color('dark green'), (50, 50), (50, 150), 5)
        pygame.draw.line(s_middle_left, pygame.Color('dark green'), (50, 150), (200, 150), 5)
        pygame.draw.line(s_middle_left, pygame.Color('dark green'), (100, 50), (200, 50), 5)
        pygame.draw.line(s_middle_left, pygame.Color('dark green'), (100, 100), (250, 100), 5)
        pygame.draw.line(s_middle_left, pygame.Color('dark green'), (250, 100), (250, 150), 5)
        pygame.draw.line(s_middle_left, pygame.Color('dark green'), (250, 50), (300, 50), 5)
        self.frame.blit(s_middle_left, (50, 250))
        s_middle_right = pygame.transform.flip(s_middle_left.copy(), True, True)
        self.frame.blit(s_middle_right, (350, 250))
        '''''
