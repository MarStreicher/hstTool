import gzip

def getReadLength(path):
    readLength = []
    with gzip.open(path, 'rt') as fqfile: #rt = read text
        lineNumber = 0
        for line in fqfile:
            lineNumber += 1
            if lineNumber % 4 == 2:
                readNumLength = len(line.strip())
                readLength.append(readNumLength)
    
    if len(set(readLength)) == 1:
        same_value = readLength[0]
        print("The list consists of the same value:", same_value)
        return [same_value]
    else:
        return readLength

def countReadAmount(readLength):
    readAmount = len(readLength)
    return readAmount
