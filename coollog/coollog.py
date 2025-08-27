import datetime

class CoolLog:
    _DEFAULT_KEY = "\033["
    _LOG_FILE = "logs.txt"

    _COLORS = {
        "ERROR": "31",    
        "WARNING": "33",  
        "SUCCESS": "32",  
        "INFO": "34",     
        "DEBUG": "35",    
        "CRITICAL": "41", 
    }

    @staticmethod
    def _write_log(level: str, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = CoolLog._COLORS.get(level, "0")

        label = f"{CoolLog._DEFAULT_KEY}2;{color}m[{level}-{timestamp}]{CoolLog._DEFAULT_KEY}0m"

        text = f"{CoolLog._DEFAULT_KEY}1;{color}m{message}{CoolLog._DEFAULT_KEY}0m"

        print(f"{label} {text}")

        file_text = f"[{level}-{timestamp}] {message}\n"
        with open(CoolLog._LOG_FILE, "a", encoding="utf-8") as f:
            f.write(file_text)

    @staticmethod
    def error(message: str):
        CoolLog._write_log("ERROR", message)

    @staticmethod
    def warning(message: str):
        CoolLog._write_log("WARNING", message)

    @staticmethod
    def success(message: str):
        CoolLog._write_log("SUCCESS", message)

    @staticmethod
    def info(message: str):
        CoolLog._write_log("INFO", message)

    @staticmethod
    def debug(message: str):
        CoolLog._write_log("DEBUG", message)

    @staticmethod
    def critical(message: str):
        CoolLog._write_log("CRITICAL", message)
