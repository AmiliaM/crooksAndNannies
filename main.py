import pygame, init, draw, game


def end():
    pygame.quit()

def main():
    init.init()
    print("good morning")
    while 1:
        game.processUserInput()
        draw.draw()
    end()


if __name__ == "__main__":
    main()
