class Test(object):
    a = 1

    def abc_1(self):
        print('Poi')

    def abc_2(self):
        print("f2")

    def abc_3(self):
        print("f3")

    def fun(self):
        for key in Test.__dict__.keys():
            if 'abc_' in key:
                # Test.__dict__[key](self)
                eval("self.{}()".format(key))  #两种发放都可行,推荐这个方式  参看https://github.com/Python3WebSpider/ProxyPool/blob/master/proxypool/scheduler.py 


if __name__ == '__main__':
    test = Test()
    test.fun()
