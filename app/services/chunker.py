# this fun takes text aand word as args and chunks down into small pieces that further
# go through miniLM-L6-v2 model for better working



def chunk_text(text, max_words=200):
    words = text.split()
    chunks = []
    
    
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
        
        
    return chunks


# this will returns resume in form of dict

# [chunk1, chunk2, chunk3] likt htis
