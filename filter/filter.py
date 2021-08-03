class FilterBadWords:
    def __init__(self, path_bad_words):
        self.__bad_phrases = []
        self.__bad_words = set()
        # отдельно соберем фразы и слова
        with open(path_bad_words, encoding='utf-8') as file:
            for word in file:
                if word.strip().find(' ') != -1:
                    self.__bad_phrases.append(word[:-1].strip())
                else:
                    self.__bad_words.add(word[:-1].strip())

    def filter(self, input_string):
        #  сначала удалим все фразы из строки
        for phrase in self.__bad_phrases:
            input_string = input_string.replace(phrase, '*'*len(phrase))

        # пройдем по созданному списку и заменить все слова, которые есть в множестве плохих слов
        valid_data = input_string.split(' ')
        for i in range(len(valid_data)):
            if valid_data[i] in self.__bad_words:
                valid_data[i] = '*'*len(valid_data[i])

        return ' '.join(valid_data)


if __name__ == '__main__':
    test_string = "rkrrk aslpsap anus slfd sfaf anal analsssd ddd bunny fucker"
    my_filter = FilterBadWords('resources/list_of_bad_words.txt')
    print(my_filter.filter(test_string))
