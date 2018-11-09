# Naive Bayes Algorithm

dummy_text = [
    'Hello! How are you?',
    'Call me back ASAP',
]
lower_case_text = []

for sms in dummy_text:
    lower_case_text.append(sms.lower())

from string import punctuation

punctuation_less_text = []

for sms in lower_case_text:
    ''.join([char for char in sms if char not in punctuation])

tokenised_text = []

for sms in punctuation_less_text:
    tokenised_text.append(sms.split(' '))

from colections import Counter

for sms in tokenised_text:
    print(Counter(sms))

from sklearn.feature_extraction.text import CounterVectorizer

cv = CounterVectorizer()
cv.fit(dummy_text)
cv.transform(dummy_text)
cv.get_feature_names()

import pandas as pd
pd.set_option('display.max_columns', 500)
frequency_matrix = pd.DataFrame(data=cv.transform(dummy_text).toarray(), columns=cv.get_feature_names())

sms_text = pd.read_table('SMSSpamCollection', names=['label', 'sms'])
sms_text.head()
sms_text['label'] = sms_text['label'].map({'ham':0,'spam':1})

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(sms_text['sms'], sms_text['label'], random_state=42)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
cv = CounterVectorizer()
transformed_xtrain = cv.fit_transform(xtrain)
transformed_xtest = cv.transform(xtest)

model.fit(transformed_xtrain, ytrain)

from sklearn.metrics import accuracy_score, precision_score, recall_score

predictions = model.predict(transformed_xtest)
print(f'Accuracy scpre: {accuracy_score(ytest, predictions)}')
print(f'Accuracy scpre: {precision_score(ytest, predictions)}')
print(f'Accuracy scpre: {recall_score(ytest, predictions)}')
