import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Download NLTK resources if not already available
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\d+', '', text)      # Remove numbers
    text = text.lower()                 # Convert to lowercase
    tokens = word_tokenize(text)        # Tokenize
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

print("Starting preprocessing...")

# Process data in chunks
chunk_size = 10000
chunks = pd.read_csv('combined_news_dataset.csv', chunksize=chunk_size)
processed_chunks = []

for chunk in chunks:
    chunk['cleaned_content'] = chunk['text'].apply(preprocess_text)
    processed_chunks.append(chunk)

# Combine processed chunks
processed_data = pd.concat(processed_chunks, ignore_index=True)
processed_data.to_csv('preprocessed_news_dataset.csv', index=False)

# Feature extraction
print("Performing feature extraction...")
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(processed_data['cleaned_content'])
y = processed_data['Label']

# Save vectorizer
print("Saving vectorizer...")
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Preprocessing complete.")
