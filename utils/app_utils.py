# import the necessary packages
from threading import Thread
import datetime
import cv2

class FPS:
    def __init__(self):
        # store the start time, end time, and total number of frames
        # that were examined between the start and end intervals
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        # start the timer
        self._start = datetime.datetime.now()
        return self
    
    def stop(self):
        # stop the timer
        self._end = datetime.datetime.now()

    def update(self):
        # increment the total number of frames examined during the
        # start and end intervals
        self._numFrames += 1

    def elapsed(self):
        # return the total number of seconds between the start and
        # end interval
        return (self._end - self._start).total_seconds()

    def fps(self):
        # compute the (approximate) frames per second
        return self._numFrames / self.elapsed()

    
class WebcamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src + cv2.CAP_V4L2)

        retval = self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        print('Set return: {}'.format(retval))
        retval = self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        print('Set return: {}'.format(retval))
        retval = self.stream.set(cv2.CAP_PROP_FPS, 30)
        print('Set return: {}'.format(retval))
        retval = self.stream.set(cv2.CAP_PROP_CONVERT_RGB, 1)
        print('Set return: {}'.format(retval))
        retval = self.stream.set(cv2.CAP_PROP_AUTOFOCUS, 1)
        print('Set return: {}'.format(retval))

        retval = self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        print('Get return: {}'.format(retval))
        retval = self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Get return: {}'.format(retval))
        retval = self.stream.get(cv2.CAP_PROP_FPS)
        print('Get return: {}'.format(retval))
        retval = self.stream.get(cv2.CAP_PROP_CONVERT_RGB)
        print('Get return: {}'.format(retval))
        retval = self.stream.get(cv2.CAP_PROP_AUTOFOCUS)
        print('Get return: {}'.format(retval))

        (self.grabbed, self.frame) = self.stream.read()
        
        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self
 
    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return
                    
            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
 
    def read(self):
        # return the frame most recently read
        return self.grabbed, self.frame
 
    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    def getWidth(self):
        # Get the width of the frames
        return int(self.stream.get(cv2.CAP_PROP_FRAME_WIDTH))

    def getHeight(self):
        # Get the height of the frames
        return int(self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def getFPS(self):
        # Get the frame rate of the frames
        return int(self.stream.get(cv2.CAP_PROP_FPS))

    def isOpen(self):
        # Get the frame rate of the frames
        return self.stream.isOpened()

    def setFramePosition(self, framePos):
        self.stream.set(cv2.CAP_PROP_POS_FRAMES, framePos)

    def getFramePosition(self):
        return int(self.stream.get(cv2.CAP_PROP_POS_FRAMES))

    def getFrameCount(self):
        return int(self.stream.get(cv2.CAP_PROP_FRAME_COUNT))
