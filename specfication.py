import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {'Car Name': ['Car A', 'Car B', 'Car C', 'Car D'],
        'Price': [25000, 27000, 26000, 29000]}

df = pd.read_excel("cars.xlsx")

# Vectorize car names using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Model'])

# Function to find related car names
def get_related_cars(car_name, top_n=3):
    # Transform input car name to the same vector space
    input_vec = vectorizer.transform([car_name])

    # Compute cosine similarity between the input and all other car names
    cos_sim = cosine_similarity(input_vec, X)

    # Get the indices of the most similar cars
    similar_indices = cos_sim.argsort()[0][-top_n-1:-1][::-1]

    related_cars = df.iloc[similar_indices]
    return related_cars

# Example usage: Find related cars to "Car A"
related = get_related_cars("جينيسG80 2018")
print(related)
