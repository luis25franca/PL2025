import re

markdown= input()

if markdown == "" :
    with open("input.txt", "r") as file:
        markdown = file.read()

markdown = re.sub(r'^### (.+)', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
markdown = re.sub(r'^## (.+)', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
markdown = re.sub(r'^# (.+)', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)

markdown = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', markdown, flags=re.MULTILINE)
markdown = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', markdown, flags=re.MULTILINE)

markdown = re.sub(r'(?m)^\d+\. (.+)', r'<ol>\n<li>\1</li>\n</ol>', markdown)
markdown = re.sub(r'\n(</ol>\n<ol>)', '', markdown)  


markdown = re.sub(r'\!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', markdown)
markdown = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown)

print(markdown)

