import os

class Chesk_file:
    def chesk(self)->bool:
        path = "log.txt"
        return os.path.exists(path)