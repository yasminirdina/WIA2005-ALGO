import filter

print("[Transport 1] MRT Bus / Rapid KL Bus / Bus:\n")
print("Converting website to text version...\n")

wordstring ='[Image: Passengers waiting anxiously for their buses to arrive. Pic by Ghazali Kori]'
wordstring += ' Passengers waiting anxiously for their buses to arrive. Pic by Ghazali Kori'
wordstring += ' October 4, 2014 @ 8:03am'
wordstring += ' KUALA LUMPUR: Some 100 passengers were stranded at UTC Pudu Sentral for a few hours on Thursday night.'
wordstring += ' The express bus they were waiting for was detained by Land Public Transport Commission (SPAD) officers as it did not have a Temporary Transition Licence (LPS) to ferry passengers.'
wordstring += ' The passengers were supposed to board the bus to Kuala Perlis at 11.30pm but it was delayed to 3.30am.'
wordstring += ' A SPAD spokesman said the express bus company had hired a tour bus to ferry the passengers because its buses could not accommodate passengers travelling back to their hometowns for Hari Raya Aidil Adha.'
wordstring += ' Yesterday morning, many people at Pudu Sentral were complaining that express buses were not arriving on time. They said they had been waiting for more than an hour for their buses to arrive.'
wordstring += ' A man, who wanted to be known only as Noh, said he was taking the express bus for the first time and was frustrated with the public transport system.'
wordstring += ' “I am supposed to fetch my daughter in Lumut and accompany her back to Kuala Lumpur for her short holiday.'
wordstring += ' “Waiting here for the bus is a waste of time. The basement where we have to wait for the bus is also hot and humid,” he said.'
wordstring += ' Noh urged the authorities, especially SPAD, to take action against operators if buses are late.'
wordstring += ' “The authorities need to ensure that our transport system is efficient. How are we going to be a developed nation if our public transport system is inefficient?”'
wordstring += ' Hazwan Nasir, 23, who was waiting for the Ekspres Kesatuan bus to Lumut, said the bus was usually punctual.'
wordstring += ' “The bus was supposed to be here at 10am. I have been waiting for almost an hour now and I don’t see any sign of the bus.'
wordstring += ' A 19-year-old passenger, who only wanted to be known as Chun, said he had expected the bus to be late as it was the norm during festive seasons.'
wordstring += ' “I hope the authorities will take action to improve the service.”'
wordstring += ' Another passenger, Naimullah Muhammad Tahir, 19, who was travelling to Baling, Kedah, said he had been waiting for an hour for the bus.'
wordstring += ' “I can’t wait to go home to celebrate Raya Qurban with my family but the bus service is delaying my journey home,” he said.'
wordstring += ' Abu Bakar Abdullah, 26, who was waiting for Edaran Ekspres bus said he had to wait for more than two hours for a bus last year.'
wordstring += ' “I guess it’s because of the heavy traffic.”'
wordstring += ' SPAD enforcement division head Datuk Che Hasni Che Ahmad confirmed that the buses were tour buses and did not have the temporary licences.'
wordstring += ' He said the delays were due to the fact that the drivers could not bring the buses to the terminal, when enforcement officers were around, because they did not have the licence.'
wordstring += ' Che Hasni said that this was not the first time such an incident had happened.'
wordstring += ' “Every time our enforcement officers carry out checks, this will happen,” he said, adding that recently, SPAD had stepped up its enforcement efforts.'
wordstring += ' “This is why we urge the public to purchase tickets from the counters, instead of touts, because the operators at the counters have the necessary permits.” By Seri Nor Nadiah Koris'

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



