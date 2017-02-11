from ProxyCrawl import *
import requests

momo_url = 'http://www.maimemo.com/share/page/?uid=328327&pid=765'

if __name__ == '__main__':
    proxy_list = get_proxy_ip()
    for i in range(1, 10):
        proxy_ip = get_random_ip(proxy_list)
        print(proxy_ip)
        try:
            momo_request = requests.get(momo_url, proxies=proxy_ip)
        except:
            continue
        print(momo_request)
