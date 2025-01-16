# Import libraries  
import pandas as pd  
import numpy as np  
from sklearn.preprocessing import StandardScaler  
from sklearn.cluster import KMeans  
from sklearn.metrics import silhouette_score  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Step 1: Load dataset from CSV file  
file_path = 'Dataset Project K-Means.csv'  
data = pd.read_csv(file_path)  
  
# Display the first few rows of the dataset to ensure it's loaded correctly  
print(data.head())  
  
# Step 2: Preprocessing  
features = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]  
scaler = StandardScaler()  
scaled_features = scaler.fit_transform(features)  
  
# Step 3: Elbow Method  
inertia = []  
silhouette_scores = []  
k_range = range(2, 11)  
  
for k in k_range:  
    kmeans = KMeans(n_clusters=k, random_state=42)  
    kmeans.fit(scaled_features)  
    inertia.append(kmeans.inertia_)  
    silhouette_scores.append(silhouette_score(scaled_features, kmeans.labels_))  
  
# Plot Elbow Method  
plt.figure(figsize=(10, 5))  
plt.plot(k_range, inertia, marker='o', label='Inertia', linestyle='--')  
plt.title('Elbow Method for Optimal k')  
plt.xlabel('Number of Clusters')  
plt.ylabel('Inertia')  
plt.legend()  
plt.grid(True)  
plt.show()  
  
# Plot Silhouette Scores  
plt.figure(figsize=(10, 5))  
plt.plot(k_range, silhouette_scores, marker='o', label='Silhouette Score', linestyle='--', color='orange')  
plt.title('Silhouette Score for Optimal k')  
plt.xlabel('Number of Clusters')  
plt.ylabel('Silhouette Score')  
plt.legend()  
plt.grid(True)  
plt.show()  
  
# Step 4: Perform K-Means Clustering with k=3 (from earlier decision)  
kmeans = KMeans(n_clusters=3, random_state=42)  
data['Cluster'] = kmeans.fit_predict(scaled_features)  
  
# Step 5: Visualizations  
plt.figure(figsize=(10, 6))  
sns.scatterplot(  
    x=data['Annual Income (k$)'],   
    y=data['Spending Score (1-100)'],   
    hue=data['Cluster'],   
    palette='Set1', s=100  
)  
plt.title('K-Means Clustering (k=3)')  
plt.xlabel('Annual Income (k$)')  
plt.ylabel('Spending Score (1-100)')  
plt.legend(title='Cluster')  
plt.show()  
  
# Step 6: Analyze Clusters  
cluster_summary = data.groupby('Cluster').mean()  
print(cluster_summary)  
