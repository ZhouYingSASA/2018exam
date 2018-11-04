# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask_cors import CORS

def get_url():
#    gurl = input()
    return "https://blog.snowstar.org/"
    pass

def savehtml(file_name, file_data):
    with open('/templates/'+ file_name + '.html', 'w') as fi:
        fi.write(file_data)

def sercha(serchname):
    return str('https://blog.snowstar.org/?' + serchname)

def gettext(aimurl):
    with request.urlopen(aimurl) as f:
        data = f.read()
        mainsoup = BeautifulSoup(data)
        i=0
        title=[]
        time=[]
        summery=[]
        for s in mainsoup.findAll('h2'):#标题
            title.append(str(s))
        i=0
        for s in mainsoup.findAll('span'):#发布时间
            i = i + 1
            if 'date' not in str(s):
                continue
            time.append(str(s))
        i=0
        for s in mainsoup.findAll('p'):#摘要
            i=i+1
            if 'button' in str(s):
                continue
            summery.append(str(s))
        contain = []
        for ti in range(0,i):
            contain.append(title[ti] + time[ti] + summery[ti])
        # 爬虫所爬内容已存入contain

    #    savehtml(str(hash(get_url())),somth)
    #    #open无法存储templates
    #    print(somth)

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/serch/')
def ser(txt):
    return render_template("serchfile.html")

@app.route('/')
def sor():
    return """<h1>Sorry, I'm stuck by outputting...</h1><button action="/serch">QAQ</button>"""

if __name__ == "__main__":
    app.run()