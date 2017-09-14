import re
import sys
from collections import Counter

from pattern.en import lemma
import textract

# from getLearingWords import begin


def getPdfWords(pdfFile):
    text = textract.process(pdfFile).decode()
    cnt = Counter()
    for word in re.sub(r"[^a-zA-Z]", " ", text).split():
        cnt[lemma(word.lower())] += 1

    remove = [k for k in cnt if len(k) < 3 or cnt[k] < 4]
    print(len(remove))
    for k in remove:
        del cnt[k]

    print(len(cnt))
    print(cnt.most_common())
    for w in cnt.most_common():
        print(w[0])


if __name__ == '__main__':
    # if sys.argv[1] == "shanbaywords":
    #     begin(sys.argv[2], sys.argv[3])
    # elif sys.argv[1] == "pdf":
    #     # getPdfWords(sys.argv[2])
    #     getPdfWords("C:\\Users\\peter\\OneDrive\\books\\Head First Design Patterns.pdf")
    getPdfWords("/mnt/c/Users/peter/Downloads/1.pdf")
