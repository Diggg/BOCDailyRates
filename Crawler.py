#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from bs4 import Tag
import codecs
import csv


def download_page(url):
    headers = { 'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)' }

    try:
        data = requests.get(url, headers=headers)
        data.raise_for_status()
        data.encoding=data.apparent_encoding
        return data.text
    except:
        print('爬取失败')


#直接输出文件进行输出
def parse_html2txt(html,fp):
    global count
    global page_count
    #print(page_count)
    soup = BeautifulSoup(html, "html.parser")
    rate_list_soup = soup.find_all('table')
    rate_list = rate_list_soup[1]
    for r in rate_list.children:
        if isinstance(r, Tag):
            cur_title = ''
            cur_rate = ''
            for r2 in r.children:
                if isinstance(r2,Tag):
                    if r2.get_text().strip() == '':
                        continue
                    if r2.name == 'th':
                        cur_title = cur_title + ',' + r2.get_text().strip()
                    if r2.name == 'td':
                        cur_rate = cur_rate + ',' + r2.get_text().strip()
                        count += 1
            #处理空行
            if page_count <0 and len(cur_title) >0:
                cur_title = cur_title.lstrip()[1:]
                fp.write(cur_title.strip()+'\n')
            cur_rate = cur_rate.lstrip()[1:]
            if len(cur_rate) > 0:
                fp.write(cur_rate.strip()+'\n')

    page_count += 1
    if page_count >= max_page:
        return None
    else:
        next_page = root_url + 'index_' + str(int(page_count + 1)) + '.html'
        if next_page:
            return next_page
        else:
            return None
#使用CSV进行输出
def parse_html2csv(html,fp):

    global count
    global page_count
    writer = csv.writer(fp,dialect='excel',delimiter = ',')
    soup = BeautifulSoup(html, "html.parser")
    rate_list_soup = soup.find_all('table')
    rate_list = rate_list_soup[1]
    for r in rate_list.children:
        if isinstance(r,Tag):
            cur_title1 = []
            cur_rate1 = []
            for r2 in r.children:
                if isinstance(r2,Tag):
                    if r2.get_text().strip() == '':
                        continue
                    if r2.name == 'th':
                        cur_title1.append(r2.get_text().strip())
                    if r2.name == 'td':
                        cur_rate1.append(r2.get_text().strip())
                        count += 1
            if page_count < 0 and len(cur_title1) >0:
                writer.writerow(cur_title1)
            if len(cur_rate1) > 0:
                writer.writerow(cur_rate1)
    page_count += 1
    if page_count >= max_page:
        return None
    else:
        next_page = root_url + 'index_' + str(int(page_count + 1)) + '.html'
        if next_page:
            return next_page
        else:
            return None


def genRateFile(parseFuc,fp):
    url = root_url
    while url:
        print(url)
        html = download_page(url)
        url = parseFuc(html,fp)
    fp.flush()
    fp.close()
    print(count, 'processed')
    print('done')


count = 0
page_count = -1
#最大抓取页数 http://www.boc.cn/sourcedb/whpj/index_19.html
#此网站每日只提供20页信息
max_page = 19
root_url = 'http://www.boc.cn/sourcedb/whpj/'
fp1 = codecs.open('DailyRates.txt', 'wb',encoding='utf-8')
fp2 = codecs.open('DailyRates.csv', 'w',encoding='utf-8')

genRateFile(parse_html2txt,fp1)
#重置记录数和页数
count = 0
page_count = -1
genRateFile(parse_html2csv,fp2)
