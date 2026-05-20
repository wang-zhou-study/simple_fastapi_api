LOG_FILE = "logs.txt"


def read_logs():

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.readlines()

        return [log.strip() for log in logs]

    except FileNotFoundError:
        return []


def write_log(log_text):

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_text + "\n")