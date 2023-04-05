import requests

url = 'http://127.0.0.1:8080/upload'
#modificare nome e percorso del file che si vuole caricare
filenamepath = 'file.txt'
files = {'ufile': open(filenamepath, 'rb')}

r = requests.post(url, files=files)

print(r)
print(r.text)