import re
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from hitler import hitlers
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def remove_bracket_content(text):
    return re.sub(r'\[.*?\]', '', text)

#Grabbing some taylor lyrics from the taylor-swift-lyrics repo
df = pd.read_csv('taylor-swift-lyrics/songs.csv')
lyrics_list = df['Lyrics'].tolist()
hitler_lengths = [len(quote) for quote in hitlers]
individual_lines = []
for song in lyrics_list:
    song = remove_bracket_content(song)
    lines = song.split('\n')  # Split by newline character
    individual_lines.extend(lines)  # Extend the list with individual lines from the song
char_cutoff = np.mean(hitler_lengths) - 1.5*np.std(hitler_lengths)
print(f"{char_cutoff=}")
num_lines = len(individual_lines)
num_lines_above_cutoff = sum(len(line) >= char_cutoff for line in individual_lines)
print(f"{num_lines_above_cutoff=} out of {num_lines=} = {num_lines_above_cutoff/num_lines*100:.2f}%")
filtered_lyrics = [f"{line}." for line in individual_lines if len(line) >= char_cutoff]
print(f"compared to {len(hitlers)=}")

MODEL_CHOICE = "sentence_transformer" # word2vec or sentence_transformer

# tokenize and vectorize
tokenized_lyrics = [sentence.split() for sentence in filtered_lyrics]
print(f"{len(tokenized_lyrics)=}")
tokenized_hitlers = [sentence.split() for sentence in hitlers]
print(f"{len(tokenized_hitlers)=}")

model_lyrics = Word2Vec(tokenized_lyrics, vector_size=100, window=5, min_count=1, workers=4)
model_hitlers = Word2Vec(tokenized_hitlers, vector_size=100, window=5, min_count=1, workers=4)

def get_sentence_embedding(sentence, model):
    return np.mean([model.wv[word] for word in sentence if word in model.wv.index_to_key], axis=0)

if MODEL_CHOICE == "word2vec":
    # Generate embeddings for each set of sentences
    embeddings_lyrics = np.array([get_sentence_embedding(sentence, model_lyrics) for sentence in tokenized_lyrics])
    embeddings_hitlers = np.array([get_sentence_embedding(sentence, model_hitlers) for sentence in tokenized_hitlers])
elif MODEL_CHOICE == "sentence_transformer":
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    # Directly generate embeddings using Sentence Transformers
    embeddings_lyrics = model.encode(filtered_lyrics)
    embeddings_hitlers = model.encode(hitlers)
else:
    raise NotImplementedError

# Remove any NaN values (in case a sentence has no words found in the vocabulary)
embeddings_lyrics = np.array([emb for emb in embeddings_lyrics if not np.isnan(emb).any()])
embeddings_hitlers = np.array([emb for emb in embeddings_hitlers if not np.isnan(emb).any()])

similarity_matrix = cosine_similarity(embeddings_lyrics, embeddings_hitlers)

# Identify pairs with high similarity (e.g., threshold of 0.9)
threshold = 0.8
similar_pairs = np.argwhere(similarity_matrix > threshold)

num_similar_pairs = len(similar_pairs)

# display them
used_lyrics_indices = set()
used_hitler_indices = set()
z = 0

for i, j in similar_pairs:
    if i not in used_lyrics_indices and j not in used_hitler_indices:
        z += 1
        print(f"--- SIMILARITY PAIR #{z} ---")
        print(f"Taylor: {filtered_lyrics[i]}")
        print(f"Hitler: {hitlers[j]}")
        
        used_lyrics_indices.add(i)
        used_hitler_indices.add(j)

print(f"{z} similar pairs at threshold {threshold}")
