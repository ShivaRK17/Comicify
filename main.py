import converttocomic

youtube_link = 'https://www.youtube.com/watch?v=UYce-bq89eI'

if __name__=="__main__":
    try:
        converttocomic.convertVideoToComic(youtube_link)
    except Exception as err:
        print(err)
