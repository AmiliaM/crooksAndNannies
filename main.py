import pygame, init, draw, game, sys

def main():
    init.init()
    print("good morning")
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
    main()
