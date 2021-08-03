from filter.filter import FilterBadWords
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    my_filter = FilterBadWords('../filter/resources/list_of_bad_words.txt')
    filtered_data = ['']

    def get(self):
        self.write(self.filtered_data[0])

    def post(self):
        self.filtered_data[0] = self.my_filter.filter(self.get_argument('data', 'No data received'))
        self.write(self.filtered_data[0])


def make_app():
    return tornado.web.Application([
        (r"/api/filter-bad-words/en-US", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(4201)
    tornado.ioloop.IOLoop.current().start()
