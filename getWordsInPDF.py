import re
from collections import Counter

from pattern.en import lemma
import textract


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
