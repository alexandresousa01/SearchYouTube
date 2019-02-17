from __future__ import unicode_literals

import requests
import json
import youtube_dl


#Configuração do video, precisa pesquisar mais infos
ydl_opts = {}

def download_youtube(videoId):

    URL = 'https://www.youtube.com/watch?v=' + videoId
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])


response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=12615&q=roubo+a+m%C3%A3o+armada&key=[PutYourKey]")

# Convert response to dict
dicionario = json.loads(response.content.decode("utf-8"))

# Print the status code of the response.
print("Status code: ", response.status_code)


arquivo = open('URLs.txt', 'w')


for k,v in dicionario['pageInfo'].items():
    newline = str(k) + ': ' + str(v) + '\n'
    arquivo.writelines(newline)


lista = dicionario['items']

for v in lista:
    videoId = str(v['id']['videoId'])
    
    download_youtube(videoId)
    
    arquivo.writelines(videoId+'\n')

arquivo.close()
