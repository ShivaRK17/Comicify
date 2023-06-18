import converttocomic

youtube_link = 'https://www.youtube.com/watch?v=Pgwaj1CSkN8'

if __name__=="__main__":
    try:
        converttocomic.convertVideoToComic(youtube_link)
    except Exception as err:
        print(err)
