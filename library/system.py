import pygame
from library.rollinggirl import RollingGirl

def lerp(a, b, t):
    return a * (1 - t) + b * t

def clamp(minValue, maxValue, value):
    value = min(value, maxValue)
    value = max(value, minValue)
    return value

class System:
    width = None
    height = None
    prevMouse = (0, 0)
    def __init__(self, screenWidth : int, screenHeight : int, fps : int):
        self.width = screenWidth
        self.height = screenHeight
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = fps

    def beginProcess(self):
        self.setup()
        while self._loopStep():
            pass

    # Pseudo_private Function (aka. stuff that should not be accessed outside the class. You can, doesn't mean you should)

    def _loopStep(self):
        delta = self.clock.tick(self.fps) / 1000
        returnCode = self.loop(delta)
        pygame.display.flip()
        return returnCode # True = program still running, False = program stopped

    # Control Code

    def setup(self):
        self.miku = RollingGirl()
        self.miku.setCoordinate(self.width // 2, self.height // 2)
        # self.miku.setCoordinate(0, 0)

        self.music = pygame.mixer.Sound("./sound/Rolling Girl.mp3")
        self.music.set_volume(0)
        self.music.play()

    def loop(self, delta):
        # Input control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        currMouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed(num_buttons = 3)[0]:
            self.miku.spin(self.prevMouse[0], self.prevMouse[1], currMouse[0], currMouse[1], delta)
        
        # Logic:
        self.miku.update(delta)
        threshold = 1000
        limit = 1000
        if abs(self.miku.angularSpeed) >= threshold:
            self.music.set_volume(lerp(0, 1, (clamp(0, limit, abs(self.miku.angularSpeed) - threshold) / limit)))
        else:
            self.music.set_volume(0)

        # Draw function:
        self.screen.fill((255, 255, 255))
        self.miku.draw(self.screen)

        # Final return:
        self.prevMouse = currMouse
        return True