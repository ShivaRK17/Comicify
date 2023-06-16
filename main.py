import cv2
import extractframes
import srtsplit
import downloadvideo
import youtubesrt

youtube_link = 'https://www.youtube.com/watch?v=yWmeBoVXwrE'

downloadvideo.Download(youtube_link)
youtubesrt.genSubfromYoutube(youtube_link)

subfile = 'friendssub.srt'
video_file = 'friendsclip.mp4'

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