import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("uber.csv").dropna()

def haversine(lat1, lon1, lat2, lon2):
    R = 6378.8
    dLat = np.radians(lat2-lat1)
    dLon = np.radians(lon2-lon1)
    lat1, lat2 = np.radians(lat1), np.radians(lat2)
    a = np.sin(dLat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dLon/2)**2
    return 2*R*np.arcsin(np.sqrt(a))

df['distance'] = haversine(df['pickup_latitude'], df['pickup_longitude'],
                           df['dropoff_latitude'], df['dropoff_longitude'])

X = df[['distance']]
y = df['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression().fit(X_train, y_train)
rf = RandomForestRegressor().fit(X_train, y_train)

print("Linear R2:", r2_score(y_test, lr.predict(X_test)))
print("RF R2:", r2_score(y_test, rf.predict(X_test)))
