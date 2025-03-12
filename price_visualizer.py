import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your spreadsheet data (assuming CSV file named 'your_file.csv')
data = pd.read_excel('cars.xlsx') # Or pd.read_excel('your_file.xlsx') for Excel files

# Data Cleaning: Remove currency and commas, then convert to numeric
data['Price'] = data['Price'].str.replace(' دينار', '', regex=False)  # Remove ' دينار'
data['Price'] = data['Price'].str.replace(',', '', regex=False)     # Remove commas
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')       # Convert to numeric, errors='coerce' for NaN

# Define price ranges (adjust these ranges as needed)
price_bins = [0, 5000, 10000, 15000, 20000, 25000, 30000, float('inf')] # Up to infinity
price_labels = ['0-5000', '5001-10000', '10001-15000', '15001-20000', '20001-25000', '25001-30000', '30000+']

# Categorize prices into groups
data['Price Group'] = pd.cut(data['Price'], bins=price_bins, labels=price_labels, right=False) # right=False to include lower bound

# Count the number of car names in each price group
price_group_counts = data.groupby('Price Group')['Name'].count()

# Create a Bar Chart to visualize price group distribution
plt.figure(figsize=(12, 7)) # Adjust figure size for better readability
price_group_counts.plot(kind='bar', color=sns.color_palette("pastel")) # Using pastel color palette
plt.title('Distribution of Car Names by Price Group')
plt.xlabel('Price Group (دينار)') # Label x-axis with price groups and currency
plt.ylabel('Number of Car Names')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
