import requests
from typing import TypedDict
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')
url = "http://localhost:4201/api/filter-bad-words/en-US"


class DtoModel(TypedDict):
	data: str


while 1:
	logging.info('\nВведите сообщение("/q" для выхода):')
	input_string = input()
	if input_string == '/q':
		break

	data_dto = DtoModel(
		data=input_string
	)
	try:
		request_result = requests.post(url, data_dto)
		logging.info("\nОтфильтрованный ответ:")
		logging.info(request_result.text)

	except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError) as e:
		logging.error("Не удалось подключиться по адресу " + url)
		logging.error("\nНеправильно задан URL")

	except Exception:
		logging.error('Непредвиденная ошибка')


