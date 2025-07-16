def memory_game():
    sequence_data = input().split()
    moves = 0

    while (command := input()) != 'end':
        moves += 1
        parts = command.split()

        match parts:
            case [a, b]:
                i1, i2 = int(a), int(b)

                match (i1 == i2 or not (0 <= i1 < len(sequence_data)) or not (0 <= i2 < len(sequence_data))):
                    case True:
                        middle_index = len(sequence_data) // 2
                        elem = f'-{moves}a'
                        sequence_data[middle_index:middle_index] = [elem, elem]
                        print(f'Invalid input! Adding additional elements to the board')

                    case False if sequence_data[i1] == sequence_data[i2]:
                        val = sequence_data[i1]
                        print(f"Congrats! You have found matching elements - {val}!")
                        for i in sorted([i1, i2], reverse=True):
                            sequence_data.pop(i)

                    case False:
                        print('Try again!')

            case _:
                print(...)

        if not sequence_data:
            print(f'You have won in {moves} turns!')
            return

    print('Sorry you lose :(')
    print(' '.join(sequence_data))


memory_game()
