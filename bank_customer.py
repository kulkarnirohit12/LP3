import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv("Churn_Modelling.csv")
X = df.iloc[:, 3:13]
y = df.iloc[:, 13]

X['Geography'] = LabelEncoder().fit_transform(X['Geography'])
X['Gender'] = LabelEncoder().fit_transform(X['Gender'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = Sequential([
    Dense(6, activation='relu', input_dim=10),
    Dense(6, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=32)
