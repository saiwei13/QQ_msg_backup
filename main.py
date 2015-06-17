import json
import logging
import threading
from tornado import web
from qq_login import SmartQQ

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
from utils import config_file
import configparser

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index2.html')

    def post(self, *args, **kwargs):
        pass
        # print('post()',self.request)
        # print('post() ',self.request.body);

class LoginHandler(tornado.web.RequestHandler):
    '''
    登录接口
    '''
    cf = configparser.ConfigParser()
    cf.read(config_file)

    # qq = SmartQQ(
    #     username=cf.get('qq','username'),
    #     password=cf.get('qq','password')
    # );

    qq = SmartQQ(
        username=cf.get('qq','username'),
        password=cf.get('qq','password')
    );

    def get(self):
        print('get()  self.id=',id(self))

        # self.write('hello world'+str(datetime.datetime.now()))

        uri = self.request.uri;
        print('uri='+uri)

        if uri == '/check':
            tmp = self.qq.check_vc();
            msg = tornado.escape.json_decode(tmp)
            print(msg)
            self.write(msg)
        elif uri == '/getimage':
            msg = self.qq.get_captcha()
            msg = tornado.escape.json_decode(msg)
            self.write(msg)
        elif uri == '/encrypt':
            self.render('encrypt.html')
        else:
            print('not deal ： match '+uri)

    def post(self):

        # print('post() self.id=',id(self))
        # print('LoginHandler post() ',self.request.body)
        uri = self.request.uri;
        print('uri='+uri)

        body = self.request.body;
        print(body)

        msg = tornado.escape.json_decode(body)
        # print(msg);

        if(uri == "/login"):
            vcode = msg['vcode']
            encrypt_pwd = msg['encrypt_pwd']
            msg = self.qq.sign_in(vcode,encrypt_pwd)
            msg = tornado.escape.json_decode(msg)
            self.write(msg)
        elif(uri == '/get_user_friends2'):
            self.qq.get_user_friends(msg['hash'])
        elif(uri == '/poll2'):
            self.qq.poll2()
            pass

class Test(tornado.web.RequestHandler):

    @web.asynchronous
    def worker(self):
        import time
        time.sleep(5)

        self.write('sleep 5')
        self.finish()

    def get(self, *args, **kwargs):
        print(self.request.body)

        # w = threading.Thread(name='get_encrypt_pwd', target=self.worker)
        # w.start()

        pass
    def post(self, *args, **kwargs):
        print('Test.class  post()  ',self.request.body)

        # s= '\x00\x00\x00\x00\x7c\x0f\x3f\xf3';
        #
        # self.write('no sleep')
        # self.write('hello world!!!')
        pass

class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        );

        handlers = [
            (r"/", MainHandler),
            (r"/test", Test),
            # (r"/set_encrypt_pwd", LoginHandler),
            # (r"/static/(.*)",tornado.web.StaticFileHandler,{'path':'html/static'}),
            (r"/check", LoginHandler),
            (r"/getimage", LoginHandler),
            (r"/login", LoginHandler),
            (r"/get_user_friends2",LoginHandler),
            (r"/poll2",LoginHandler),
            # (r"/encrypt", LoginHandler),
        ]

        tornado.web.Application.__init__(self,handlers,**settings)

        # LOGDIR = os.path.join(os.getcwd(),'log')
        LOGDIR = os.path.join('/home/chenwei/workspace/PycharmProjects/QQ_msg_backup','log')
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