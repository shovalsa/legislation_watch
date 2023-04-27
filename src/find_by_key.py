import pathlib
keys_path = pathlib.Path('data/key_words')
with open(keys_path, 'r') as file:
    text = file.read()

words = text.split(' ')  # split by space
lines = text.split('\n')  # split by newline
commas = text.split(',')  # split by comma

combined_list = []
combined_list.extend(words)
combined_list.extend(line.strip(',\n') for line in lines)
combined_list.extend(commas)


kuku=1