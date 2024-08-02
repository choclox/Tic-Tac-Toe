import random


def run():
    print("""Welcome to ROCK-PAPER-SCISSORS

1.Rock
2.Paper
3.Scissors

This game consist of the best of 3 games
""")

    # rock = 1
    # paper = 2
    # scissors = 3

    user_points = 0
    program_points = 0

    def wins():
        print("YOU WIN +1 POINT")

    def loses():
        print("PROGRAM WINS +1 POINT")

    def draw():
        print("ITS A DRAW")

    for i in range(3):
        program_selection = random.randint(1, 3)
        print("")
        user_selection = int(input("select your game: "))
        print("The program chose:" + str(program_selection))
        int(program_selection)
        if user_selection == program_selection:
            draw()
        elif user_selection == 1 and program_selection == 3 or user_selection == 2 and program_selection == 1 or user_selection == 3 and program_selection == 2:
            wins()
            user_points = user_points + 1
        elif user_selection == 1 and program_selection == 2 or user_selection == 2 and program_selection == 3 or user_selection == 3 and program_selection == 1:
            loses()
            program_points = program_points + 1

    print("")

    if user_points > program_points:
        print("CONGRATULATIONS, YOU WIN THE GAME")
    elif user_points < program_points:
        print("SORRY, YOU LOSE THE GAME")
    elif user_points == program_points:
        print("WOW, ITS DRAW")

# posibilities
# 1-1 , 2-2 , 3-3 draws
# 1-3 , 2-1 , 3-2 wins
# 3-1 , 1-2 , 2-3 loses


if __name__ == "__main__":
    run()
