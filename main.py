import logging

__author__ = 'chenwei'

__author__ = 'chenwei'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import datetime

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

logger = logging.getLogger('demo')

count = 0;


## 模拟场景一：


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('index.html')

class TestAdd(tornado.web.RequestHandler):
    def get(self):
        print('TestAdd()')
        global count;
        count += 1;

        print('count = ',count)
        self.render('index.html')

class SetEncryptPwd(tornado.web.RequestHandler):
    '''将js解析后的值传过来，进行保存'''
    def get(self):
        print('SetEncryptPwd  get()')
    def post(self, *args, **kwargs):
        print("SetEncryptPwd() post() ")

        # print(self.request)
        print(self.request.body)

class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r"/", MainHandler),
            (r"/add", TestAdd),
            (r"/set_encrypt_pwd", SetEncryptPwd),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        );
        tornado.web.Application.__init__(self,handlers,**settings)

        LOGDIR = os.path.join(os.getcwd(),'log')
        LOGFILE = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        logging.basicConfig(level=logging.DEBUG,
                            format='',
                            datefmt='%a, %d %b %Y',
                            filename = os.path.join(LOGDIR,LOGFILE),
                            filemode='a'
                            )

        fileLog = logging.FileHandler(os.path.join(LOGDIR,LOGFILE),'w')
        formatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s')
        fileLog.setFormatter(formatter)

        logger.addHandler(fileLog)
        logger.setLevel(logging.DEBUG)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()


