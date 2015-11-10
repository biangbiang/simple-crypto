#!/usr/bin/env python

import base64

def encode(sourceFileName, targetFileName):
    # encode
    source = open(sourceFileName, "rb")
    target = open(targetFileName, "wb")
    line = source.readline()
    while line:
        encodeData = base64.b64encode(line)
        target.write(encodeData + "\n")
        line = source.readline()
    source.close()
    target.close()

def decode(sourceFileName, targetFileName):
    # decode
    source = open(sourceFileName, "rb")
    target = open(targetFileName, "wb")
    line = source.readline()
    while line:
        decodeData = base64.b64decode(line)
        target.write(decodeData)
        line = source.readline()
    source.close()
    target.close()
