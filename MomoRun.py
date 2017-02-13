from ProxyCrawl import *
import requests

momo_url = 'http://www.maimemo.com/share/page/?uid=328327&pid=766'

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
    # useful_http_proxy = ['http://121.40.139.217:80',
    #                      'http://36.249.192.128:8118',
    #                      'http://118.123.245.153:3128',
    #                      'http://115.231.105.109:8081',
    #                      'http://121.40.139.217:80',
    #                      'http://115.231.105.109:8081',
    #                      'http://121.40.139.217:80',
    #                      'http://106.46.136.59:808',
    #                      'http://115.231.105.109:8081',
    #                      'http://106.46.136.29:808',
    #                      'http://115.231.105.109:8081',
    #                      'http://118.123.245.152:3128'
    #                      ]
    # for i in useful_http_proxy:
    #     proxy_ip = {'http': i}
    #     try:
    #         momo_request = requests.get(momo_url, proxies=proxy_ip)
    #     except:
    #         print(proxy_ip)
    #         continue
    #     print(momo_request)
