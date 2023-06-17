from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename='videoclip.mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")