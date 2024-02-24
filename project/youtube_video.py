from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

yt = YouTube("https://www.youtube.com/watch?v=rDYbpmRCZHk")

# print(yt.title)
# print(yt.streams)

# for i in yt.streams:
#     print(type(i))
#     print(i)

for i in yt.streams.filter(file_extension="mp4"):
    # print(type(i))
    print(i)
down = input("What itag to download?: ")
to_down = yt.streams.get_by_itag(int(down))
to_down.download()

