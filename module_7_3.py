class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # кортеж (tuple) имен файлов
        #  print(f'Кортеж имен файлов:, {type(self.file_names)}, {self.file_names}')

    def get_all_words(self):
        all_words = {}  # возвращаемый словарь {файл: список слов}
        del_char = [',', '.', '=', '!', '?', ';', ':', ' - ']  # список удаляемых символов
        for i in range(len(self.file_names)):  # перебираем список файлов
            #  print(f'Файл {i}, {self.file_names[i]}')
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                new_str = ''
                for line in file:
                    for _char in del_char:
                        line = line.replace(_char, '')
                    new_str += line.lower()
            # print(f'Строка слов из файла: {new_str}')
            # print(f'Строка слов из файла: {new_str.split()}')
            all_words[self.file_names[i]] = new_str.split()  # добавляем в словарь {файл: список слов}
        return all_words

    def find(self, word):
        find_dict = {}  # возвращаемый словарь {файл: позиция слова в файле}
        for name, words in self.get_all_words().items():  # name - имя файла, words - список слов
            # print(f'Слова: {words}')
            for i in range(len(words)):
                if word.lower() == words[i]:
                    #  print(f'Слово {word}, найдено в файле {name}, слово по счету {str(i+1)}')
                    find_dict[name] = i+1
                    break
        return find_dict

    def count(self, word):
        count_dict = {}  # возвращаемый словарь {файл: количество слов в файле}
        for name, words in self.get_all_words().items():  # name - имя файла, words - список слов
            words = words.count(word.lower())
            count_dict[name] = words
            #  print(f'Кол-во слов {word} в файле {name} = {words}')
        return count_dict


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # все слова
print(finder1.find('TEXT'))     # 3-е слово по счёту
print(finder1.count('teXT'))    # в тексте 4 слова teXT
