import filter

print("[Transport 5] Ferry:\n")
print("Converting website to text version...\n")

wordstring = 'Butterworth to Penang by ferry: A relaxing, scenic journey'
wordstring += ' by'
wordstring += ' Malaysia Traveller'
wordstring += ' -'
wordstring += ' July 4, 2019 8:30 AM '
wordstring += ' The Butterworth to Penang Ferry is the traditional way to travel to Penang Island from the mainland.'
wordstring += ' The ferry opened back in 1894 and was then the only way for railway passengers from Singapore or Kuala Lumpur to reach George Town. It is still the most convenient way for rail travellers to reach Penang Island.'

wordstring += ' Nice view approaching George Town ferry pier. The building with the clock tower was the old FMS Railway Terminal where passengers would wait for the arrival of their ferry.'
wordstring += ' Most vehicle traffic these days use the two road bridges to Penang but the ferry, which carries cars and motorbikes, is a pleasant alternative for those not in a hurry. It is a relaxing way to travel and very convenient.'

wordstring += ' The ferry company is branded as Rapid Ferry. This ferry is 56 metres long and 11.6 m wide with a gross tonnage of 1647 tons and built in 2002 with a capacity of 300 passengers and about 60 cars.'

txt = wordstring
q = 101 # A prime number

print("Removing stop words and punctuations...\n")
# print("[CHECK] ori text: ", txt)
txt_nopunct = filter.removePunc(txt)
# print("[CHECK] txt no punc: ", txt_nopunct)

# print("\n[REMOVING STOPWORDS..]")
occurrence = filter.search(filter.stopwords, txt_nopunct, q)
txt_new = filter.removeStopwords(txt_nopunct, occurrence)
#print("[CHECK] new txt: ", txt_new)

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
# print("[CHECK OCCURRENCE] StopW, PosW, NegW, NeutralW: " + str(stopwfreq) + " & " + str(poswfreq) + " & " + str(negwfreq) + " & " + str(neutralwfreq))

print("Filtered text: \n" + txt_new + "\n")
print("Frequency: " + str(wordfreq) + " words\n")
#print("Pairs\n" + str(list(zip(wordlist, wordfreq))))

