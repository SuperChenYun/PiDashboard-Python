def getFile(path):
    f = open(path)
    content = f.read()
    f.close()
    return content