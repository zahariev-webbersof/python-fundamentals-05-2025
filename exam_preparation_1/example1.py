data = input().split('!')

while (command := input()) != 'Go Shopping!':
    parts = command.split()
    action, *args = parts

    match action:
        case 'Urgent' if args[0] not in data: data.insert(0, args[0])
        case 'Unnecessary' if args[0] in data: data.remove(args[0])
        case 'Correct' if args[0] in data: data[data.index(args[0])] = args[1]
        case 'Rearrange' if args[0] in data: data.remove(args[0]); data.append(args[0])

print(', '.join(data))
