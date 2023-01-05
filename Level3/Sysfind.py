import os


class Sysfind:
    def __init__(self):
        pass

    def findDrive(self):
        print(os.popen("fsutil fsinfo drives").read())
        print(os.system('cmd /c "wmic logicaldisk list brief"'))


if __name__ =='__main__':
    obj = Sysfind()
    obj.findDrive()
