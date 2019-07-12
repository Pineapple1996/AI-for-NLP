# -*- coding: utf-8 -*-

# -------------------------------------------------
# @Time    : 7/12/19 5:23 PM
# @Author  : 蒋默然
# @File    : sub_station_spider.py
# -------------------------------------------------
import logging
import re

import requests
from pyquery import PyQuery as pq

def get_index(url):
    try:
        r = requests.get(url)
    except Exception as e:
        logging.error(e)
        return
    div = pq(r.text)('.line-list')
    line_info_dict = {}
    for i in div:
        title = pq(i)('div.line-list-heading > div > strong').text().strip('线路图')
        stations = pq(i)('.station')

        # title = re.findall('(\w+)',title)[0] if re.findall('\d+',title) else title
        print(title)
        line = []
        for sta in stations:
            name = pq(sta)('.station .link').text()
            line.append(name)
        line_info_dict[title] = line
    print(line_info_dict)


def main():
    url = 'http://bj.bendibao.com/ditie/linemap.shtml'
    get_index(url)


if __name__ == '__main__':
    main()