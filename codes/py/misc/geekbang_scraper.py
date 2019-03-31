#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import datetime
import hashlib
import jinja2
import json
import os
import pymongo
import re
import requests

client = pymongo.MongoClient()
table = client['geekbang']['cache']

style_string = """
<style type="text/css">html {
    font-family: Georgia, "Microsoft Yahei", "WenQuanYi Micro Hei";
}

/* pre { */
/*     background-color: #eee; */
/*     box-shadow: 5px 5px 5px #888; */
/*     border: none; */
/*     padding: 5pt; */
/*     margin-bottom: 14pt; */
/*     color: black; */
/*     padding: 12pt; */
/*     font-family: Consolas; */
/*     font-size: 95%; */
/*     overflow: auto; */
/* } */

.title  { /* text-align: center; */
          margin-bottom: 1em; }
.subtitle { /* text-align: center; */
            font-size: medium;
            font-weight: bold;
            margin-top:0; }
.todo   { font-family: monospace; color: red; }
.done   { font-family: monospace; color: green; }
.priority { font-family: monospace; color: orange; }
.tag    { background-color: #eee; font-family: monospace;
          padding: 2px; font-size: 80%; font-weight: normal; }
.timestamp { color: #bebebe; }
.timestamp-kwd { color: #5f9ea0; }
.org-right  { margin-left: auto; margin-right: 0px;  text-align: right; }
.org-left   { margin-left: 0px;  margin-right: auto; text-align: left; }
.org-center { margin-left: auto; margin-right: auto; text-align: center; }
.org-ul { padding-left: 10px; }
.org-ol { padding-left: 20px; }
ul { padding-left: 10px; }
ol { padding-left: 20px; }

.underline { text-decoration: underline; }
#postamble p, #preamble p { font-size: 90%; margin: .2em; }
p.verse { margin-left: 3%; }
pre {
    border: 1px solid #ccc;
    box-shadow: 3px 3px 3px #eee;
    padding: 8pt;
    font-family: monospace;
    overflow: auto;
    margin: 1.2em;
}
pre.src {
    position: relative;
    overflow: visible;
    padding-top: 1.2em;
}
pre.src:before {
    display: none;
    position: absolute;
    background-color: white;
    top: -10px;
    right: 10px;
    padding: 3px;
    border: 1px solid black;
}
pre.src:hover:before { display: inline;}
pre.src-sh:before    { content: 'sh'; }
pre.src-bash:before  { content: 'sh'; }
pre.src-emacs-lisp:before { content: 'Emacs Lisp'; }
pre.src-R:before     { content: 'R'; }
pre.src-perl:before  { content: 'Perl'; }
pre.src-java:before  { content: 'Java'; }
pre.src-sql:before   { content: 'SQL'; }

table { border-collapse:collapse; }
caption.t-above { caption-side: top; }
caption.t-bottom { caption-side: bottom; }
td, th { vertical-align:top;  }
th.org-right  { text-align: center;  }
th.org-left   { text-align: center;   }
th.org-center { text-align: center; }
td.org-right  { text-align: right;  }
td.org-left   { text-align: left;   }
td.org-center { text-align: center; }
dt { font-weight: bold; }
.footpara { display: inline; }
.footdef  { margin-bottom: 1em; }
.figure { padding: 1em; }
.figure p { /* text-align: center; */ }
.inlinetask {
    padding: 10px;
    border: 2px solid gray;
    margin: 10px;
    background: #ffffcc;
}
#org-div-home-and-up
{ text-align: right; font-size: 70%; white-space: nowrap; }
textarea { overflow-x: auto; }
.linenr { font-size: smaller }
.code-highlighted { background-color: #ffff00; }
.org-info-js_info-navigation { border-style: none; }
#org-info-js_console-label
{ font-size: 10px; font-weight: bold; white-space: nowrap; }
.org-info-js_search-highlight
{ background-color: #ffff00; color: #000000; font-weight: bold; }

/* http://www.yinwang.org/main.css */

body {
    /* font-family:"lucida grande", "lucida sans unicode", lucida, helvetica, "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif; */
    font-size: 18px;
    margin: 5% 5% 5% 5%;
    padding: 2% 5% 5% 5%;
    width: 80%;
    line-height: 150%;
    border: 1px solid LightGrey;
}

H1 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
}

H2 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
    margin-bottom: 60px;
    margin-bottom: 40px;
    padding: 5px;
    border-bottom: 2px LightGrey solid;
    width: 98%;
    line-height: 150%;
    color: #666666;
}


H3 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
    margin-top: 40px;
    margin-bottom: 30px;
    border-bottom: 1px LightGrey solid;
    width: 98%;
    line-height: 150%;
    color: #666666;
}


H4 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
    margin-top: 40px;
    margin-bottom: 30px;
    border-bottom: 1px LightGrey solid;
    width: 98%;
    line-height: 150%;
    color: #666666;
}


li {
    margin-left: 10px;
}


blockquote {
    border-left: 4px lightgrey solid;
    padding-left: 5px;
    margin-left: 20px;
}


pre {
    font-family: Inconsolata, Consolas, "DEJA VU SANS MONO", "DROID SANS MONO", Proggy, monospace;
    font-size: 75%;
    border: solid 1px lightgrey;
    background-color: Ivory;
    padding: 5px;
    line-height: 130%;
    margin-left: 10px;
    width: 95%;
}


code {
    font-family: Inconsolata, Consolas, "DEJA VU SANS MONO", "DROID SANS MONO", Proggy, monospace;
    font-size: 90%;
}


a {
    text-decoration: none;
    # cursor: crosshair;
    border-bottom: 1px dashed Red;
    padding: 1px;
    # color: black;
}


a:hover {
	background-color: LightGrey;
}


img {
    box-shadow: 0 0 10px #555;
    border-radius: 6px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    margin-bottom: 10px;
    -webkit-box-shadow: 0 0 10px #555;
    width: 100%;
    max-width: 600px;
}

img.displayed {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

#table-of-contents {
    border-bottom: 2px LightGrey solid;
}</style>
"""


def get_sha1_key(s):
    return hashlib.sha1(s.encode('utf8')).hexdigest()


def parse_response(doc):
    data = doc['data']
    title = data['article_title']
    content = data['article_content']
    return title, content


sp_string = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="viewport" content="width=device-width, initial-scale=1" />
<title>{{ single_page_title }}</title>
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="maypeppa" />
{{ style_string }}
</head>

<body>
<div id="content">
<h1 class="title">{{ single_page_title }}</h1>
<div id="table-of-contents">
<h2>Table of Contents</h2>
<ul>
{% for x in items %}
<li><a href="#anchor{{ x.idx }}">{{ x.title }}</a></li>
{% endfor %}
</ul>
</div>

{% for x in items %}
<div class="outline-2">
<h2 id="anchor{{ x.idx }}">{{ x.title }}<a href="#table-of-contents">#</a></h2>
<div class="outline-text-2">
{{ x.html }}
</div>
</div>
{% endfor %}

</div>
</body>
</html>
"""

index_string = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="viewport" content="width=device-width, initial-scale=1" />
<title>{{ index_page_title }}</title>
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="maypeppa" />
{{ style_string }}
</head>

<body>
<div id="content">
<h1 class="title">{{ index_page_title }}</h1>
<p><a href="sp.html">Single Page Document</a></p>
<ul>
{% for x in items %}
<li><a href="{{ x.href }}">{{ x.title }}</a></li>
{% endfor %}
</ul>
</div>
</body>
</html>
"""

page_string = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="viewport" content="width=device-width, initial-scale=1" />
<title>{{ title }}</title>
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="maypeppa" />
{{ style_string }}
</head>

<body>

<div class="outline-2">
<h2>{{ title }}</h2>
<div class="outline-text-2">
{{ html }}
</div>
</div>

</body>
</html>
"""


def create_session(cookie):
    sample_headers = """Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7
Connection: keep-alive
Content-Type: application/json
Host: time.geekbang.org
Origin: https://time.geekbang.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"""

    sample_headers = sample_headers.split('\n')
    ss = requests.Session()
    headers = {}
    for sh in sample_headers:
        k, v = sh.split(': ', maxsplit=1)
        headers[k] = v
    headers['Cookie'] = cookie
    ss.headers = headers
    return ss


def get_article(ss, article_id):
    print('get article of {}'.format(article_id))
    r = table.find_one({'_id': article_id})
    if not r:
        url = 'https://time.geekbang.org/serv/v1/article'
        payload = {
            'id': str(article_id),
            'include_neighbors': True
        }
        r = ss.post(url, data=json.dumps(payload))
        data = r.json()
        value = json.dumps(data)
        table.update_one({'_id': article_id}, {'$set': {'value': value}}, upsert=True)
    else:
        value = r['value']
    return json.loads(value)


def make_page(docs):
    items = []
    dup = set()
    os.makedirs('html', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    template = jinja2.Template(page_string)

    for doc in docs:
        title, html = parse_response(doc)
        if title in dup: continue
        dup.add(title)
        title = title.replace('/', '')
        path = "html/{}.html".format(title)
        with open(path, 'w') as fh:
            output = template.render(style_string=style_string,
                                     title=title,
                                     html=html)
            output = output.replace('images/', '../images/')
            fh.write(output)
        items.append((title, html, path))
    items.sort(key=lambda x: x[0])

    items = [{'title': x[0], 'html': x[1], 'idx': idx, 'href': x[2]} for (idx, x) in enumerate(items)]

    template = jinja2.Template(sp_string)
    with open('sp.html', 'w') as fh:
        output = template.render(items=items, style_string=style_string,
                                 single_page_title="Single Page Document")
        fh.write(output)

    template = jinja2.Template(index_string)
    with open('index.html', 'w') as fh:
        output = template.render(items=items, style_string=style_string,
                                 index_page_title="Index Page Document")
        fh.write(output)


evernote_template_string = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export3.dtd">
<en-export export-date="{{ export_date }}" application="Evernote" version="Evernote Mac 7.2.1 (456793)">
{% for x in notes %}
<note>
<title>{{ x.title }}</title>
<content>
<![CDATA[<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note>{{ x.html_data }}</en-note>]]>
</content>
<created>{{ x.created_date }}</created>
<updated>{{ x.updated_date }}</updated>
<note-attributes>
  <author>{{ x.author }}</author>
  <source>python.script</source>
  <reminder-order>0</reminder-order>
</note-attributes>
</note>
{% endfor %}
</en-export>"""


# def make_evernote_notebook(name, docs):
#     now = datetime.datetime.now()
#     date_now = now.strftime('%Y%m%dT%H%M%SZ')
#     ctx = {
#         'export_date': date_now
#     }
#     notes = []
#     for doc in docs:
#         title, html = parse_response(doc)
#         note = {
#             'created_date': date_now,
#             'updated_date': date_now,
#             'author': '章炎',
#             'title': title,
#             'html_data': html
#         }
#         notes.append(note)
#     ctx['notes'] = notes
#     template = jinja2.Template(evernote_template_string)
#     output = template.render(**ctx)
#     with open(name + '.enex', 'w') as fh:
#         fh.write(output)
#

def get_docs(cookie, article_ids):
    ss = create_session(cookie)
    docs = []
    for article_id in article_ids:
        doc = get_article(ss, article_id)
        docs.append(doc)
    return docs


def run(cookie, org_file):
    article_ids = []
    reobj = re.compile(r'column/article/(?P<article_id>\d+)')
    with open(org_file) as fh:
        for x in fh:
            if x.startswith('#+title:'):
                ss = x.split(' ')
                output_path = ss[1]
                continue

            m = reobj.search(x)
            if m:
                x = int(m.group('article_id'))
                article_ids.append(x)

    docs = get_docs(cookie, article_ids)
    pwd = os.getcwd()
    os.makedirs(output_path, exist_ok=True)
    os.chdir(output_path)
    make_page(docs)
    os.chdir(pwd)
    # make_evernote_notebook(output_path, docs)


#
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--cookie', action='store')
#     # # org_file see geekbang_index2org
#     # parser.add_argument('--org-file', action='store')
#     args = parser.parse_args()
#     run(args.cookie, args.org_file)
#
#
# if __name__ == '__main__':
#     main()


def main():
    import geekbang_scraper_conf as conf
    cookie = conf.cookie
    org_files = conf.org_files
    for org_file in org_files:
        print(org_file)
        run(cookie, org_file)


if __name__ == '__main__':
    main()
