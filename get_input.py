import subprocess
import queue
import threading
import sys

class GetEvent(object):

    def __init__(self):
        self.process = subprocess.Popen(['adb', 'shell', 'getevent'],
                                                stdout=subprocess.PIPE)
        self.thread = threading.Thread(target=lambda: self.process)
        self.queue = queue.Queue()

    def run(self):
        self.thread.start()

    def get_output(self):
        try:
            for line in iter(self.process.stdout.readline, ''):
                self.queue.put(line)
                self.print_output()
        except KeyboardInterrupt:
            self.stop()

    def print_output(self):
        print('printing queue')
        while True:
            try:
                output = self.queue.get_nowait()
                print(output)
                sys.stdout.flush()
            except queue.Empty:
                break

    def stop(self):
        self.process.terminate()
        print('Terminated')
        self.thread.join()
        print('Finished')


if __name__ == '__main__':
    get_event = GetEvent()
    get_event.run()
    get_event.get_output()
