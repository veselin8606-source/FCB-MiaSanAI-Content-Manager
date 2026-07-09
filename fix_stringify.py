import re

with open('server.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('JSON.stringify(error)', 'String(error)')
content = content.replace('JSON.stringify(err)', 'String(err)')

with open('server.ts', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced JSON.stringify")
