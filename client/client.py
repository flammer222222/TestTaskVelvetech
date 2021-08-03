import requests


url = "http://localhost:4201/api/filter-bad-words/en-US"
input_string = ''
while input_string != '/q':
	input_string = input()
	post_data = {'data': input_string}
	res = requests.post(url, post_data)
	print(res.text)
