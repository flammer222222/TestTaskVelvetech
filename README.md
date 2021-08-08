# TestTaskVelvetech
Фильтр мата слушающий порт 4201 и имеющий 1 endpoint - /api/filter-bad-words/en-US

Для запуска можно использовать 3 варианта:
  1. Запустить скрипты через python напрямую
  2. Собрать свои docker контейнеры и запустить в них
  3. Скачать уже готовые docker контейнеры (https://hub.docker.com/r/flammer222222/test_task_velvetech1/tags?page=1&ordering=last_updated)

1. Запуск через python
  - С помощью команд pip install tornado и pip instal requests установить дополнительные библиотеки.
  - Запустить файл tornado_server/tornado_server.py 
  - Запустить файл test_filter/test_filter.py, который проводит небольшой тест работоспособности фильтра
  - Запустить файл client/client.py

2. Сборка своих контейнеров docker
  - открыть в папке tornado_server терминал, ввести "docker build -t server_for_filter_bad_words ." 
  - открыть в папке client терминал, ввести "docker build -t client_for_filter_bad_words ."
  - открыть в папке test_filter терминал, ввести "docker build -t test_for_filter_bad_words ."

  - Запустить сервер с помощью команды "docker run -it -p 4201:4201 server_for_filter_bad_words"
  - Запустить тест с помощью команды "docker run -it --network="host" test_for_filter_bad_words"
  - Запустить клиент с помощью команды "docker run -it --network="host" client_for_filter_bad_words"

3. Запуск готовых контейнеров docker
  - С помощью команды "docker pull flammer222222/test_task_velvetech1:test_for_filter_bad_words" нужно скачать образ теста
  - С помощью команды "docker pull flammer222222/test_task_velvetech1:client_for_filter_bad_words" нужно скачать образ клиента
  - С помощью команды "docker pull flammer222222/test_task_velvetech1:server_for_filter_bad_words" нужно скачать образ сервера

  - Запустить сервер с помощью команды "docker run -it -p 4201:4201 flammer222222/test_task_velvetech1:server_for_filter_bad_words"
  - Запустить тест с помощью команды "docker run -it --network="host" flammer222222/test_task_velvetech1:test_for_filter_bad_words"
  - Запустить клиент с помощью команды "docker run -it --network="host" flammer222222/test_task_velvetech1:client_for_filter_bad_words"
  
