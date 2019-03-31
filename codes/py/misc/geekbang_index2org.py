#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import argparse
from bs4 import BeautifulSoup
from jinja2 import Template

template = Template(
    """#+title: 极客时间|{{ org_title }} 文章目录
#+options: num:nil

{% for doc in docs %}
** [[https://time.geekbang.org{{ doc.url }}][{{ doc.title }}]]

{{ doc.desc }}

{% endfor %}
"""
)


def run(html_path, org_title, org_path):
    with open(html_path) as fh:
        html_data = fh.read()
        bs = BeautifulSoup(html_data, 'lxml')

    more = [x.attrs['href'] for x in bs.select('.article-item-more > a')]
    title = [x.text for x in bs.select('.article-item-title')]
    desc = [x.text for x in bs.select('.article-item-desc')]
    docs = [{'url': x[0], 'title': x[1], 'desc': x[2]} for x in zip(more, title, desc)]
    docs = docs[::-1]
    text = template.render(org_title=org_title, docs=docs)
    with open(org_path, 'w') as fh:
        fh.write(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--html-path', action='store')
    parser.add_argument('--org-title', action='store')
    parser.add_argument('--org-path', action='store')
    args = parser.parse_args()
    html_path = args.html_path
    org_title = args.org_title
    org_path = args.org_path
    run(html_path, org_title, org_path)


if __name__ == '__main__':
    main()
