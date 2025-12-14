import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')

# Load the spaCy model for lemmatization
nlp = spacy.load("en_core_web_sm")

# Load FAQ data
faq_df = pd.read_csv('faq_data.csv')  # Adjust the path if needed

# Preprocess text function (tokenization, stopword removal, and lemmatization)
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())  # Lowercase the text and tokenize it
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    
    # Lemmatize tokens using spaCy
    doc = nlp(" ".join(tokens))
    lemmatized_tokens = [token.lemma_ for token in doc]
    
    return " ".join(lemmatized_tokens)

# Apply preprocessing to the 'question' column
faq_df['processed_question'] = faq_df['question'].apply(lambda x: preprocess_text(x))

# Initialize the TF-IDF Vectorizer
tfidf = TfidfVectorizer()

# Fit the model on the processed FAQ questions
faq_tfidf = tfidf.fit_transform(faq_df['processed_question'])

# Function to find the most similar FAQ answer for a user's question
def get_best_match(user_input):
    # Preprocess the user input
    processed_input = preprocess_text(user_input)
    
    # Convert the user input to a TF-IDF vector
    user_tfidf = tfidf.transform([processed_input])
    
    # Compute cosine similarity between the user input and FAQ questions
    similarity = cosine_similarity(user_tfidf, faq_tfidf)
    
    # Get the index of the most similar question
    best_match_index = similarity.argmax()
    
    # Return the corresponding answer
    return faq_df.iloc[best_match_index]['answer']

# Example usage (You can remove or comment this out later)
if __name__ == "__main__":
    while True:
        user_input = input("Ask a question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        answer = get_best_match(user_input)
        print(f"Answer: {answer}")
