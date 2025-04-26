from pytubefix import YouTube
import os

link = 'https://www.youtube.com/watch?v=RHvM6vgCXhk&list=RDRHvM6vgCXhk&start_radio=1&ab_channel=zahoz75'
download = YouTube(link)

ys = download.streams.get_highest_resolution()

caminho_download = os.path.join(os.path.dirname(__file__))
print(caminho_download)


ys.download(output_path=caminho_download)
