import time

__author__ = 'chenwei'

# config_file = 'config.ini'

config_file = '/home/chenwei/workspace/PycharmProjects/QQ_msg_backup/config.ini'

'''配置文件'''


def timestamp():
    return int(time.time()*1000 )
    ##1392637410384
    ##1431270579


if __name__ == '__main__':

    print(type(timestamp()))