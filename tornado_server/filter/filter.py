import Levenshtein


def normalize(input_string):
    normalize_string = input_string.lower()
    normalize_string = normalize_string.replace('0', 'o')
    normalize_string = normalize_string.replace('1', 'l')
    normalize_string = normalize_string.replace('5', 's')
    normalize_string = normalize_string.replace('$', 's')
    normalize_string = normalize_string.replace('@', 'a')
    normalize_string = normalize_string.replace('2', 'z')
    normalize_string = normalize_string.replace('|', 'i')
    return normalize_string


class FilterBadWords:
    def __init__(self, path_bad_words, path_good_words, levenshtein_distance):
        self.__bad_phrases = []
        self.__bad_words = []
        self.__levenshtein_distance = levenshtein_distance
        # создадим список хороших слов
        with open(path_good_words, encoding='utf-8') as file:
            self.__good_words = {word.strip() for word in file}

        # отдельно соберем плохие фразы и слова
        with open(path_bad_words, encoding='utf-8') as file:
            for word in file:
                if word.strip().find(' ') != -1:
                    self.__bad_phrases.append(word.strip())
                else:
                    self.__bad_words.append(word.strip())
        self.__bad_phrases.sort(key=len, reverse=True)

    def remove_bad_spaces_word(self, input_string):
        output_string = input_string
        i = 0
        while i < len(input_string):
            if input_string[i] == ' ':
                # счетчик букв идущих подряд
                count_letter = 0
                # начальная и конечная точки среза строки с пробелами
                start_point = i + 1
                end_point = i + 1
                while count_letter != 2:
                    i += 1
                    if input_string[i] != ' ':
                        count_letter += 1
                        end_point = i - 2
                    else:
                        count_letter = 0
                # удалим чередуются пробелы из участка строки
                current_string = input_string[start_point: end_point].replace(' ', '')
                # вначале нормализуем строку
                if normalize(current_string) not in self.__good_words:
                    for word in self.__bad_words:
                        if Levenshtein.distance(current_string, word) < self.__levenshtein_distance:
                            # заменяем часть строки, содержащую плохие слова с пробелами
                            print(start_point, end_point)
                            output_string = output_string[:start_point] + '*' * (end_point - start_point) + output_string[end_point:]
            i += 1
        return output_string

    def filter(self, input_string):
        #  сначала заменим все фразы из строки
        for phrase in self.__bad_phrases:
            input_string = input_string.replace(phrase, '*'*len(phrase))

        # пройдем по созданному списку и заменим все слова, которые есть в множестве плохих слов
        valid_data = input_string.split(' ')
        for i in range(len(valid_data)):
            # Заменяем только если они не в хороших словах
            # вначале нормализуем строку
            if normalize(valid_data[i]) not in self.__good_words:
                for word in self.__bad_words:
                    if Levenshtein.distance(valid_data[i], word) < self.__levenshtein_distance:
                        valid_data[i] = '*'*len(valid_data[i])
        # Проверим слова с многочисленными пробелами
        return self.remove_bad_spaces_word(' '.join(valid_data))


if __name__ == '__main__':
    test_string = "rkrrk aslpsap anus slfd sfaf anal analsssd ddd bunny fucker f u c k  a s s h o l e asshole hello"
    test_string2 = 'ass bloody butt damn fucking God hell sex shit'

    path_bad_words = 'resources/list_of_bad_words.txt'
    path_good_words = 'resources/list_of_good_words.txt'
    levenshtein_distance = 2

    my_filter = FilterBadWords(path_bad_words, path_good_words, levenshtein_distance)
    print(my_filter.filter(test_string))
    print(my_filter.filter(test_string2))
