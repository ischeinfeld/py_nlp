from preprocessing import import_wsj, replace_rarities, word_counts

sentences = import_wsj("train")
print(sentences[1])


new_sentences = replace_rarities(sentences)
print(new_sentences[1])