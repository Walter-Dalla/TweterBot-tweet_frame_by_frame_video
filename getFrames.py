import time
import pafy
import cv2

from twitter import TwitterApi


def getFramesAndTweetThen(url, imagesFolder, videoName, TIMER):

    # get video from youtube
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")

    vidcap = cv2.VideoCapture(best.url)
    success, image = vidcap.read()
    count = 1

    while success:

        # save frame as JPEG file
        cv2.imwrite("%s/frame%d.jpg" % (imagesFolder, count), image)
        success, image = vidcap.read()

        print("Posting frame %d" % (count))

        # Tweet image and description
        TwitterApi("%s/frame%d.jpg" % (imagesFolder, count),
                   'Frame %d do video %s (postado a cada %ds)' % (count, videoName, int(TIMER)))

        count += 1

        time.sleep(int(TIMER))
