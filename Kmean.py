import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')
data = df[['SALES', 'QUANTITYORDERED']].dropna()

# Scale data
scaler = StandardScaler()
X = scaler.fit_transform(data)

# Elbow Method
sse = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    sse.append(km.inertia_)

plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('SSE')
plt.show()

# From elbow, assume optimal K = 3
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Add cluster labels to data
data['Cluster'] = labels

# Plot clusters
plt.scatter(data['SALES'], data['QUANTITYORDERED'], c=labels, cmap='rainbow')
plt.xlabel('Sales')
plt.ylabel('Quantity Ordered')
plt.title('K-Means Clustering Result')
plt.show()
