#coding:utf-8
"""
HTML输出器
"""

class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]


    def collect_data(self,data):
        """
        收集数据
        :param data:
        :return:
        """
        if data is None:
            return
        self.datas.append(data)
        
        
    def output_html(self):
        """
        将收集结果输出HTML页面
        :return:
        """
        fout=open('output.html','w')
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type'content='text/html;charset=utf-8'>")
        fout.write("<link rel='Stylesheet' href='style.css'/>")
        fout.write("<link rel='Stylesheet' href='base.css'/>")
        fout.write("</head>")
        fout.write("<body>")
        fout.writelines('<h1>Python爬虫爬取百度百科</h1>')
        fout.write("<table>")
        fout.write("<tr class='td_th'><th>名称</th> <th>简介内容</th>  </tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")	
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()