import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from env import user, password, host
from sklearn.feature_extraction.text import TfidfVectorizer

def get_db_url(database, host=host, user=user, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'

url = get_db_url("spam_db")
sql = "SELECT * FROM spam"

df = pd.read_sql(sql, url, index_col="id")
print(df.head())

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df.text)
y = df.label

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2)

train = pd.DataFrame(dict(actual=y_train))
test = pd.DataFrame(dict(actual=y_test))

lr = LogisticRegression().fit(X_train, y_train)

train['predicted'] = lr.predict(X_train)
test['predicted'] = lr.predict(X_test)

print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.predicted)))
print('---TRAIN---')
print('Confusion Matrix')
print(pd.crosstab(train.predicted, train.actual))
print('---TRAIN---')
print(classification_report(train.actual, train.predicted))

print('Accuracy: {:.2%}'.format(accuracy_score(test.actual, test.predicted)))
print('---TEST---')
print('Confusion Matrix')
print(pd.crosstab(test.predicted, test.actual))
print('---TEST---')
print(classification_report(test.actual, test.predicted))