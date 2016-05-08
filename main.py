import argparse

import Compare
import DirSha1
import Interface


def main(Standfile, Testfile, dir, output):
    if dir is not None and output is not None:
        dict = DirSha1.Sha1ADir(dir)
        Interface.Dict2File(dict, output)
    if Standfile is not None and Testfile is not None:
        s = Interface.File2Dict(Standfile)
        t = Interface.File2Dict(Testfile)
        Compare.TraceFileMove(t, s)
        Compare.TraceFileChange(t, s)
        Compare.TaceFileDel(t, s)
        Compare.TraceFileAdd(t, s)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="File integrity verification tool.")
    g1 = parser.add_argument_group('Sha1 Calc', 'Sha1 and Record a dir')
    g1.add_argument('-o', '--output', help='The file you save result.')
    g1.add_argument('-d', '--dir', help='The dir you want to sha1 it.')
    g2 = parser.add_argument_group('Compare tool', 'Compare the result file to find changed.')
    g2.add_argument('-s', '--Standfile', help='The result you trust.')
    g2.add_argument('-t', '--Testfile', help='The result you want to test.')
    argv = parser.parse_args()
    print(argv)
    main(argv.Standfile, argv.Testfile, argv.dir, argv.output)
