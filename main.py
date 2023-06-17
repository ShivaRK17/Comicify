import cv2
import extractframes
import srtsplit
import downloadvideo
import youtubesrt

youtube_link = 'https://www.youtube.com/watch?v=yoZLUnaC3JE'

def convertVideoToComic(youtube_link):
    youtubesrt.genSubfromYoutube(youtube_link)
    downloadvideo.Download(youtube_link)

    subfile = 'videosub.srt'
    video_file = 'videoclip.mp4'

    startstr = '00:00'
    endstr = '00:00'

    dialogues = srtsplit.subtitleSplit(subfile)
    count = 0
    for frames in dialogues:
        startstr = frames[1][3:8]
        if(int(startstr[3:])-int(endstr[3:])>3):
            # print(endstr,'->',startstr)
            count = extractframes.extract_frame(video_file,endstr,startstr,count)
        endstr = frames[1][20:25]
        # print(startstr,'->',endstr,frames[2])
        count = extractframes.extract_frame(video_file,startstr,endstr,count,len(frames[2])+1,frames[2])
    startstr = endstr
    video = cv2.VideoCapture(video_file)
    endstr = int(video.get(cv2.CAP_PROP_POS_FRAMES))
    endstr = "{:02d}:{:02d}".format(int(endstr // 60), int(endstr % 60))
    extractframes.extract_frame(video_file,startstr,endstr,count)

if __name__=="__main__":
    try:
        convertVideoToComic(youtube_link)
    except Exception as err:
        print(err)