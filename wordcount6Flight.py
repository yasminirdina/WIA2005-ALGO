import filter

print("[Transport 6] Flight:\n")
print("Converting website to text version...\n")

wordstring = '19 Penang flights affected by haze'
wordstring += ' [Image: Nineteen flights to and from Penang have been affected by the worsening haze. -- NSTP/ROSLI AHMAD] '
wordstring += ' Nineteen flights to and from Penang have been affected by the worsening haze. -- NSTP/ROSLI AHMAD'
wordstring += ' [Image: Mohamed Basyir] '
wordstring += ' by Mohamed Basyir'
wordstring += ' September 18, 2019 @ 7:41pm'

wordstring += ' GEORGE TOWN: Nineteen flights to and from Penang have been affected by the worsening haze.'

wordstring += ' Penang International Airport senior airport manager Mohd Nadzim Hashim said the flights were affected due to low visibility of only 1,600m as of 5pm today.'

wordstring += ' He said the eight flights which experienced delays included AirAsia Penang to Singapore at 11.20am, Lion Air from Penang to Kualanamu at 11.50am, Malaysian Airlines from Penang to Kuala Lumpur at 12.40pm, Cathay Dragon from Penang to Hong Kong at 1pm, AirAsia from Penang to Kualanamu at 12.45, Firefly from Penang to Subang at 1.05pm, AirAsia from Penang to Bangkok at 2pm and Malindo Air from Penang to Kuala Lumpur at 4.14pm.'

wordstring += ' He added that Lion Air from Medan, scheduled to land at 9.40am and UPS from Kuala Lumpur, scheduled to land at 10am were turned back.'

wordstring += ' Nadzim said five flights were diverted. Silk Air from Singapore to Penang scheduled to land at 10.15am was diverted to Kualanamu, Fedex from Bangkok and scheduled to land at 10.15am was diverted to Kuala Lumpur, Cathay Dragon from Hong Kong scheduled to land at 11.45am was diverted to Kuala Lumpur, EVA Air from Taiwan scheduled to land at noon was diverted to Langkawi and China Airlines from Taiwan and scheduled to land at 12.50pm was diverted to Kuala Lumpur.'

wordstring += ' “Four flights were cancelled — Silk Air from Singapore at 2.50pm, Silk Air to Singapore at 3.35pm, China Airlines from Taiwan at 1.15pm and China Airlines to Taiwan at 2.15pm.'

wordstring += ' “We are closely monitoring the situation with feedback from the Air Traffic Control Civil Aviation Authority Malaysia.'

wordstring += ' “We are handing out water to stranded passengers while the airlines are giving coupon meals to their passengers as well,” he added.'

wordstring += ' As of 6pm, the Air Pollutant Index (API) reading was at 239 in Minden and 257 in Balik Pulau.'

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

neutralwfreq = wordfreq - poswfreq - negwfreq
# print("[CHECK FREQUENCY] StopW, PosW, NegW, NeutralW: " + str(stopwfreq) + " & " + str(poswfreq) + " & " + str(negwfreq) + " & " + str(neutralwfreq))

print("Filtered text: \n" + txt_new + "\n")
print("Frequency: " + str(wordfreq) + " words\n")
#print("Pairs\n" + str(list(zip(wordlist, wordfreq))))


