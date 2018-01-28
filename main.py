import pygame, init, draw, game, sys

def main():
    init.init()
    print("good morning")
    while 1:
        game.processUserInput()
        if game.isGameWon(): draw.win()
        if game.isGameover(): draw.gameover()
        draw.render()


if __name__ == "__main__":
    main()
