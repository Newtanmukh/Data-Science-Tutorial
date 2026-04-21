import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    # 1. Convert to lowercase and tokenize
    text = text.lower()
    tokens = nltk.word_tokenize(text)

    # 2. Remove non-alphanumeric characters
    tokens = [word for word in tokens if word.isalnum()]

    # 3. Remove stopwords and punctuation
    # (Ensure 'stopwords' and 'string' are imported)
    tokens = [word for word in tokens if word not in stopwords.words('english') and word not in string.punctuation]

    # 4. Apply stemming
    # (Ensure 'ps' is initialized as PorterStemmer())
    tokens = [ps.stem(word) for word in tokens]

    return " ".join(tokens)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

buttonPressed = st.button('Predict')

if buttonPressed:
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")