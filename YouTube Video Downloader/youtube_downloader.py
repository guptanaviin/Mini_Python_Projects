from pytube import YouTube

link = "https://www.youtube.com/watch?v=Omlx6z1NIBA&list=RDOmlx6z1NIBA&start_radio=1"
yt_1 = YouTube(link)

#print(yt_1.title)
#print(yt_1.thumbnail_url)

#video_download  = yt_1.streams.all()                      #All video and Audio
video_download = yt_1.streams.filter(only_audio=True)
vid = list(enumerate(video_download))
for i in vid:
    print(i)
print()
streaming = int(input("Enter : "))
video_download[streaming].download()
print("Sucessfully")