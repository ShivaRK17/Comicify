import cv2,os
import img2pdf
from natsort import natsorted
def midtimediff(start_time, end_time):
    start_minutes, start_seconds = map(int, start_time.split(":"))
    end_minutes, end_seconds = map(int, end_time.split(":"))

    start_total_seconds = start_minutes * 60 + start_seconds
    end_total_seconds = end_minutes * 60 + end_seconds

    total_seconds = (start_total_seconds + end_total_seconds) / 2
    timestamp_minutes, timestamp_seconds = divmod(total_seconds, 60)
    timestamp = "{:02d}:{:02d}".format(int(timestamp_minutes), int(timestamp_seconds))
    return timestamp

def timediffsec(start_time, end_time):
    start_minutes, start_seconds = map(int, start_time.split(":"))
    end_minutes, end_seconds = map(int, end_time.split(":"))

    # Convert minutes and seconds to seconds for easier calculation
    start_total_seconds = start_minutes * 60 + start_seconds
    end_total_seconds = end_minutes * 60 + end_seconds

    # Calculate the time difference in seconds
    time_difference = abs(start_total_seconds - end_total_seconds)

    return time_difference

def frametommss(video):
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    total_seconds = frame_count / frame_rate
    # Convert to minutes and seconds
    minutes, seconds = divmod(total_seconds, 60)
    # Format the time as "mm:ss"
    time_formatted = "{:02d}:{:02d}".format(int(minutes), int(seconds))
    return time_formatted



def converttopdf(dirname):
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    imgs = natsorted(imgs)
    with open("output.pdf","wb") as f:
        f.write(img2pdf.convert(imgs))

def deletefiles(dirname):
    for filename in os.listdir(dirname):
        os.remove(os.path.join(dirname,filename))
