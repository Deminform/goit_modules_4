import string
from datetime import datetime
from pathlib import Path

list_of_dir = ['unicode', 'utf-8', 'utf-16']

alphabet = string.ascii_letters
alphabet += string.digits
file_path = None

for type_of_data in list_of_dir:

    DIRECTORY_PATH = Path('directory') / type_of_data
    DIRECTORY_PATH.mkdir(exist_ok=True)
    file_path = DIRECTORY_PATH / f'{type_of_data}.txt'

    with open(file_path, 'a') as write_file:
        write_file.write('Last record: ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')

    for char in alphabet:
        if type_of_data == 'unicode':
            line = f'Symbol {char} / Unicode {ord(char)}\n'
        else:
            line = f'Symbol {char} / {type_of_data} {char.encode(type_of_data)}\n'

        with open(file_path, 'a') as write_file:
            write_file.write(line)

