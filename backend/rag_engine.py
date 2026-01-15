from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_documents(path="documents/global_affairs.txt"):
    with open(path, "r", encoding="utf-8") as f:
        docs = f.read().split("\n\n")
    return [d.strip() for d in docs if len(d.strip()) > 50]

def retrieve_context(question, documents, top_k=4):
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([question] + documents)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    best_indices = similarities.argsort()[::-1][:top_k]
    return "\n".join([documents[i] for i in best_indices])