# -*- coding: utf-8 -*-
__version__ = '0.0.1'

import sys


class ProgressBar(object):
    """docstring for ProgressBar"""
    def __init__(self, done, totalSize, filelike=sys.stdout):
        self.done = done
        self.totalSize = totalSize
        self.filelike = filelike
        self.progressBarWidth = 40
        self.progressBarChars = ['☐', '☒']
        # self.percent = float(done) / float(totalSize)

        self.progress(done)

    def progress(self, done):
        self.done += done
        self.percent = float(self.done) / float(self.totalSize)
        if self.percent >= 1:
            self.filelike.write("Done\n")
            self.filelike.flush()
            return None
        # update the bar
        output = ('['
            + (self.progressBarChars[1] * int(round(self.percent * self.progressBarWidth)))
            + (self.progressBarChars[0]
                * int(round(self.progressBarWidth - self.percent * self.progressBarWidth)))
            + ']'
            + str(int(self.percent * 100))
            + '%')
        self.filelike.write(output)
        self.filelike.flush()
        # return to start of line
        self.filelike.write("\b" * (len(output)))
        self.filelike.flush()
