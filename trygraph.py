import plotly.graph_objects as go

print("<--- QUESTION 5: Extracting information on public transportation from Internet. --->")
print("<-------------------------------------- & ----------------------------------------->")
print("<---------- QUESTION 7: Compare negative/positive/neutral English words. ---------->\n")

import wordcount1Bas

import wordcount2KTM

import wordcount3LRT

import wordcount4Grab

import wordcount5Ferry

import wordcount6Flight

import wordcount7Walk

print("<--- QUESTION 6 & 8: Plotting histogram related to word count, stop words, negative and positive words. --->\n")

x = ["Bas","KTM","LRT","Grab", "Ferry","Flight", "Walk"]
y = [str(wordcount1Bas.wordfreq),str(wordcount2KTM.wordfreq),str(wordcount3LRT.wordfreq),str(wordcount4Grab.wordfreq),str(wordcount5Ferry.wordfreq),str(wordcount6Flight.wordfreq),str(wordcount7Walk.wordfreq)]
z = [str(wordcount1Bas.stopwfreq), str(wordcount2KTM.stopwfreq), str(wordcount3LRT.stopwfreq), str(wordcount4Grab.stopwfreq), str(wordcount5Ferry.stopwfreq), str(wordcount6Flight.stopwfreq),str(wordcount7Walk.stopwfreq)]
a = [str(wordcount1Bas.poswfreq), str(wordcount2KTM.poswfreq), str(wordcount3LRT.poswfreq), str(wordcount4Grab.poswfreq), str(wordcount5Ferry.poswfreq), str(wordcount6Flight.poswfreq),str(wordcount7Walk.poswfreq)]
b = [str(wordcount1Bas.negwfreq), str(wordcount2KTM.negwfreq), str(wordcount3LRT.negwfreq), str(wordcount4Grab.negwfreq), str(wordcount5Ferry.negwfreq), str(wordcount6Flight.negwfreq),str(wordcount7Walk.negwfreq)]

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="Word count"))
fig.add_trace(go.Histogram(histfunc="sum", y=z, x=x, name="Stop words"))
fig.add_trace(go.Histogram(histfunc="sum", y=a, x=x, name="Positive words"))
fig.add_trace(go.Histogram(histfunc="sum", y=b, x=x, name="Negative words"))

fig.show()

print("Histogram has been draw successfully! Check the localhost page on your web browser to view the histogram.\n")

#question 9
trans_perc = []
trans_wt = []

def calc_sent_perc():
    sent_bus =  (wordcount1Bas.poswfreq / wordcount1Bas.wordfreq) - (wordcount1Bas.negwfreq / wordcount1Bas.wordfreq)
    trans_perc.append(["Bus", sent_bus])
    trans_wt.append(["Bus", round(sent_weightage(sent_bus),2)])
    sent_KTM =  (wordcount2KTM.poswfreq / wordcount2KTM.wordfreq) - (wordcount2KTM.negwfreq / wordcount2KTM.wordfreq)
    trans_perc.append(["KTM", sent_KTM])
    trans_wt.append(["KTM", round(sent_weightage(sent_KTM),2)])
    sent_LRT =  (wordcount3LRT.poswfreq / wordcount3LRT.wordfreq) - (wordcount3LRT.negwfreq / wordcount3LRT.wordfreq)
    trans_perc.append(["LRT", sent_LRT])
    trans_wt.append(["LRT", round(sent_weightage(sent_LRT),2)])
    sent_Grab =  (wordcount4Grab.poswfreq / wordcount4Grab.wordfreq) - (wordcount4Grab.negwfreq / wordcount4Grab.wordfreq)
    trans_perc.append(["Grab", sent_Grab])
    trans_wt.append(["Grab", round(sent_weightage(sent_Grab),2)])
    sent_Ferry = (wordcount5Ferry.poswfreq / wordcount5Ferry.wordfreq) - (wordcount5Ferry.negwfreq / wordcount5Ferry.wordfreq)
    trans_perc.append(["Ferry", sent_Ferry])
    trans_wt.append(["Ferry", round(sent_weightage(sent_Ferry),2)])
    sent_Flight = (wordcount6Flight.poswfreq / wordcount6Flight.wordfreq) - (wordcount6Flight.negwfreq / wordcount6Flight.wordfreq)
    trans_perc.append(["Flight", sent_Flight])
    trans_wt.append(["Flight", round(sent_weightage(sent_Flight),2)])
    sent_Walk =  (wordcount7Walk.poswfreq / wordcount7Walk.wordfreq) - (wordcount7Walk.negwfreq / wordcount7Walk.wordfreq)
    trans_perc.append(["Walk", sent_Walk])
    trans_wt.append(["Walk", round(sent_weightage(sent_Walk),2)])

def print_sent_analysis():
    calc_sent_perc()
    #print("trans_perc: ", trans_perc)
    #print("\ntrans_wt: ", trans_wt)
    print("<--- QUESTION 9: Concluding the sentiment of the articles for different types of transportation. --->\n")
    for i in range(len(trans_perc)):
        print((trans_perc[i])[0] + " " + sent_conclude((trans_perc[i])[1]))
    print("")

def calc_sentiment_weightage():
    return trans_wt

def sent_weightage(sent):
    weightage = 25+ (50*sent)
    return weightage

def sent_conclude(sent):
    if(sent < 0):
        return "has a negative sentiment"
    else:
        return "has a positive sentiment"

print_sent_analysis()
