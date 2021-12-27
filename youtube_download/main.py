import csv
from pytube import YouTube

with open('youtube_link.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for link in spamreader:     
        yt = YouTube(link[0])
        #print(yt.streams.filter(progressive=True, file_extension='mp4').desc())
        #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="patrick")#,filename = f"{idx}.mp4")
        yt.streams.get_highest_resolution().download(output_path="music")#,filename = f"{idx}.mp4")
