import filter

print("[Transport 3] LRT Train / MRT Train:\n")
print("Converting website to text version...\n")

wordstring = ' Delays at Kelana Jaya LRT due to signalling issues'
wordstring += ' Nation'
wordstring += ' Monday, 18 Feb 2019'

wordstring += ' 1:22 AM MYT'
wordstring += ' PETALING JAYA: The Kelana Jaya LRT line is experiencing delays on Monday (Feb 18) due to a signalling fault between the Kelana Jaya station and KLCC. '
wordstring += ' "Train within the area moving in manual mode," LRT operator RapidKL said in a tweet. '
wordstring += ' It added that trains within the area were moving slower and stayed longer at the platform. '
wordstring += ' It said that their technical team was on site working to resolve the problem and apologised for the disruption. '
wordstring += ' RapidKL said they would send buses to ferry passengers between Kelana Jaya Station to KL Sentral and between the KLCC Station to KL Sentral. '

txt = wordstring
q = 101 # A prime number

print("Removing stop words and punctuations...\n")
# print("[CHECK] ori text: ", txt)
txt_nopunct = filter.removePunc(txt)
# print("[CHECK] txt no punc: ", txt_nopunct)

# print("\n[REMOVING STOPWORDS..]")
occurrence = filter.search(filter.stopwords, txt_nopunct, q)
txt_new = filter.removeStopwords(txt_nopunct, occurrence)
# print("[CHECK] new txt: ", txt_new)

stopwfreq = len(occurrence)

print("Comparing words with positive, negative and neutral English words...\n")
occurrence = filter.search(filter.poswords, txt_new, q)
poswfreq = len(occurrence)

occurrence = filter.search(filter.negwords, txt_new, q)
negwfreq = len(occurrence)

occurrence = txt_new.split()
wordfreq = len(occurrence)

#wordlist = txt_new.split()
#wordfreq = []

#for w in wordlist:
#    wordfreq.append(wordlist.count(w))

neutralwfreq = wordfreq - poswfreq - negwfreq
# print("[CHECK FREQUENCY] StopW, PosW, NegW, NeutralW: " + str(stopwfreq) + " & " + str(poswfreq) + " & " + str(negwfreq) + " & " + str(neutralwfreq))

print("Filtered text: \n" + txt_new + "\n")
print("Frequency: " + str(wordfreq) + " words\n")
#print("Pairs\n" + str(list(zip(wordlist, wordfreq))))


