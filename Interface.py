def Dict2File(dict, file_name):
    print("*\tWrite out result file to ", file_name, '.', sep="")
    file = open(file_name, "w")
    file.write('\t\tSHA1\t\t\t\tsize(bytes)\t\t\tFile\n')
    for i in dict:
        file.write(dict[i][0] + '\t' + str(dict[i][1]) + '\t\t\t' + i + '\n')
    file.close()
    print("*\tWrite out Finish.", sep="")
    return


def File2Dict(file_name):
    print("*\tRead in result file from ", file_name, '.', sep="")
    file = None
    try:
        file = open(file_name, 'r')
    except:
        print('No such file')
    file.readline()
    dict = {}
    while True:
        str = file.readline()
        if not str:
            break
        str = str.split('\t')
        dict[str[4].strip('\n')] = (str[0], int(str[1]))
    file.close()
    print("*\tRead in Finish.", sep="")
    return dict
