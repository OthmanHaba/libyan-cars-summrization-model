import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data (replace with your file path)
data = pd.read_excel('cars.xlsx')  # Replace with your file path
car_names = data['Name']  # Replace with the correct column name

# Vectorize the car names using TF-IDF
vectorizer = TfidfVectorizer()
car_vectors = vectorizer.fit_transform(car_names)

# Reduce dimensionality to 2D using PCA
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(car_vectors.toarray())

# Create a scatter plot of the car vectors
plt.figure(figsize=(10, 8))
sns.scatterplot(x=reduced_vectors[:, 0], y=reduced_vectors[:, 1], hue=car_names, palette='viridis', legend=None)

# Title and labels for the graph
plt.title('Car Names Vectorized and Visualized', fontsize=16)
plt.xlabel('PCA Component 1', fontsize=12)
plt.ylabel('PCA Component 2', fontsize=12)

# Show the plot
plt.show()
