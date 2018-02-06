class MarkHelper:
    @staticmethod
    def get_io_mark(record, style):

        if (record.thread == "main"):
            return MarkHelper.IOMark("io in main thread", style.error)
        elif MarkHelper.isUnbufferedIO(record):
            return MarkHelper.IOMark("unbufferedIO", style.warning)
        else:
            return MarkHelper.IOMark("ok", style.common)

    @staticmethod
    def isUnbufferedIO(ioRecord):
        return ioRecord.readBytes < 10 * 512 and ioRecord.readCount > 10 or (
            ioRecord.writeBytes < 10 * 512 and ioRecord.writeCount > 10)

    class IOMark(object):

        def __init__(self, message, style) -> None:
            super().__init__()

            self.message = message
            self.style = style
