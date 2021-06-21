from pytube import YouTube
url = input("HOLA BIENVENIDO AL YOUTUBE DOWNLOADER MP4 BY @MARKUS ESPERO QUE LO DISFRUTES ENGANCHA AQUI TU URL I DESCARGA EL VIDEO :) URL: ")
yt = YouTube(url)
yt.title
yt.author
quality = input("HD 22(hd) or 18 (low quality): ")
yt.streams.get_by_itag(quality).download(r"C:\Users\Marc\Desktop\yt download py")