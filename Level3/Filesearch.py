import os


class Filesearch:
    def __init__(self):
        pass

    def search_for_file(self, drive, file_name):
        try:
            print('This is a file searcher.')
            file_paths = []
            drv = drive + ":\\"
            print(drv)

            for r, d, f in os.walk(drv):
                for name in f:
                    if name == file_name:
                        path = os.path.abspath(os.path.join(r, name))
                        file_paths.append(path)
                        self.search_for_file(self, drive, file_name)

        except:
            print("There was an error")

    #        return file_paths

    def runn(self):
        self.search_for_file(self.drive, self.file_name)


if __name__ == '__main__':
    obj = Filesearch()
    obj.search_for_file("C", "demo.py")
    print(obj.runn())
