import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample documents
documents = [
    "Artificial Intelligence is transforming industries.",
    "Machine Learning enables computers to learn from data.",
    "Football is a popular sport worldwide.",
    "Deep learning is a subset of machine learning.",
    "Natural Language Processing helps machines understand text."
]

# Convert documents to embeddings
doc_embeddings = model.encode(documents)

# Convert to float32 (FAISS requirement)
doc_embeddings = np.array(doc_embeddings).astype("float32")

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

print("🚀 FAISS Semantic Search Ready\n")

while True:
    query = input("Enter your query (type 'quit' to exit): ")

    if query.lower() == "quit":
        break

    # Encode query
    query_vector = model.encode([query]).astype("float32")

    # Search top 1 match
    distances, indices = index.search(query_vector, k=1)

    best_idx = indices[0][0]

    print("\nMost Relevant Document:")
    print(documents[best_idx])
    print("Distance Score:", round(float(distances[0][0]), 3))
    print("-" * 50)