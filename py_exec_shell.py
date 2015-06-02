import os
from subprocess import PIPE

__author__ = 'chenwei'


def test_2():
    dd = os.system('phantomjs  test.js')


def test_3():
    import subprocess

    # retcode = subprocess.call(["ls", "-l"])
    retcode = subprocess.call(["phantomjs", "test.js"])

    # data = subprocess.Popen(['phantomjs','test.js'])
    # subprocess.Popen('phantomjs test.js')
    # p = subprocess.Popen('phantomjs test.js',stdout=PIPE)
    # data = p.stdout.readlines();
    # # # print(p.stdout.readlines())
    # print(data)
    # print(data[0])
    # print(len(data))
    # print(data[0])
def test():
    pass

    # dd = os.system('ls')
    # print(type(dd))
    # print(dd)
    #
    # import commands
    # a,b = commands.getstatusoutput('ls')

    # dd = os.system("echo \"Hello World\"")
    # print()
    # import commands

    # from subprocess import call
    # dd = call(["ls", "-l"])
    # print(type(dd))
    # print('dd= ',dd)

    # import subprocess
    # p = subprocess.Popen('pwd',stdout=subprocess.PIPE)
    #
    # data = p.stdout.readlines();
    # # print(p.stdout.readlines())
    # print(data)
    # print(len(data))
    # print(data[0])

if __name__ == '__main__':
    # test()
    # test_2()
    test_3()