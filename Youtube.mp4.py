from pytube import YouTube

url = 'youtube video URL'
my_video = YouTube(url)

#don't change anything below

print("Video Title") 
print(my_video.title)

print("Tumbnail Image") 
print(my_video.thumbnail_url)

print("Download video") 
for stream in my_video.streams:
    print(stream)

my_video = my_video.streams.get_highest_resolution()

my_video.download()
