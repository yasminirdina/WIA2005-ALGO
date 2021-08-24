# filter.py

# LIST OF STOP WORDS
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']

for i in range(len(stopwords)):
    sw = stopwords[i]
    stopwords.append(sw.capitalize())

#list storing start index of stopword occurrences & the length of each stop word found in text
occurrence = []

# d is the number of characters in the input alphabet
d = 256
q = 101
punctuations = '''!()-[]{};:'“”"\,<>./?@#$―%^&*_~—’'''
# pat -> pattern
# txt -> text
# q -> A prime number

def removePunc(txt):
    no_punct = ""
    for i in range(len(txt)):
        if txt[i] not in punctuations: #(txt[i] is a space or huruf)
                no_punct = no_punct + txt[i]
        elif i>0 and txt[i] in punctuations and txt[i-1] != " " and txt[i-1] not in punctuations: #if (any char except space and punc)(punc)
            if i+1 != len(txt) and txt[i+1] != " " and txt[i+1] not in punctuations: #(any char except space & punc)(txt[i] = punc)(any char except space & punc)
                no_punct = no_punct + txt[i]
            elif i+1 != len(txt) and txt[i+1] in punctuations: #(any char except space & punc)(txt[i] = punc)(punc)
                no_punct = no_punct + ""
        elif txt[i] in punctuations and txt[i-1] == " ": #(space)(txt[i] = punc)
            if txt[i+1] != " " and txt[i+1] not in punctuations: #(space)(txt[i] = punc)(huruf)
                no_punct = no_punct + ""
        elif i == 0 and txt[i] in punctuations and txt[i+1] != " " and txt[i+1] not in punctuations: #(START WORD)(punc)(huruf)
                no_punct = no_punct + ""

    return no_punct

def search(stopwords, txt, q):
    occurrence = []
    for x in range(len(stopwords) - 1):
        M = len(stopwords[x])
        N = len(txt)
        i = 0
        j = 0
        p = 0 # hash value for pattern
        t = 0 # hash value for txt
        h = 1
        index_occ = 0

        # The value of h would be "pow(d, M-1)%q"
        for i in range(M-1):
            h = (h*d)%q

        # Calculate the hash value of pattern and first window
        # of text
        for i in range(M):
            p = (d*p + ord((stopwords[x])[i]))%q
            t = (d*t + ord(txt[i]))%q

        # Slide the pattern over text one by one
        for i in range(N-M+1):
            # Check the hash values of current window of text and
            # pattern if the hash values match then only check
            # for characters on by one
            if p==t:
                # Check for characters one by one
                for j in range(M):
                    if txt[i+j] != (stopwords[x])[j]:
                        break

                j+=1
                # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
                if j==M and i > 0 and txt[i-1] == " ":
                    #if (space)(stopword)(space)
                    if i+M != len(txt) and txt[i+M] == " ":
                        #print ("[CHECK] #1a Pattern found at index " + str(i))
                        occurrence.append([i, txt[i: i+M+1: 1], len(txt[i: i+M+1: 1])])
                    #if (space)(stopword)(END OF TEXT) @ last word is the stop word
                    elif i+M == len(txt):
                        #print ("[CHECK] #1b Pattern found at index " + str(i))
                        occurrence.append([i, txt[i: i+M: 1], len(txt[i: i+M: 1])])
                #if (START OF TEXT)(stopword)(space) @ the first word is stop word
                elif j==M and i == 0 and txt[i+M] == " ":
                        #print ("[CHECK] #2 Pattern found at index " + str(i))
                        occurrence.append([i, txt[i: i+M+1: 1], len(txt[i: i+M+1: 1])])


            # Calculate hash value for next window of text: Remove
            # leading digit, add trailing digit
            if i < N-M:
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

                # We might get negative values of t, converting it to
                # positive
                if t < 0:
                    t = t+q

    # print("\n[CHECK] occurrence: ", occurrence)
    return occurrence

# Given a list of words, remove any that are
# in a list of stop words.
def removeStopwords(txt_nopunct, occurrence):
    txt_ast = txt_nopunct
    #replacing stopwords + with/without spaces with '*'
    for i in range(len(txt_nopunct)):
        for j in range(len(occurrence)):
            if i == (occurrence[j])[0]:
                length = i + occurrence[j][2]
                for k in range(i, length):
                    #print("[CHECK] txt at k before *: ", txt_ast[k])
                    txt_ast = txt_ast[:k] + "*" + txt_ast[k+1:]
                    #txt_nopunct.replace(str(txt_nopunct[k]), "*")
                    #print("[CEHCK] txt at k after *: ", txt_ast[k])
                break

    # print("[CHECK] txt with *: ", txt_ast)
    # #removing '*', only leave characters other than asterisk
    new_txt = ""
    for m in range(len(txt_ast)):
        if txt_ast[m] != "*":
            new_txt = new_txt + txt_ast[m]

    return new_txt

# LIST OF POSITIVE WORDS
f = open('positivewords.txt', 'r', encoding="utf8")
poswords = f.read()
poswords = removePunc(poswords)
poswords = poswords.split()
for i in range(len(poswords)):
    pw = poswords[i]
    poswords.append(pw.capitalize())
f.close()

# LIST OF NEGATIVE WORDS
f = open('negativewords.txt', 'r', encoding="utf8")
negwords = f.read()
negwords = removePunc(negwords)
negwords = negwords.split()
for i in range(len(negwords)):
    nw = negwords[i]
    negwords.append(nw.capitalize())
f.close()
