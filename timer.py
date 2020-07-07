import time
class Timer:
    def __init__(self, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger
    def start(self, label="task"):
        self.label = label
        self.t1 = time.time()
    def stop(self):
        self.t2 = time.time()
        print("Time lapsed for %s: %s" % (self.label, self.t2-self.t1))