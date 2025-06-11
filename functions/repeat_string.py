repeat_string = lambda text, counter: text * counter

current_text = input()
current_counter = int(input())
result = repeat_string(current_text, current_counter)


def print_result(text: str):
    print(text)


print_result(result)
