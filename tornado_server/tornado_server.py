from typing import TypedDict
import logging
from filter.filter import FilterBadWords
import tornado.ioloop
import tornado.web

# настроим логирование
logging.basicConfig(level=logging.INFO, format='%(message)s')
# создадим фильтр для слов
path_bad_words = 'filter/resources/list_of_bad_words.txt'
path_good_words = 'filter/resources/list_of_good_words.txt'
# можно изменять расстояние Левенштейна
levenshtein_distance = 1
try:
    my_filter = FilterBadWords(path_bad_words, path_good_words, levenshtein_distance)
except FileNotFoundError:
    logging.error('Не удалось создать фильтр текста, неправильно указан путь к словарям')
except Exception:
    my_filter = None
    logging.error('Не удалось создать фильтр текста, проверьте его конфигурацию и перезапустите приложение')


class DtoModel(TypedDict):
    data: str


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        data_dto = DtoModel(
            data='Некорректно переданы данные'
        )
        if self.request.body_arguments.keys() == data_dto.keys():
            data_dto['data'] = self.get_argument('data', 'No data received')

        if my_filter is not None:
            self.write(my_filter.filter(data_dto['data']))
        else:
            self.write('Фильтр временно не работает')


def make_app():
    return tornado.web.Application([
        (r"/api/filter-bad-words/en-US", MainHandler),
    ])


def my_app():
    try:
        app = make_app()
        app.listen(4201)
        logging.info('Сервер запущен...')
        tornado.ioloop.IOLoop.current().start()

    except OSError:
        logging.error('Ошибка соединения, попробуйте указать другой порт и перезапустите приложение')

    except Exception:
        logging.error('Непредвиденная ошибка')


if __name__ == "__main__":
    my_app()
