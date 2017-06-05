#coding=utf-8
import urllib.request

def run_demo():
    f=urllib.request.urlopen('http://www.baidu.com')
    print(f.read())

if __name__=='__main__':
    run_demo()