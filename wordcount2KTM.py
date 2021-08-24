import filter

print("[Transport 2] KTM Train / ETS Train / KLIA Transit:\n")
print("Converting website to text version...\n")

wordstring = 'KTM Komuter, ETS services to be delayed by 15 minutes after train derails at KL station (NSTTV)'
wordstring += ' Share this story'
wordstring += ' Whatsapp'
wordstring += ' Facebook'
wordstring += ' Twitter'
wordstring += ' [Image: Teoh Pei Ying] '
wordstring += ' By Teoh Pei Ying'
wordstring += ' April 15, 2018 @ 7:04pm'

wordstring += 'KUALA LUMPUR: All Keretapi Tanah Melayu Berhad (KTMB) services will be delayed at least 15 minutes after a train derailed at Platform 4 of the Kuala Lumpur station.'
wordstring += ' A KTMB spokesman, when contacted, said the train was travelling from Kuala Lumpur to Port Klang when the derailment occurred at 12.57pm.'
wordstring += ' It is understood that the KTM Komuter and ETS services will experience a 20 to 30 minutes delay, but there will be no cancellation of train services.'
wordstring += ' The spokesman added that KTMB still in the midst of investigating the case.'
wordstring += ' [Image: All Keretapi Tanah Melayu Berhad (KTMB) services will be delayed at least 15 minutes after a train derailed at Platform 4 of the Kuala Lumpur station. Pic by NSTP/ASWADI ALIAS]  All Keretapi Tanah Melayu Berhad (KTMB) services will be delayed at least 15 minutes after a train derailed at Platform 4 of the Kuala Lumpur station. Pic by NSTP/ASWADI ALIAS '
wordstring += ' Meanwhile, KTMB in a statement said Platform 3 of the Kuala Lumpur station is still operating.'
wordstring += ' "KTM Berhad apologises for any inconvenience. Repairs works are ongoing. We will update from time to time via our social media account.'
wordstring += ' "KTM Komuter will experience a delay between 20 and 30 minutes, while the ETS service is expected to be delayed between 15 and 20 minutes."'

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


