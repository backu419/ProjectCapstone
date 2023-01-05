import os


def file_as_dic(path):
    d = path  # "C:\ProjectCapstone"
    result = {}
    for root, dire, files in os.walk(d):
        for d in dire:
            result[d] = os.listdir(root + "/" + d)
    print(result)


pa = input("Enter the file path: ")
file_as_dic(pa)
