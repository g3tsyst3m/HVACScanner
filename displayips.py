with open("collectedips.txt") as f:
    content = f.readlines()
    print len(content)
print content[len(content)-1]