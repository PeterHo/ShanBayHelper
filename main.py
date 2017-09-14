import sys

from getLearingWords import begin
from getWordsInPDF import getPdfWords

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("shanbaywords username password")
        print("pdf pdfFileName")
    elif sys.argv[1] == "shanbaywords":
        begin(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "pdf":
        getPdfWords(sys.argv[2])
