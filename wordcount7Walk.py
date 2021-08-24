import filter

print("[Transport 7] Walk:\n")
print("Converting website to text version...\n")

wordstring = 'Why prioritising pedestrians over cars in Malaysia makes sense '
wordstring += 'Thursday, 28 Sep 2017 07:18 AM MYT '
wordstring += 'By Ida Lim '
wordstring += '[Image: David Tan is a researcher at United Nations University ― International Institute for Global Health. ― Picture by Choo Choy May]   David Tan is a researcher at United Nations University ― International Institute for Global Health. ― Picture by Choo Choy May '
wordstring += 'KUALA LUMPUR, Sept 28 — Making Malaysia more pedestrian-friendly instead of prioritising automobiles could improve the health of both Malaysians and the economy, according to researchers. '
wordstring += 'David Tan, a researcher with United Nations University International Institute for Global Health (UNU-IIGH), said cities should be designed and built to make it easy and convenient for people to make the healthier choice of walking over driving. “When neighbourhoods are walkable, when cities are walkable, obesity and diabetes go down,” he said in a talk by Think City on Tuesday night. Malaysia is reportedly the most obese nation in Southeast Asia. The National Health and Morbidity Survey of 2015 showed the Malaysian population to have greater rates of obesity and diabetes, with 17.7 per cent considered obese and 30 per cent overweight, while the overall prevalence of diabetes among adults was 17.5 per cent. '
wordstring += 'The government has sought to remedy this by, among others, eliminating price subsidies for both sugar and cooking oil. While pointing out that improving walkability in cities alone “is not going to magically solve everything,” Tan told Malay Mail Online that it is a “necessary part of any solution for obesity” and that cities should work at reducing barriers to help people incorporate physical activity into their everyday life. While advocating a grid layout of roads and a pedestrian-centric design to encourage walking for a new city built from scratch, Tan said existing cities like Kuala Lumpur could still make improvements to its walking experience by taking inspiration from the US city of Oklahoma. Oklahoma went from being the US second fattest city in 2009 to 22nd fittest city in 2012 by implementing a holistic health programme and using a sales tax that the community agreed on to fund the reforms, he explained. “Yes, there was health literacy. The government provided resources for small businesses, NGOs to create organisations that got people active. They also poured a ton of money into putting in sidewalks where they were not there; by rebuilding sidewalks that were in poor condition; by putting parks in the city and connecting walking routes to make a more connected, more attractive walking experience. And this city of 600,000 people collectively lost more than a million pounds in three years," he said during the talk. '
wordstring += 'When met later, Tan told Malay Mail Online that Oklahoma City is still a work in progress despite making a huge leap from its previously poor walking infrastructure. “Sometimes when we look at the most walkable cities in the world, we think there’s no way we are ever to get there, but we can look at Oklahoma City as a place that started out problematic and it has improved and continuing to improve, I think that can be encouraging for us when we don’t see how we get to the perfect place that we hope to be.” [Image: Tan said people should push for more spending on pedestrian infrastructure, instead of demanding for wider and more roads that would only make traffic jams worse. — Pix by Choo Choy May]   Tan said people should push for more spending on pedestrian infrastructure, instead of demanding for wider and more roads that would only make traffic jams worse. — Pix by Choo Choy MayAcknowledging that the heat in tropical Malaysia could make walking uncomfortable, Tan listed out various ways to do overcome this, such as putting up shaded walkways as seen around train stations, putting up plants or creating green spaces, designing buildings that reflect heat away from streets instead of into streets, and building places closer to each other to reduce walking distance. '
wordstring += '“If we invest in this infrastructure, making places more walkable, improving walking activity, we improve health. We can also develop a culture or society in which walking is a norm, where we value the infrastructure that helps us walk, where we demand it instead of demanding more roads," he said, later telling Malay Mail Online that it was important for citizens to back pedestrian culture for governments to be willing to spend on this. '
wordstring += 'He said the tendency of governments to build more and wider roads in response to public demand is counterproductive, as it does not cut down on congestion but spurs more people to buy cars and further worsen traffic jams. '
wordstring += '“No city in the world has managed to build its way out of congestion. It doesn’t work. When we build for driving, we end up building against walking,” he said, noting that pedestrian bridges for example are not built primarily to make it safer for pedestrians but to enable cars to drive without slowing down and stopping. '
wordstring += '[Image: James Speirs is a South African researcher based in Kuala Lumpur with an interest in urban mobility. ― Picture by Choo Choy May]   James Speirs is a South African researcher based in Kuala Lumpur with an interest in urban mobility. ― Picture by Choo Choy May KL doing well in region '
wordstring += 'James Speirs, a Think City researcher, told Malay Mail Online that Kuala Lumpur performed relatively well in the Southeast Asian region in terms of walkability, save for Singapore, which was a denser and more contained city-state not comparable to Malaysia’s sprawling capital city. '
wordstring += '“If you compare KL to its regional neighbours — to Bangkok, Manila and Jakarta, KL is doing very well. So the government is aware of the importance of it (walkability) and they are looking to develop it,” he said, noting that cities that are known globally for being easy to walk around in such as Barcelona and Paris could offer ideas for further improvement. '
wordstring += 'Noting the federal government’s River of Life project and a dedicated bicycle lane from Masjid Jamek to Midvalley, Speirs said Kuala Lumpur should focus on building pedestrian and cycling infrastructure that connects to this central artery as it would “increase mobility across the city.” '
wordstring += '“I think KL needs to expand on its strengths, the River of Life is going to put a fantastic pedestrian corridor through the middle of the city, I think the city should concentrate on connecting to the River of Life so that there are arteries going out into the city so that people can connect to it from adjacent neighbourhoods,” he said. '
wordstring += 'Speirs said Malaysia should increase the amount of money allocated for and spent on pedestrian infrastructure, such as pavements that are low-maintenance and long-lasting infrastructure. '
wordstring += '“So when you invest in pedestrian infrastructure, you improve the lives of people who live there and the experiences of people who visit. Everyone benefits,” he said, noting that a good walking experience would help encourage the millions of tourists visiting Kuala Lumpur annually to return. '
wordstring += 'He suggested simple measures to improve the experience for walking in cities, such as creating pedestrian crossings on the road instead of building expensive pedestrian bridges. '
wordstring += '[Image: People walk across a pedestrian crossing in front of a shopping mall at Kuala Lumpur’s Golden Triangle, as seen in 2015. — Picture by Yusof Mat Isa]   People walk across a pedestrian crossing in front of a shopping mall at Kuala Lumpur’s Golden Triangle, as seen in 2015. — Picture by Yusof Mat Isa '
wordstring += 'Arguing that more pedestrian space was good for tourism and businesses, Speirs said Kuala Lumpur must bring back its street-food culture and street-side businesses. '
wordstring += 'He cited food street Jalan Alor in Kuala Lumpur as an example of the city at its “pedestrian best” with a walk down this street showing a city that is alive and humming with business, while also sharing examples of other pedestrian-friendly spaces in cities abroad. '
wordstring += '“These are pedestrian spaces that people go to for recreation, to walk around, spend money and have a good time. It’s good for the economy, it’s good for property values, it’s good for our cities,” he said during the same talk. '
wordstring += 'Speirs encouraged Malaysians to increase their usage of sustainable transport methods such as cycling, riding buses or trains, as these public transport services and their frequencies would and could still improve when there is more usage as their capacity have not been fully used. '
wordstring += '“You will make the city more walkable by using these services because these are complementary industries,” he said, noting that the increased usage of motorcycles or cars would conversely worsen the commuting experience. '
wordstring += '[Image: Ian Goh is an entrepreneur and currently the Business Development Manager at oBike. ― Picture by Choo Choy May]   Ian Goh is an entrepreneur and currently the Business Development Manager at oBike. ― Picture by Choo Choy May '
wordstring += 'Cycling for better bike infrastructure '
wordstring += 'Ian Goh, oBike’s business development manager, explained at the talk why the dockless bike-sharing company decided to offer its services in Malaysia when the existing supporting infrastructure may be inadequate. '
wordstring += '“For us, it’s like a chicken-and-egg theory, our business by providing the bikes is like providing the chicken, when we provide this service and we gather sort of majority uptake of people using bicycles, some way or another bicycles become a major form of transportation in the Malaysian transportation ecosystem. '
wordstring += '“And with that you can get the egg, working closely with councils sharing the data that we have in terms of where they use it for,” he said at the same talk, adding that this would help cities plan better for bicycle lanes or routes that actually improves urban connectivity instead of being multi-million lanes built “for show.” '
wordstring += 'The data collection is possible as oBike’s bicycles are fitted with a satellite tracking system that can detect routes taken, with the service also using an app that pairs bicycles with individual users and records their trips. '
wordstring += 'Goh sees oBike’s bicycles as a solution for Malaysians who want to use public transport, but are located too near to drive and too far to walk to places like train stations. '
wordstring += 'The three were speakers at the eighth in a series of free public lectures held by community-focused urban rejuvenation organisation Think City since late last year. '

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

# Store stop word, positive word, negative word and total word frequency in a variable
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

