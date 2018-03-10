#coding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        """
        获取该页面所有符合检验规则的url
        :param page_url:
        :param soup:
        :return:
        """
        #新的待爬取的url集合
        new_urls=set()
        #获取所有符合检验规则的url
        links=soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            new_url=link['href']
            #将相对路径的url拼接成绝对路径url
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        """
        整合页面数据
        :param page_url:
        :param soup:
        :return:
        """
        #该页面整合的数据
        res_data={}
        #url
        res_data['url']=page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #获取爬取页面的标题
        title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']=title_node.get_text()
        
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        #获取爬取页面的概要
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()
        return res_data
    def parse(self,page_url,html_cont):
        """
        解析该页面
        :param page_url:
        :param html_cont:
        :return:
        """
        if page_url is None or html_cont is None:
            return
        
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data