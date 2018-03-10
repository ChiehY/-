#coding:utf-8
"""
URL管理器
"""
class UrlManager(object):
    def __init__(self):
        #待爬取url集合
        self.new_urls=set()
        #已爬取url集合
        self.old_urls=set()

    def add_new_url(self,url):
        """
        添加新的待爬取的url
        :param url:
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            #若为新的url,则添加进待爬取的url集合中
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        """
        批量添加新的待爬取的url集合
        :param urls:
        :return:
        """
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def has_new_url(self):
        """
        检测待爬取集合是否为空
        :return:
        """
        return len(self.new_urls)!=0


    def get_new_url(self):
        """
        获取要爬取的url
        :return:
        """
        #获取url并从集合中去除该url
        new_url=self.new_urls.pop()
        #将获取的url添加进已爬取的url中
        self.old_urls.add(new_url)
        return new_url