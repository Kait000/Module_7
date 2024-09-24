def custom_write(file_name, string):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(string)):
        strings_positions[(str(i+1), file.tell())] = string[i]
        file.write(f'{string[i]}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
