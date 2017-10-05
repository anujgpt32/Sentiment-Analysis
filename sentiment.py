import pandas as pd
from textblob import TextBlob

def main():
	dat = pd.read_csv('twitter-sanders-apple3.csv', index_col = False)
	length = len(dat)
	calculated = list()
	for txt in dat.text:
		t = TextBlob(txt)
		pol = t.sentiment.polarity
		#Setting new calculated labels according to the original lables.
		if(pol<0.0):
			calculated.append("Neg")
		elif(pol==0.0):
			calculated.append("Neutral")
		else:
			calculated.append("Pos")

	dat['calculated'] = pd.Series(calculated)
	#x = dat.loc[dat['class']=='Neg']
	print("Analysis of tweets about Apple: ")
	pos = len(dat.loc[dat['calculated']=='Pos'])
	neu = len(dat.loc[dat['calculated']=='Neutral'])
	neg = len(dat.loc[dat['calculated']=='Neg'])

	print("Total Calculated Positive comments: ", pos)
	print("Total Calculated Negative comments: ", neg)
	print("Total Calculated Neutral comments: ", neu)

	pos = len(dat.loc[dat['class']=='Pos'])
	neu = len(dat.loc[dat['class']=='Neutral'])
	neg = len(dat.loc[dat['class']=='Neg'])

	print("Original Positive comments: ", pos)
	print("Original Negative comments: ", neg)
	print("Original Neutral comments: ", neu)

	correct = dat.loc[dat['class']==dat['calculated']]
	accuracy = (len(correct)/length)*100
	print("Accuracy: "+'{0:.5g}'.format(accuracy)+"%")


main()