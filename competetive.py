import time
import tictactoe
import trainer
import pygame

try:
    while True:
        try:
            amount_of_games = int(input("enter"))
        except ValueError:
            amount_of_games = 1000
        beg = time.time()
        count = [0, 0, 0]
        train = trainer.TicTacToeTr(5, "mem5_tr.txt")
        tictac = tictactoe.TicTacToe(5, "mem5.txt", backup_filename="back_train.txt")

        try:
            tictac.remember()
        except tictactoe.NoMemoryError:
            tictac.memorize_to_file()

        try:
            train.remember()
        except trainer.NoMemoryError:
            train.memorize_to_file()

        for i in range(amount_of_games):
            tictac.nullify()
            train.nullify()
            b = True

            while True:
                tictac.display_board()
                if tictac.detect_draw():
                    count[0] += 1
                    train.memorize(train.prev_turn)
                    print("draw")
                    break
                move = train.do_turn()
                if not move:
                    print("train_bad_move")
                    if b:
                        print("that's it")
                        input()
                    move = train.do_bad_move()
                    if not move:
                        train.memorize(train.prev_turn)
                        count[0] += 1
                        print("draw")
                        break
                elif isinstance(move, int):
                    print(move, "won")
                    if move == 1:
                        count[1] += 1
                    if move == 2:
                        count[2] += 1
                    break

                while not tictac.player_turn(move[1], move[2]):
                    pass
                train.display_board()
                a = tictac.do_turn()
                if not a:
                    print("bad_move")
                    a = tictac.do_bad_move()
                    if not a:
                        count[0] += 1
                        train.memorize(train.prev_turn)
                        print("draw")
                        break
                elif isinstance(a, int):
                    print(a, "won")
                    if a == 1:
                        count[1] += 1
                    if a == 2:
                        count[2] += 1
                    break
                train.player_turn(a[1], a[2])
                b = False



        print(count[0], "draws")
        print(count[1], "loses")
        print(count[2], "wins")
        print(time.time() - beg, "seconds")
        print("writing to file")
        tictac.memorize_to_file()
        train.memorize_to_file()
        print("wrote to file")
        print("backing up")
        tictac.backup()
        train.backup()
        print("backed up")

except KeyboardInterrupt:
    print("ending here")
    print(count[0], "draws")
    print(count[1], "loses")
    print(count[2], "wins")
    print(time.time() - beg, "seconds")
    print("writing to file")
    tictac.memorize_to_file()
    train.memorize_to_file()
    print("wrote to file")
    print("backing up")
    tictac.backup()
    train.backup()
    print("backed up")