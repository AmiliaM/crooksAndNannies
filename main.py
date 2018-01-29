import pygame, init, draw, game, sys, atexit

tutorialShown = False

def main():
    global tutorialShown
    init.init()
    print("good morning")
    if not tutorialShown:
        draw.tutorial()
        tutorialShown = True
    draw.menu()
    while 1:
        game.processUserInput()
        draw.moveNanny()
        if game.isGameWon(): 
            draw.win()
            break
        if game.isGameover(): 
            draw.gameover()
            break
        draw.render()
    main()


if __name__ == "__main__":
    atexit.register(lambda: print("good night"))
    main()
