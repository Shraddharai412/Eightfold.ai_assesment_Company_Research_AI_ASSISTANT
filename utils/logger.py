import datetime
import os

class Logger:
    """
    Lightweight file + console logger for debugging and tracking errors.
    """

    LOG_FILE = "app.log"

    def __init__(self):
        self.log_path = os.path.join(os.getcwd(), self.LOG_FILE)

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message: str):
        """Write a timestamped log message to file + console."""
        entry = f"[{self._timestamp()}] {message}"
        print(entry)

        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

    def error(self, message: str):
        """Shortcut for logging errors."""
        self.log(f"ERROR: {message}")

    def info(self, message: str):
        """Shortcut for info logs."""
        self.log(f"INFO: {message}")
