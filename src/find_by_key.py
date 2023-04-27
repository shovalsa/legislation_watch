import pathlib


def parse_key_words(input: str = 'data/key_words'):
    keys_path = pathlib.Path(input)
    with open(keys_path, 'r') as file:
        text = file.read()

    words = text.split(' ')  # split by space
    lines = text.split('\n')  # split by newline
    commas = text.split(',')  # split by comma

    combined_list = []
    combined_list.extend(words)
    combined_list.extend(line.strip(',\n') for line in lines)
    combined_list.extend(commas)
