import logging


class FileLog():

    def __init__(self):
        logging.basicConfig(filename="filelog.txt",level=logging.WARNING)

    def Operations(self):
        try:
            self.x = int(input("Enter the Number: "))
            self.y = int(input("Enter the Second Number: "))
            print(self.x/self.y)
        except ZeroDivisionError as msg:
            logging.exception(msg)
        except ValueError as msg:
            logging.exception(msg)


if __name__ == '__main__':
    obj = FileLog()
    obj.Operations()

    # obj.Operations(10,0)
    # obj.Operations(10, "ten")
