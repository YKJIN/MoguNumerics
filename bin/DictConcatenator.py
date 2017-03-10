# concatenate pickles of Python dicts

import pickle
import argparse

def getArgParser():
    parser = argparse.ArgumentParser(description='Concatenate pickles of Python dicts.')
    parser.add_argument('output_file', help='pickled file of concatenated dict.')
    parser.add_argument('input_files', nargs='+', help='pickled files of dicts to concatenate.')
    return parser

def readPickledFile(pickledfile):
    return pickle.load(pickledfile)

def writePickledObjToFile(obj, outputpickledfile):
    pickle.dump(obj, outputpickledfile)

if __name__=='__main__':
    parser = getArgParser()
    args = parser.parse_args()

    resultdict = {}
    for inputfilename in args.input_files:
        infile = open(inputfilename, 'rb')
        thisdict = readPickledFile(infile)
        try:
            resultdict.update(thisdict)
        except TypeError:
            print 'File ', infile, ' is not a valid Python dict!'

    writePickledObjToFile(resultdict, open(args.output_file, 'wb'))