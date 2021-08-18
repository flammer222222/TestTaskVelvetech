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
		# сначала проверять будем самые длинные
		self.__bad_phrases.sort(key=len, reverse=True)

	def replace_space_words(self, valid_data):
		# задаем конечную точку
		end_point = 0
		# собираем слово без пробелов
		while end_point < len(valid_data) and len(normalize(valid_data[end_point])) <= 1:
			end_point += 1

		current_string = ''.join(valid_data[0:end_point])
		if normalize(current_string) not in self.__good_words:
			for word in self.__bad_words:
				if Levenshtein.distance(current_string, word) <= self.__levenshtein_distance:
					# заменяем элементы списка, с учетоми пробелов и длины строки
					valid_data[:end_point] = ['*' * (len(valid_data[0:end_point]) - 1 + len(current_string))]
					# возвращаем исходный список и шаг на который надо сместиться
					return valid_data, 0

		# возвращаем исходный список и шаг на который надо сместиться
		# -1 чтобы не сбить счетчик в главной функции и не перескочить слово
		return valid_data, end_point - 1

	def filter(self, input_string):
		#  сначала заменим все фразы из строки
		for phrase in self.__bad_phrases:
			input_string = input_string.replace(phrase, '*'*len(phrase))

		# пройдем по созданному списку и заменим все слова, которые есть в множестве плохих слов
		valid_data = input_string.split(' ')
		i = 0
		while i < len(valid_data):
			# вначале нормализуем строку
			# Заменяем только если они не в хороших словах
			if len(normalize(valid_data[i])) != 1 and normalize(valid_data[i]) not in self.__good_words:
				for word in self.__bad_words:
					if Levenshtein.distance(valid_data[i], word) <= self.__levenshtein_distance:
						valid_data[i] = '*'*len(valid_data[i])

			elif len(normalize(valid_data[i])) == 1:
				valid_data[i:], count = self.replace_space_words(valid_data[i:])
				i += count

			i += 1
		# Соберем все в строку
		return ' '.join(valid_data)


if __name__ == '__main__':
	test_string = 'some string 1'
	test_string2 = 'some string 2'
	test_string3 = 'some string 3'

	path_bad_words = 'resources/list_of_bad_words.txt'
	path_good_words = 'resources/list_of_good_words.txt'
	levenshtein_distance = 1

	my_filter = FilterBadWords(path_bad_words, path_good_words, levenshtein_distance)
	print(my_filter.filter(test_string))
	print(len(my_filter.filter(test_string)) == len(test_string))
	print(my_filter.filter(test_string2))
	print(len(my_filter.filter(test_string2)) == len(test_string2))
	print(my_filter.filter(test_string3))
	print(len(my_filter.filter(test_string3)) == len(test_string3))
