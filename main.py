import sys

import textract

from getLearingWords import begin


def getPdfWords(pdfFile):
    text = textract.process(pdfFile)
    print(len(text))


if __name__ == '__main__':
    # if sys.argv[1] == "shanbaywords":
    #     begin(sys.argv[2], sys.argv[3])
    # elif sys.argv[1] == "pdf":
    #     # getPdfWords(sys.argv[2])
    #     getPdfWords("C:\\Users\\peter\\OneDrive\\books\\Head First Design Patterns.pdf")
    getPdfWords("C:\\Users\\peter\\Downloads\\1.pdf")
