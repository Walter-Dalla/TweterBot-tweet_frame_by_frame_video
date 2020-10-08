from getFrames import getFramesAndTweetThen
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


IMAGES_PATH = os.getenv("IMAGES_PATH")
VIDEO_URL = os.getenv("VIDEO_URL")
FILE_NAME = os.getenv("FILE_NAME")
VIDEO_NAME = os.getenv("VIDEO_NAME")
TIMER = os.getenv("TIMER")


async def main():

    print("So lets start...")
    print(IMAGES_PATH, FILE_NAME)

    imagesFolder = IMAGES_PATH+FILE_NAME

    try:
        os.mkdir(IMAGES_PATH)
        os.mkdir(imagesFolder)
    except OSError:
        print("Creation of the directory %s failed" % imagesFolder)

    getFramesAndTweetThen(VIDEO_URL, imagesFolder, VIDEO_NAME, TIMER)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
