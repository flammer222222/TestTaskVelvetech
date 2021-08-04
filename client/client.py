import requests


url = "http://localhost:4201/api/filter-bad-words/en-US"
while 1:
	print('\nВведите сообщение("/q" для выхода):')
	input_string = input()
	if input_string == '/q':
		break
	post_data = {'data': input_string}
	try:
		request_result = requests.post(url, post_data)
		print("\nОтфильтрованный ответ:")
		print(request_result.text)
	except:
		print("\nНе удалось подключиться по адресу ", url)
