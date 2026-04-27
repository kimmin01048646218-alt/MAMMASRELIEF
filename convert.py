import base64
import os

with open('daily.png', 'rb') as f:
    d_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('family.png', 'rb') as f:
    f_b64 = base64.b64encode(f.read()).decode('utf-8')

filename = '마마스 릴리프.html'
with open(filename, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("url('cof3.png')", f"url('data:image/png;base64,{d_b64}')")
html = html.replace("url('cof4.png')", f"url('data:image/png;base64,{f_b64}')")

with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)

print("Success")
