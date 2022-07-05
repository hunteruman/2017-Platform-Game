################################################################################
#                         T E R M   P R O J E C T                              #
#                             by: HUNTER UMAN                                  #
################################################################################

import pygame
import random 
import string

##################### Idea for level generation from: ##########################
################ http://stackoverflow.com/questions/14354171/ ##################
################### add-scrolling-to-a-platformer-in-pygame ####################

def getScreen(n):
    if n == 0:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "               a              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        " b                            E",
        "                              E",
        "                              E",
        "  Y                           E",
        "                              E",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 1 or n == 2:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "Y                             E",
        "                              E",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 3:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "Y                             E",
        "                              E",
        "PPPPPPPPPPPPPPPPPPP         PP",
        "PPPPPPPPPPPPPPPPPPP         PP",
        "PPPPPPPPPPPPPPPPPPP         PP",
        "PPPPPPPPPPPPPPPPPPP         PP",
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]
    elif n == 4:
        return [
        "   Y                          E",
        "  eee                         E",
        "  eee                         E",
        "  eee                         E",
        "  eee                         E",
        " eeeee                        E",
        " eeeee                        E",
        " eeeee                        E",
        " eeeee                        E",
        " eeeee                        E",
        "eeeeeee                       E",
        "eeeeeee                       E",
        "eeeeeee                       E",
        "eeeeeee                       E",
        "eeeeeee                       E",
        "eeeeeee                       E",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 5:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "Y                             E",
        "                              E",
        "PPPPPPPPPPPP    P    P    PPPP",
        "PPPPPPPPPPPP    P    P    PPPP",
        "PPPPPPPPPPPP    P    P    PPPP",
        "PPPPPPPPPPPP    P    P    PPPP",]
    elif n == 6:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "Y                             E",
        "                              E",
        "PPPPPPP    F    F    F    PPPP",
        "PPPPPPP                   PPPP",
        "PPPPPPP                   PPPP",
        "PPPPPPP                   PPPP",]
    elif n == 7:
        return [
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                          PPPP",
        "                          PPPP",
        "                   F      PPPP",
        "                          PPPP",
        "            F             PPPP",
        "Y                         PPPP",
        "                          PPPP",
        "PPPPPP                    PPPP",
        "PPPPPP                    PPPP",
        "PPPPPP                    PPPP",
        "PPPPPP                    PPPP",
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]
    elif n == 8:
        return [
        "   Y                          E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                      0       E",
        "                              E",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 9:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                     c        E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                     1        E",
        "Y                             E",
        "                              E",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 10:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "        F     F     F       PP",
        "Y                2          PP",
        "                            PP",
        "PPPP                      PPPP",
        "PPPP                      PPPP",
        "PPPP                      PPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 11:
        return [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "                    PPPPPPPPPP",
        "                          PPPP",
        "                           PPP",
        "                           PPP",
        "                            PP",
        "                            PP",
        "                            PP",
        "                            PP",
        "                            PP",
        "Y                           PP",
        "                  3          P",
        "PP                           P",
        "PP                            E",
        "PP                            E",
        "PPPP                        PP",
        "PPPP                        PP",
        "PPPP                        PP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 12:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                          PPPP",
        "                           PPP",
        "                       F   PPP",
        "                            PP",
        "                            PP",
        "                F       F    P",
        "          F                  P",
        "                              ",
        "                     F        ",
        "Y          F                  ",
        "                              ",
        "PP                            ",
        "PP      F                     ",
        "PP                            ",]
    elif n == 13:
        return [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "               2              E",
        "                              E",
        "Y                             E",
        "        F            F        E",
        "PPPP       P      P       PPPP",
        "PPPP       PPPPPPPP       PPPP",
        "PPPP       P  PP  P       PPPP",
        "PPPP       P  PP  P       PPPP",]
    elif n == 14:
        return [
        "E                             ",
        "E                             ",
        "PPP                           ",
        "PP F     F                    ",
        "PP             F      F       ",
        "P                           F ",
        "P                             ",
        "                              ",
        "                           F  ",
        "                              ",
        "                              ",
        "                            F ",
        "                              ",
        "                              ",
        "Y          F F F F F F F F F  ",
        "       F                      ",
        "PPP                           ",
        "PPP                           ",
        "PPP                           ",
        "PPP                           ",]
    elif n == 15:
        return [
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "         F     F     F     F  ",
        "            3                 ",
        "                              ",
        "      F                     F ",
        "                             Y",
        "         P         P          ",
        "         PPPPP PPPPP    F   PP",
        "         PPPPP PPPPP        PP",
        "         PPPPP PPPPP        PP",
        "          EEEEEEEEE           "]
    elif n == 16:
        return [
        "P  Y                         PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                    4       PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]
    elif n == 17:
        return [
        "P  Y                         PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                    5       PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "P                            PE",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPP PPPPPP",
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]
    elif n == 18:
        return [
        "E                       Y     ",
        "E                             ",
        "E                             ",
        "PPP                           ",
        "PP F                          ",
        "PP                            ",
        "P       F                     ",
        "P                             ",
        "             F                ",
        "                              ",
        "                  F           ",
        "                              ",
        "                       F      ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",]
    elif n == 19:
        return [
        "                              ",
        "                              ",
        "                              ",
        "                              E",
        "                              E",
        "                      F    PPP",
        "                            PP",
        "                            PP",
        "                     F       P",
        "          F                  P",
        "                              ",
        "     F        F     F         ",
        "                              ",
        "                              ",
        "    F         F               ",
        "                             Y",
        "                   F          ",
        "     F     F                PP",
        "                            PP",
        "                       P    PP",]
    elif n == 20:
        return [
        "                              ",
        "                              ",
        "                              ",
        "                              E",
        "Y                             E",
        "                              E",
        "PP   F    F    F    F    F   PP",
        "P                            P",
        "P                            P",
        "P                            P",
        "P                            P",
        "                              ",
        "PPP PPPPPP PPPPPPPP PPPP PPPPP",
        "P  3   P      PP 3    P      P",
        "P      P  3   PP      P   3  P",
        "P      P      PP      P      P",
        "P      P      PP      P      P",
        "P      P      PP      P      P",
        "P      P      PP      P      P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 21:
        return [
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "                 2      2     E",
        "                              E",
        "                              E",
        "                              E",
        "                              E",
        "Y                             E",
        "                              E",
        "PPP    F    PPP    PPP    PPPPE",
        "PP           P      P      PPPE",
        "PP                         PPPE",
        "P                           PPE"]
    elif n == 22:
        return [
        "PPPPPPPPPPPPPPPPPPPPeeeeeeeeeeE",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPeeeE",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPeE",
        "               eeeeeeeeeeeeeeeE",
        "        eeeeeeeeeee         eeE",
        "  eeeeeeeeeeee           ee eeE",
        "eeeeeeeee              ee   eeE",
        "eeee                eee    eeeE",
        "                  eee     eeeeE",
        "               eeee      eeeeeE",
        "             eeee       eePPPPE",
        "           eeee        ePPPPPPE",
        "        eeeee   PPPP1  PPPPPPPE",
        "      eeee PPPPPPPPP   PPPPPPPE",
        "Y  eeeeePPPPPPPPPPPP   PPPPPPPE",
        " eeeeePPPPPPPPPPPPPPPPPPPPPPPPE",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPE",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPE",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPE",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    elif n == 23:
        return [
        "                              ",
        "                              ",
        "                              ",
        "                d             ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "Y                             ",
        "                              ",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]

def buildLevel(game):
    game.screen = getScreen(game.level)
    game.blocks = []
    game.fallys = []
    game.pewys = []
    i = j = 0
    l = m = None
    for row in game.screen:
        n = 0
        for col in row:
            n += 1
            if col in string.ascii_lowercase:
                image = getImage(col)
                (a,b,width,height) =  image.get_rect()
                rect = pygame.Rect(i,j,width,height)
                a = Image(image, rect)
                game.gameObjects.add(a)
            if col == 'P':
                p = Block(i, j, game)
                game.blocks.append(p)
                game.gameObjects.add(p)
                game.blockos.add(p)
            if col == 'E':
                if n == 1:
                    i -= 20
                e = ExitBlock(i, j, game)
                game.blocks.append(e)
                game.gameObjects.add(e)
                game.blockos.add(e)
            if col == 'F':
                f = FallyBlock(i, j, game)
                game.fallys.append(f)
                game.gameObjects.add(f)
                game.fallyBlocks.add(f)
                game.blockos.add(f)
            if col == 'Y':
                l,m = i,j
            if (col == '0' or col == '1' or col == '2' or col == '3' or col == 
                    '4' or col == '5'):
                b = Baddy(i,j,int(col))
                game.gameObjects.add(b)
                game.baddys.add(b)
                game.blockos.add(b)
            i += 20
        j += 20
        i = 0
    if l != None:
        if m == 0:
            game.player = Player(l,m,0,8)
        else:
            game.player = Player(l,m)
        game.gameObjects.add(game.player)
    game.newLevel = False

def getImage(alpha):
    if alpha == 'a':
        image = pygame.image.load('images/gonLOGO.png').convert_alpha()
        return pygame.transform.scale(image, (216, 98))
    elif alpha == 'b':
        image =  pygame.image.load('images/moveDesign.png').convert_alpha()
        return pygame.transform.scale(image, (53, 53))
    elif alpha == 'c':
        image =  pygame.image.load('images/spaceDesign.png').convert_alpha()
        return pygame.transform.scale(image, (60, 60))
    elif alpha == 'd':
        image =  pygame.image.load('images/finalScreen.png').convert_alpha()
        return pygame.transform.scale(image, (200,200))
    elif alpha == 'e':
        image = pygame.Surface((20, 20))
        image.fill(Colour.white)
        return image
    elif alpha == 'f':
        pass
    elif alpha == 'g':
        pass
    elif alpha == 'h':
        pass
    elif alpha == 'i':
        pass
    elif alpha == 'j':
        pass  
    elif alpha == 'k':
        pass
    elif alpha == 'l':
        pass
    elif alpha == 'm':
        pass

class Colour(object):
    white = (225,225,225)
    darkGray = (75,75,75)
    lightGray = (175,175,175)
    red = (200,75,75)

class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Image(GameObject):
    def __init__(self, image, rect):
        GameObject.__init__(self)
        self.image = image
        self.rect = rect

class Player(GameObject):
    def __init__(self, x, y, xspeed = 0, yspeed = 0):
        GameObject.__init__(self)
        self.x = x
        self.y = y

        self.right = self.left = self.up = False

        self.xspeed = xspeed
        self.yspeed = yspeed

        self.width = 13
        self.height = 36

        self.dead = False
        self.onBlock = False
        self.grav = True

        self.image = pygame.image.load('images/basicPlayer.png').convert_alpha()
        (a,b,width,height) =  self.image.get_rect()
        self.rect = pygame.Rect(x,y,width,height)

    def update(self, game, blocks, pewys, fallys, baddys):
        if self.left:
            self.xspeed = -4
        if self.right:
            self.xspeed = 4
        if not self.left and not self.right:
            self.xspeed = 0
        if self.up and self.onBlock:
            self.yspeed = -8
        if not self.onBlock:
            self.yspeed += 0.5
            if self.yspeed > 8:
                self.yspeed = 8
        if ((self.rect.left > game.width) or 
                (self.rect.top > game.height or self.rect.bottom < -50)):
            self.dead = True
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.left += self.xspeed
        self.collide(self.xspeed, 0, game, blocks, pewys, fallys, baddys)
        self.rect.top += self.yspeed
        self.onBlock = False
        self.collide(0, self.yspeed, game, blocks, pewys, fallys, baddys)

        #if (self.succ.dick.xspeed, 0, penis, balls, daddy, cummies):
        #    self.cry.left < 4

    def collide(self, xspeed, yspeed, game, blocks, pewys, fallys, baddys):
        for block in blocks:
            if pygame.sprite.collide_rect(self, block):
                if isinstance(block, ExitBlock):
                    game.level += 1
                    game.newLevel = True
                if xspeed > 0:
                    self.rect.right = block.rect.left
                if xspeed < 0:
                    self.rect.left = block.rect.right
                if yspeed > 0:
                    self.rect.bottom = block.rect.top
                    self.onBlock = True
                    self.yspeed = 0
                if yspeed < 0:
                    self.rect.top = block.rect.bottom
        for fally in fallys:
            if pygame.sprite.collide_rect(self, fally):
                if xspeed > 0:
                    self.rect.right = fally.rect.left
                if xspeed < 0:
                    self.rect.left = fally.rect.right
                if yspeed > 0:
                    self.rect.bottom = fally.rect.top
                    self.onBlock = True
                    fally.falling = True
                    self.yspeed = fally.fallSpeed
                if yspeed < 0:
                    self.rect.top = fally.rect.bottom
        for pew in pewys:
            if isinstance(pew, badPew):
                if pygame.sprite.collide_rect(self, pew):
                    self.dead = True
        if pygame.sprite.spritecollideany(self, baddys) != None:
            self.dead = True

class Baddy(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        if n == 0:
            self.image = pygame.image.load('images/baddy0temp.png'
                ).convert_alpha()
        elif n == 1:
            self.image = pygame.image.load('images/baddy1temp.png'
                ).convert_alpha()
        elif n == 2:
            self.image = pygame.image.load('images/baddy2temp.png'
                ).convert_alpha()
        elif n == 3:
            self.image = pygame.image.load('images/baddy3temp.png'
                ).convert_alpha()
        elif n == 4:
            self.image = pygame.image.load('images/baddy4temp.png'
                ).convert_alpha()
        elif n == 5:
            self.image = pygame.image.load('images/baddy5temp.png'
                ).convert_alpha()
        (a,b,width,height) =  self.image.get_rect()

        self.rect = pygame.Rect(x,y,width,height)
        self.n = n
        self.health = 20*n

        self.act = -1

        self.xspeed = 0  
        self.yspeed = 0
        
        self.onBlock = False
        self.dead = False
        self.right = self.left = self.up = False

    def update(self, game, blocks, pewys, fallys):
        self.act = (self.act+1)%100

        if self.n == 5:
            if self.act%50 ==0:
                p = badPew(self.rect.left-50,(self.rect.top+self.rect.bottom)/2,
                            game)
                game.pewys.append(p)
                game.gameObjects.add(p)
                game.pews.add(p)
                p = badPew(self.rect.left-50,(self.rect.top+self.rect.bottom)/2,
                            game)
                game.pewys.append(p)
                game.gameObjects.add(p)
                game.pews.add(p)
        elif self.n == 4:
            if self.act%30 ==0:
                p = badPew(self.rect.left-50,(self.rect.top+self.rect.bottom)/2,
                            game)
                game.pewys.append(p)
                game.gameObjects.add(p)
                game.pews.add(p)
        elif self.n == 3:
            if self.act == 0:
                self.right = False
                self.left = True
                self.up = True
            if self.act == 50:
                self.up = True
                self.left = False
                self.right = True
        elif self.n == 2:
            self.up = False
            if self.act == 0:
                self.right = False
                self.left = True
            if self.act == 50:
                self.left = False
                self.right = True

        if self.left:
            self.xspeed = -3
        if self.right:
            self.xspeed = 3
        if not self.left and not self.right:
            self.xspeed = 0
        if self.up and self.onBlock:
            self.yspeed = -12
        if not self.onBlock:
            self.yspeed += 0.5
            if self.yspeed > 12:
                self.yspeed = 12
        if ((self.rect.left > game.width) or 
                (self.rect.top > game.height or self.rect.bottom < -50)):
            self.dead = True
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.left += self.xspeed
        self.collide(self.xspeed, 0, game, blocks, pewys, fallys)
        self.rect.top += self.yspeed
        self.onBlock = False
        self.collide(0, self.yspeed, game, blocks, pewys, fallys)

    def collide(self, xspeed, yspeed, game, blocks, pewys, fallys):
        for block in blocks:
            if pygame.sprite.collide_rect(self, block):
                if xspeed > 0:
                    self.rect.right = block.rect.left
                if xspeed < 0:
                    self.rect.left = block.rect.right
                if yspeed > 0:
                    self.rect.bottom = block.rect.top
                    self.onBlock = True
                    self.yspeed = 0
                if yspeed < 0:
                    self.rect.top = block.rect.bottom
        for fally in fallys:
            if pygame.sprite.collide_rect(self, fally):
                if xspeed > 0:
                    self.rect.right = fally.rect.left
                if xspeed < 0:
                    self.rect.left = fally.rect.right
                if yspeed > 0:
                    self.rect.bottom = fally.rect.top
                    self.onBlock = True
                    fally.falling = True
                    self.yspeed = fally.fallSpeed
                if yspeed < 0:
                    self.rect.top = fally.rect.bottom
        for pew in pewys:
            if pygame.sprite.collide_rect(self, pew):
                if not isinstance(pew, badPew):
                    self.health -= 1
                    if self.health < 0 and self.n > 0:
                        l,t,n = self.rect.left, self.rect.top, self.n-1
                        game.gameObjects.remove(self)
                        game.blockos.remove(self)
                        game.baddys.remove(self)
                        b = Baddy(l,t,n)
                        game.gameObjects.add(b)
                        game.baddys.add(b)
                        game.blockos.add(b)
                    else:
                        pass                    

class Block(GameObject):
    def __init__(self, x, y, game):
        GameObject.__init__(self)
        self.image = pygame.Surface((20, 20))
        if (game.level >= 0 and game.level <4) or game.level > 22:
            self.image.fill(Colour.darkGray)
        else:
            self.image.fill(Colour.lightGray)
        self.rect = pygame.Rect(x, y, 20, 20)

class ExitBlock(Block):
    def __init__(self, x, y, game):
        Block.__init__(self, x, y, game)
        #self.image.fill(Colour.darkGray)

class FallyBlock(Block):
    def __init__(self, x, y, game):
        Block.__init__(self, x, y, game)
        if (game.level >= 0 and game.level <4) or game.level > 22:
            self.image.fill(Colour.darkGray)
        else:
            self.image.fill(Colour.lightGray)
        self.fallSpeed = 2
        self.falling = False

    def update(self, game, blocks):
        if self.falling:
            self.rect.bottom += self.fallSpeed
        if self.rect.bottom >= game.height:
            del self

class Pew(Block):
    def __init__(self, x, y, game):
        Block.__init__(self, x, y, game)
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colour.red)
        self.shootSpeed = 10 

    def update(self, game, blocks, fallys):
        self.rect.left += self.shootSpeed
        if self.rect.left >= game.width: 
            self.kill()

class badPew(Pew):
    def __init__(self, x, y, game):
        Block.__init__(self, x, y, game)
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colour.red)
        self.shootSpeed = -6 
        self.yoff = random.randint(-4,4)

    def update(self, game, blocks, fallys):
        self.rect.left += self.shootSpeed
        self.rect.top += self.yoff
        if self.rect.left >= game.width: 
            self.kill()


################# The following pygame structure is from: ######################
#### https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py ####

'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15
use this code in your term project if you want
- CITE IT
- you can modify it to your liking
  - BUT STILL CITE IT
- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''

class Game(object):

    def init(self):
        self.gameObjects = pygame.sprite.Group()
        self.fallyBlocks = pygame.sprite.Group()
        self.blockos = pygame.sprite.Group()
        self.pews = pygame.sprite.Group()
        self.baddys = pygame.sprite.Group()
        self.level = 0
        buildLevel(self)

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_UP:
            self.player.up = True
        if keyCode == pygame.K_LEFT:
            self.player.left = True
        if keyCode == pygame.K_RIGHT:
            self.player.right = True
        #if keyCode == pygame.K_n:
        #    self.level = (self.level + 1)%24
        #    self.newLevel = True
        #if keyCode == pygame.K_r:
        #    self.init()
        if keyCode == pygame.K_SPACE:
            p = Pew(self.player.rect.right, self.player.rect.top, self)
            self.pewys.append(p)
            self.gameObjects.add(p)
            self.pews.add(p)

    def keyReleased(self, keyCode, modifier):
        if keyCode == pygame.K_UP:
            self.player.up = False
        if keyCode == pygame.K_LEFT:
            self.player.left = False
        if keyCode == pygame.K_RIGHT:
            self.player.right = False

    def timerFired(self, dt):
        self.player.update(self, self.blocks, self.pewys, self.fallys, 
            self.baddys)
        self.fallyBlocks.update(self, self.fallys)
        self.pews.update(self, self.blocks, self.fallys)
        self.baddys.update(self, self.blocks, self.pewys, self.fallys)
        l = []
        for i in range(len(self.pewys)):
            if str(self.pewys[i]) == '<Pew sprite(in 0 groups)>':
                l = [i] + l
        for i in l:
            self.pewys.pop(i)


    def redrawAll(self, screen):
        self.gameObjects.draw(screen)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def loadNextLevel(self):
        #progresses to the next screen
        if (self.level >= 0 and self.level <4) or self.level > 22:
            self.bgColor = Colour.white
        else:
            self.bgColor = Colour.darkGray
        self.gameObjects.empty()
        self.fallyBlocks.empty()
        self.baddys.empty()
        buildLevel(self)

    def __init__(self, width=600, height=400, fps=50, title="gon"):
        self.width = width
        self.height = height
       
        self.fps = fps
        self.title = title
        self.bgColor = Colour.white
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()
        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            if self.newLevel:
                self.loadNextLevel()
            if self.player.dead:
                self.loadNextLevel()
            screen.fill(self.bgColor)
            self.timerFired(time)
            self.redrawAll(screen)
            pygame.sprite.groupcollide(self.pews, self.baddys, True, False)
            pygame.display.flip()

        pygame.quit()


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()