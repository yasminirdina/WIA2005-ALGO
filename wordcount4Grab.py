import filter

print("[Transport 4] Grab:\n")
print("Converting website to text version...\n")

wordstring = 'How Grab is Becoming an Everyday, Everything App in Southeast Asia'
wordstring += ' A glimpse of the ride-hailing powerhouses forays into various consumer services sectors'
wordstring += ' [Image: How Grab is Becoming an Everyday, Everything App in Southeast Asia]'
wordstring += ' Image credit: Shutterstock'
wordstring += ' [Image: Dipen Pradhan]'
wordstring += ' Dipen Pradhan'
wordstring += ' Senior Correspondent, Entrepreneur Asia Pacific'
wordstring += ' June 3, 2019 6 min read'

wordstring += ' Opinions expressed by Entrepreneur contributors are their own.'
wordstring += ' Anthony Tan and Tan Hooi Ling spun the idea of building a ride-hailing company, Grab, while pursuing MBA at Harvard Business School. Grab was initially conceived as a college project and had bagged US$25,000 in prize money from the pitch contest organised by the school.'

wordstring += ' Hailing from Malaysia, the duo was aware of the chaotic and unorganised scene the Southeast Asian countries’ transportation sector  faced. Moreover, rolling out a ride-hailing service in the region would give them first-mover advantage. Bringing together their knowledge in business administration and general management, the two started jotting down a business plan and built the application with the prize money they won from the pitch contest.'

wordstring += ' After sleepless nights and countless brainstorming sessions, Anthony and Tan rolled out GrabTaxi in 2012 in Malaysia—just a year before Uber launched its ride-hailing service in Singapore and two years after Go-Jek in Indonesia.'

wordstring += ' Like in any developed and developing nations, ride-hailing has become an everyday app in the SEA countries as well. The region’s online economy is driven heavily by a large, growing, and incredibly engaged internet user base. A 2018 report by Google and Temasek suggests the Southeast Asian internet economy has reached US$72 billion in (GMV). And, taking the lead position are online travel, e-commerce, online media, and ride hailing sectors, the same report suggests.'


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


