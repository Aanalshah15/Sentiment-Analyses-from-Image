import nltk

# nltk.download('movie_reviews')
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews


def extract_features(word_list):
    return dict([(word, True) for word in word_list])


negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
# print(negids)

negfeats = [(extract_features(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(extract_features(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = int(len(negfeats) * 0.8)
poscutoff = int(len(posfeats) * 0.8)

trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print("train on %d instances, test on %d instances", len(trainfeats), len(testfeats))
classifier = NaiveBayesClassifier.train(trainfeats)
print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
classifier.show_most_informative_features()


# input_reviews = ["It is an amazing movie","This is a dull movie. I would never recommend it to anyone.",
# "The cinematography is pretty great in this movie","The direction was terrible and the story was all over the place",
# "it was great experience","it was awesome movie","food was not good","i like to swim"]
#
# # input_reviews = [input("Enter: ") for i in range(int(input("Enter number: ")))]
#
input_reviews = []

# file = open('output.txt','r')
# text = file.readlines()
# for i in text:
#
#     input_reviews.append(i)
# file.close()
# # # ----------------------------------
file = open('new12.txt','r')
text = file.read()
input_reviews.append(text)
file.close()
print(input_reviews)

print("Predictions: ")
neg_review = []
for review in input_reviews:
    # if probdist=="neg":
    print("\nReview:", review)
    probdist = classifier.prob_classify(extract_features(review.split()))
        # if probdist=="neg":

    pred_sentiment = probdist.max()
    print("Predicted sentiment: ", pred_sentiment)
    print("Probability: ", round(probdist.prob(pred_sentiment), 2))
    print("Probdist: ", probdist)
# # -------------------------------------------------------------------------
# # for review in input_reviews:
#     if pred_sentiment=="neg":
#         # print("xxxxxxxxxxx",review)
#         neg_review.append(review)
# print("\n")
# for i in neg_review:
#     print("NEGATIVE : ",i)
#
# a = open('new12.txt','w')
# a.writelines