from pytube import YouTube

url = input('Please enter youtube video url \n')
youtube = YouTube(url)

formates = youtube.streams.all()
video = list(enumerate(formates))

for i in video:
    print(i)
option = int(input('Choose the formate \n'))

d = formates[option]
d.download('videos')

print('\n video downloaded successfully')