from imagesearch import *
from state import State
import keyboard
import random

class Main:
    def determine_current_state(self):
        try:
            im = region_grabber((0, 0, 1920, 1080))
            
            a = imagesearcharea("play.png", 0, 0, 1920, 1080, 0.95, im)
            b = imagesearcharea("confirm.png", 0, 0, 1920, 1080, 0.95, im)
            c = imagesearcharea("findmatch.png", 0, 0, 1920, 1080, 0.95, im)
            d = imagesearcharea("accept.png", 0, 0, 1920, 1080, 0.95, im)
            i = imagesearcharea("findingmatch.png", 0, 0, 1920, 1080, 0.95, im)
            g = imagesearcharea("currently_in_tft_game.png", 0, 0, 1920, 1080, 0.8, im)
            j = imagesearcharea("35.png", 0, 0, 1920, 1080, 0.99, im)
            p = imagesearcharea("36.png", 0, 0, 1920, 1080, 0.99, im)
            k = imagesearcharea("surr1.png", 0, 0, 1920, 1080, 0.8, im)
            l = imagesearcharea("surr2.png", 0, 0, 1920, 1080, 0.8, im)
            o = imagesearcharea("exitnow.png", 0, 0, 1920, 1080, 0.8, im)

            h = imagesearcharea("continue.png", 0, 0, 1920, 1080, 0.95, im)
            m = imagesearcharea("playagain.png", 0, 0, 1920, 1080, 0.8, im)
            n = imagesearcharea("ok.png", 0, 0, 1920, 1080, 0.8, im)

            #e = imagesearcharea("champion.png", 0, 0, 1920, 1080, 0.95, im)
            #f = imagesearcharea("lockin.png", 0, 0, 1920, 1080, 0.95, im)
            #g = imagesearcharea("nexus.png", 0, 0, 1920, 1080, 0.8, im)
            #k = imagesearcharea("honorscreen.png", 0, 0, 1920, 1080, 0.8, im)
            #p = imagesearcharea("shop.png", 0, 0, 1920, 1080, 0.8, im)
            #q = imagesearcharea("doran.png", 0, 0, 1920, 1080, 0.95, im)
            #s = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8, im)
            #t = imagesearcharea("lockscreen.png", 0, 0, 1920, 1080, 0.95, im)

            if o[0] != -1:
                return State.EXIT, o
            elif l[0] != -1:
                return State.SURRENDER_2, l
            elif k[0] != -1:
                return State.SURRENDER_1, k
            elif j[0] != -1:
                return State.OPTIONS, j
            elif p[0] != -1:
                return State.OPTIONS, p
            elif g[0] != -1:
                return State.MOVE_AROUND_MODE, g
            elif n[0] != -1:
                return State.OK, n
            elif b[0] != -1:
                return State.GAME_TYPE_SELECT, b
            elif c[0] != -1:
                return State.LOBBY, c
            elif d[0] != -1:
                return State.ACCEPT_SCREEN, d
            elif h[0] != -1:
                return State.ACCEPT_VICTORY, h
            elif a[0] != -1:
                return State.HOME, a
            elif i[0] != -1:
                return State.FINDING_MATCH, 0
            elif m[0] != -1:
                return State.POST_GAME_LOBBY, m
            else:
                return State.UNKNOWN_STATE, 0

        except:
            print("error occurred, continuing anyway")


    def loop(self):
        #keyboard.write("Testing this sick keyboard writer")
        #keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

        while True:
            try:
                beforeanythingpos = pyautogui.position()
                state, position = self.determine_current_state()
                print(state)
                print(position)
                
                if self.active:
                    if state == State.HOME:
                        click_image("play.png", position, "left", 0.2, offset=5)
                        
                        pyautogui.moveTo(beforeanythingpos)
                        time.sleep(1)

                    elif state == State.GAME_TYPE_SELECT:
                        click_image("confirm.png", position, "left", 0.2, offset=5)
                        
                        pyautogui.moveTo(beforeanythingpos)
                        time.sleep(1)
                    elif state == State.LOBBY:
                        click_image("findmatch.png", position, "left", 0.2, offset=5)

                        pyautogui.moveTo(beforeanythingpos)
                        time.sleep(1)
                    
                    elif state == State.EXIT:
                        click_image("exitnow.png", position, "left", 0.2, offset=5)
                        
                        pyautogui.moveTo(beforeanythingpos)
                        time.sleep(1)

                    elif state == State.FINDING_MATCH:
                        time.sleep(2)
                    
                    elif state == State.ACCEPT_SCREEN:
                        click_image("accept.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)

                    elif state == State.LOCK_SCREEN:
                        click_image("lockscreen.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)
                        
                    elif state == State.SURRENDER_2:
                        click_image("surr2.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)

                    elif state == State.SURRENDER_1:
                        click_image("surr1.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)
                    
                    elif state == State.OPTIONS:
                        pos2 = imagesearcharea("options.png", 0, 0, 1920, 1080, 0.8)

                        if (pos2[0] != -1):
                            click_image("options.png", pos2, "left", 0.2, offset=5)

                        pyautogui.moveTo(beforeanythingpos)

                    elif state == State.MOVE_AROUND_MODE:
                        self.waitRandomShortTime()
                        self.moveMouseRandomPosition()
                        pyautogui.mouseDown(button="right")
                        self.waitRandomShortTime()
                        pyautogui.mouseUp(button="right")
                        pyautogui.moveTo(beforeanythingpos)
                        self.waitRandomShortTime()

                        pyautogui.moveTo(580 + random.randint(1,5), 940 + random.randint(1,5))
                        pyautogui.mouseDown(button="left")
                        self.waitRandomShortTime()
                        pyautogui.mouseUp(button="left")

                        pyautogui.moveTo(785 + random.randint(1,5), 940 + random.randint(1,5))
                        pyautogui.mouseDown(button="left")
                        self.waitRandomShortTime()
                        pyautogui.mouseUp(button="left")

                        pyautogui.moveTo(980 + random.randint(1,5), 940 + random.randint(1,5))
                        pyautogui.mouseDown(button="left")
                        self.waitRandomShortTime()
                        pyautogui.mouseUp(button="left")
                        
                        pyautogui.moveTo(1185 + random.randint(1,5), 940 + random.randint(1,5))
                        pyautogui.mouseDown(button="left")
                        self.waitRandomShortTime()
                        pyautogui.mouseUp(button="left")

                        pyautogui.moveTo(1380 + random.randint(1,5), 940 + random.randint(1,5))
                        pyautogui.mouseDown(button="left")
                        self.waitRandomShortTime()
                        pyautogui.mouseUp(button="left")

                        #click_image("nexus.png", position, "left", 0.2, offset=10)
                        pyautogui.moveTo(beforeanythingpos)

                        time.sleep(5)

                    elif state == State.ACCEPT_VICTORY:
                        click_image("continue.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)
                        
                        time.sleep(5)

                    elif state == State.POST_GAME_LOBBY:
                        click_image("playagain.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)

                        time.sleep(5)

                    elif state == State.OK:
                        click_image("ok.png", position, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)

                        time.sleep(5)

            except:
                print("error occurred, continuing anyway")

    def waitRandomShortTime(self):
        time.sleep(random.uniform(0.1, 0.4))

    def waitRandomTime(self):
        # random time between the two times
        time.sleep(random.uniform(0.5, 1.5))

    def moveMouseRandomPosition(self):
        x = random.uniform(0, 1920)
        y = random.uniform(0, 1080)
        #bottom left corner of screen

        pyautogui.moveTo(x, y)
    
    def __init__(self):
        self.active = True
        self.loop()

if __name__ == '__main__':
    Main()