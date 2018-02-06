class Record(object):
    def __init__(self, data) -> None:
        super().__init__()

        self.path = data[0]
        self.process = data[1]
        self.thread = data[2]
        self.processId = data[3]
        self.threadId = data[4]
        self.readCount = data[5]
        self.readBytes = data[6]
        self.readTime = data[7]
        self.writeCount = data[8]
        self.writeBytes = data[9]
        self.writeTime = data[10]
        self.stacktrace = data[11]
        self.openTime = data[12]
        self.closeTime = data[13]
