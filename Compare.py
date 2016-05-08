def TraceFileMove(Tdict, Sdict):
    Tset = Tdict.items()
    Sset = Sdict.items()
    reSdict = {value[0]: key for key, value in Sdict.items()}
    diff = Tset - Sset
    for i in diff:
        if i[1][0] in reSdict.keys() and i[0] != reSdict[i[1][0]]:
            print("Move\t", reSdict[i[1][0]], "\t------->\t", i[0], sep="")
    return


def TraceFileChange(Tdict, Sdict):
    Tset = Tdict.items()
    Sset = Sdict.items()
    diff = Tset - Sset
    for i in diff:
        if i[0] in Sdict.keys() and i[1][0] != Sdict[i[0]][0]:
            print("Change\t", i[0], "\tSize(bytes)\t", Sdict[i[0]][1], "\t------->\t", i[1][1])
    return


def TaceFileDel(Tdict, Sdict):
    Tset = set(Tdict.keys())
    Sset = set(Sdict.keys())
    diff = Sset - Tset
    for i in diff:
        if Sdict[i] not in Tdict.values():
            print("Del\t", i, "\tSize(bytes)\t", Sdict[i][1], "\tsha1\t", Sdict[i][0])
    return


def TraceFileAdd(Tdict, Sdict):
    Tset = set(Tdict.keys())
    Sset = set(Sdict.keys())
    diff = Tset - Sset
    for i in diff:
        if Tdict[i] not in Sdict.values():
            print("Add\t", i, "\tSize(bytes)\t", Tdict[i][1], "\tsha1\t", Tdict[i][0])
    pass
