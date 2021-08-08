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
	request_result = requests.post(url, data_dto)

	logging.info("\nОтфильтрованный ответ:")
	logging.info(request_result.text)
	logging.error("\nНе удалось подключиться по адресу " + url)
