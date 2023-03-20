from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLjVLYmrlmjGdBG50ND8FY-2XygL3VH0xk")
print(f'Downloading : {playlist.title}')

for video in playlist.videos:
    video.streams.first().download()
    


