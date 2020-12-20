# -*- encoding: utf-8 -*-
'''
@File    :   merger.py
@Time    :   2020/12/20 19:14:30
@Author  :   Xiaochuan LI 
@Version :   1.0
@Contact :   lixiaochuan@buua.edu.cn
@License :   (C)Copyright 2020-2021, Lixiaochuan-BUAA-vrlab
@Desc    :   None
'''

# here put the import lib

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time


def MergePDF(files, outfile):
    log = ""
    output = PdfFileWriter()
    outputPages = 0
    for pdf_file in files:
        # print(type(pdf_file))
        log += "filename : {}\n".format(pdf_file)
        input = PdfFileReader(open(pdf_file, "rb"))
        pageCount = input.getNumPages()
        log += "pageCount : {}\n".format(pageCount)
        outputPages += pageCount
        for iPage in range(pageCount):
            output.addPage(input.getPage(iPage))
        log += "\n"

    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()
    log += "Save to : {}\n".format(outfile)
    log += "Total pages : {}".format(outputPages)
    return log
