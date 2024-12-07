# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/sneha/Documents/Python/Movie Analysis/IMDB Dataset.csv'  # Modify with your dataset path
movies_df = pd.read_csv(file_path)

# Display dataset information and first few rows
print(movies_df.info())
print(movies_df.head())

# Data Preprocessing
# Handle missing values - You can fill missing values or drop rows with missing values
movies_df = movies_df.dropna()  # Drop rows with missing values (you can also fill them)

# Basic Statistical Summary
print("Basic Statistics:")
print(movies_df.describe())

# Count the number of reviews by sentiment
sentiment_counts = movies_df['sentiment'].value_counts()

# Plot Sentiment Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='sentiment', data=movies_df, order=sentiment_counts.index, palette='viridis')
plt.title('Number of Reviews by Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

# Top 10 Positive Reviews
top_positive_reviews = movies_df[movies_df['sentiment'] == 'positive'].head(10)
print("Top 10 Positive Reviews:")
print(top_positive_reviews)

# Top 10 Negative Reviews
top_negative_reviews = movies_df[movies_df['sentiment'] == 'negative'].head(10)
print("Top 10 Negative Reviews:")
print(top_negative_reviews)

# Distribution of Review Lengths
movies_df['review_length'] = movies_df['review'].apply(len)

plt.figure(figsize=(8, 6))
sns.histplot(movies_df['review_length'], kde=True, color='blue', bins=30)
plt.title('Distribution of Review Lengths')
plt.xlabel('Review Length')
plt.ylabel('Frequency')
plt.show()

# Relationship Between Review Length and Sentiment
plt.figure(figsize=(10, 6))
sns.boxplot(x='sentiment', y='review_length', data=movies_df, palette='Set2')
plt.title('Review Length by Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Review Length')
plt.show()

