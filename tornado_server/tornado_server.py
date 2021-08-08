from typing import TypedDict
import logging
from filter.filter import FilterBadWords
import tornado.ioloop
import tornado.web


logging.basicConfig(level=logging.INFO, format='%(message)s')


class DtoModel(TypedDict):
    data: str


class MainHandler(tornado.web.RequestHandler):
    my_filter = FilterBadWords('filter/resources/list_of_bad_words.txt')

    def post(self):
        data_dto = DtoModel(
            data=self.get_argument('data', 'No data received')
        )
        self.write(self.my_filter.filter(data_dto['data']))


def make_app():
    return tornado.web.Application([
        (r"/api/filter-bad-words/en-US", MainHandler),
    ])


def my_app():
    logging.info('Сервер запущен...')
    app = make_app()
    try:
        app.listen(4201)
    except:
        logging.error('Ошибка порта, попробуйте указать другой порт и перезапустите приложение')
        return
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    my_app()
