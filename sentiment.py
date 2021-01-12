from textblob import TextBlob

userSentence = input("Enter sentence to analyse: ")
scanner = TextBlob(userSentence)
score = scanner.sentiment.polarity

if score < 0:
    print("This sentance contains negative sentiment")
elif score==0:
    print("This sentance contains neutral sentiment")
elif score>0 and score<=1:
    print("This sentance contains positive sentiment")