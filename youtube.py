from pytube import YouTube
link = input('enter link\n')
res = input('enter quality 480/720\n')

YouTube(f'{link}').streams.filter(progressive=True, file_extension='mp4', res=f"{res}p").first().download()
print("download is done")
title=YouTube(f'{link}').title
print(f"title of video : {title}")
channel = YouTube(f'{link}').channel_url
print(f"url of channel : {channel}")
print(f"url of video: {link}")
print(f"quality of video: {res}p")
views=YouTube(f'{link}').views
print(f"views of video: {views}")
des = YouTube(f'{link}').description
print(f"the local link of the video is {title}.mp4")
print(f"description of video : {des}")


