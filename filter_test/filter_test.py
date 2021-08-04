import requests


url = "http://localhost:4201/api/filter-bad-words/en-US"


def filter_test():
	with open('resources/list_of_bad_words.txt', encoding='utf-8') as file:
		bad_words = [word.strip() for word in file]

	not_filtered = []

	for word in bad_words:
		post_data = {'data': word}
		try:
			res = requests.post(url, post_data)
		except:
			print("\nНе удалось подключиться по адресу ", url)
			return
		if res.text != '*'*len(word):
			not_filtered.append(word)
	if not not_filtered:
		print('Все слова и фразы фильтруются корректно')
	else:
		print('Слова и фразы, которые не отфильтровались: ')
		print(not_filtered)


if __name__ == "__main__":
	print('Проверка фильтра, подождите...')
	filter_test()
