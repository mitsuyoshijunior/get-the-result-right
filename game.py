from models.calculate import Calculate

def main() -> None:
    scores: int = 0
    play_game(scores)

def play_game(scores: int) -> None:

    level: int = int(input('What level of difficulty do you want? Type 1, 2, 3, or 4 — from easiest to hardest.'))

    calc: Calculate = Calculate(level)
    calc.show_operation()

    answer: int = int(input('Type your answer: '))

    if calc.check_result(answer):
        scores += 1
        print(f'Congratulations! Your answer ir correct! You have {scores} points!')

    keep: int = int(input('Do you want to keep playing? Type 1 for yes or 0 for no.'))

    if keep:
        play_game(scores)
    else:
        print(f'You finished this game with {scores} points! See you!')


if __name__ == '__main__':
    main()