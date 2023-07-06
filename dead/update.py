import os 
path = "."
filename = "index.html"

with open(filename,'w',-1,'utf-8') as html:
    html.write("""<!DOCTYPE html>
<head>
    <title>华中师大一附中社团联合会</title>
</head>
<body>
    <ul>""")
    for file in os.listdir(path):
        html.write("\n\t\t<li><a href=\"./"+file+"\">"+file[:-4]+"</a></li>")
    html.write("""
    </ul>
</body>""")
