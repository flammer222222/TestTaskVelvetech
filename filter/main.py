class FilterBadWords:
    def __init__(self, path_bad_words):
        with open(path_bad_words, encoding='utf-8') as file:
            self.__bad_words = [word[:-1] for word in file]
            self.__bad_words.sort(key=len, reverse=True)

    def filter(self, input_string):
        for word in self.__bad_words:
            input_string = input_string.replace(word, '*'*len(word))
        return input_string


test_string = "rkrrk aslpsap anus slfd sfaf anal analsssd ddd bunny fucker"
if __name__ == '__main__':
    my_filter = FilterBadWords('resources/list_of_bad_words.txt')
    print(my_filter.filter(test_string))
    print(test_string)
