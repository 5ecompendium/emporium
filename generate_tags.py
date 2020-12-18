#!/usr/bin/env python

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.

Run this to generate the tag pages before pushing to Github Pages (since jekyll-archive isn't yet whitelisted).
'''

import glob
import os
import re

post_dir = '_items/'
tag_dir = '_tags/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            stripped_line = re.sub('[\[\]]', '', line.strip())          # -> "tags: A, B, C"
            current_tags = stripped_line.split(':')                     # -> ["tags", " A, B, C"]
            if current_tags[0] == 'tags':                               #
                current_tags = current_tags[1].strip().split(',')       # -> ["A", " B", "C"]
                current_tags = [tag.strip() for tag in current_tags]    # -> ["A,", "B", "C"]
                total_tags.extend(current_tags)
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tag\nname: \"' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())