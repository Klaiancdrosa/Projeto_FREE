from pytube import YouTube
from pywebio.input import input, radio
from pywebio.output import put_text
import os

def video_download():
    option = radio("O que deseja fazer?", options=["Baixar Video", "Converter o Video em Musica"])

    if option == "Baixar Video":
        video_link = input("Informe o link do video: ")
        if video_link.startswith("https://"):
            put_text("Fazendo o download do vídeo...").style('color: red; font-size: 20px')
            yt = YouTube(video_link)
            stream = yt.streams.get_highest_resolution()
            download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            stream.download(download_path)
            put_text("Vídeo baixado com sucesso!").style('color: blue; font-size: 20px')
        else:
            put_text("O link do vídeo deve começar com 'https://'.")

    elif option == "Converter o Video em Musica":
        video_link = input("Informe o link do vídeo para o áudio: ")
        if video_link.startswith("https://"):
            put_text("Fazendo o download do áudio...").style('color: red; font-size: 20px')
            yt = YouTube(video_link)
            stream = yt.streams.filter(only_audio=True).first()
            download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            stream.download(download_path)
            put_text("Áudio baixado com sucesso!").style('color: blue; font-size: 20px')
        else:
            put_text("O link da áudio deve começar com 'https://'.")

if __name__ == "__main__":
    video_download()
