text_data = input().split()
new_text = [text * len(text) for text in text_data]

print(''.join(new_text))