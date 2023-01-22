import tornado.httpserver
import tornado.ioloop
import tornado.web

class getToken(tornado.web.RequestHandler):
    def get(self):
        self.render("./demo.html")

class getDetector(tornado.web.RequestHandler):
    def get(self):
        self.render("./note-detector.js")

class getUtils(tornado.web.RequestHandler):
    def get(self):
        self.render("./note-utils.js")

application = tornado.web.Application([
    (r'/', getToken),
    (r'/demo.html', getToken),
    (r'/note-detector.js', getDetector),
    (r'/note-utils.js', getUtils),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "certfile": "note-detector.crt",
        "keyfile": "note-detector.key",
    })
    http_server.listen(443)
    tornado.ioloop.IOLoop.instance().start()
