class FileIO:

    def __init__(self, file_path, mode = "a+"):
        self.file_path = file_path
        self.file = open(file_path, mode)

    def read(self):
        return self.file.read()

    def write(self, data):
        self.file.write(data)

    def append(self, data):
        if isinstance(data, list):
            self.file.write("\n".join(data) + "\n")
        else:
            self.file.write(data + "\n")

    def read_last_line(self):
        lines = self.file.readlines()
        return lines[-1]

    def close(self):
        self.file.close()

