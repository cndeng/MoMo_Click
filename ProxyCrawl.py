from bs4 import BeautifulSoup
import requests
import random


def get_ip_list(url, headers):
    web_ip = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_ip.text, 'lxml')
    ip_set = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ip_set)):
        ip_info = ip_set[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxy_log = {'http': proxy_ip}
    return proxy_log


def get_proxy_ip():
    proxy_url = 'http://www.xicidaili.com/wt/'
    proxy_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36'
    }
    proxy_list = get_ip_list(proxy_url, proxy_headers)
    return proxy_list
