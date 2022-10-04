from pytube import YouTube

#ask for the link from user
link = input("Write youtube video url")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
print("Keywords of video: ",yt.keywords)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()

#Finishing download
print("Downloaded!")
