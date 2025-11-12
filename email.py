import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv("emails.csv")
X = df['text']
y = df['spam']

tfidf = TfidfVectorizer(stop_words='english')
X_vec = tfidf.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
svm = SVC(kernel='linear').fit(X_train, y_train)

print("KNN Accuracy:", accuracy_score(y_test, knn.predict(X_test)))
print("SVM Accuracy:", accuracy_score(y_test, svm.predict(X_test)))
