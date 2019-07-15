# -*- coding: utf-8 -*-

# -------------------------------------------------
# @Time    : 7/12/19 5:23 PM
# @Author  : 蒋默然
# @File    : sub_station_spider.py
# -------------------------------------------------
import json
import logging
import re
import time
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
        # print(title)
        line = []
        for sta in stations:
            name = pq(sta)('.station .link').text()
            line.append(name)
        line_info_dict[title] = line
    return line_info_dict


def get_poi(line_info_dict):
    location = set()
    for i in line_info_dict:
        for m in line_info_dict[i]:
            location.add(m)
    result = {}
    for i in location:
        poi_url = 'http://api.map.baidu.com/geocoder?address={}&output=json&key=37492c0ee6f924cb5e934fa08c6b1676&city=%E5%8C%97%E4%BA%AC%E5%B8%82'.format(i)
        r = requests.get(poi_url)
        js_data = json.loads(r.text)
        print(js_data)
        poi = js_data['result']['location']
        print(poi)
        result[i] = poi
        time.sleep(0.1)


def main():
    url = 'http://bj.bendibao.com/ditie/linemap.shtml'
    line_info = get_index(url)
    get_poi(line_info)


if __name__ == '__main__':
    main()