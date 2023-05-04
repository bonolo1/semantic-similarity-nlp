# 1. Run examples
import spacy
nlp = spacy.load('en_core_web_md')

print("-------------Similarity Between 3 Words---------------")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("-------------Similarity Between Multiple Words---------------")

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

print("-------------Similarity Between Sentences---------------")

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ", similarity)

# 2. Comment on what's interesting about the similarities between cat, monkey and banana.
# A: The fact that this model can pick up that banana and monkey are more similar than cat and banana as it shows that not only is similarity
# detected based on word/token categories (where both cat and monkey are animals), but it can pick up which animal eats which food (i.e. monkey and banana).
# This shows that NLP and the model is able to compare similarity of objects across various attribute dimensions to determine the similarity score.

print("\nThree-Word Alternative Example:")
# 3. Other Example
# A: Another example would be the objects: "festival", "stage" and "airport". Stage is most similar to festivals as stages are used at festivals but stages have
# the least similarity or relationship to airports. "Airport" is a bit more similar to "festival" however, as going to festivals may entail flights/travel to the
# festival. Therefore, the model is not only comparing across the same category for similarities, but different dimensions of object attributes and their
# relationship to one another.
word1 = nlp("festival")
word2 = nlp("stage")
word3 = nlp("airport")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# 4.Using the simpler language model ‘en_core_web_sm’ as opposed 'en_core_web_md'
# A: The similarity scores reduced substantially across all the texts.
# What's particularly noticeable is the substantial reduction in the similarity scores even within the complaints commmunication as well as within
# the recipe instructions. This shows the lower ability of the 'en_core_web_sm’ model to detect similarity than the 'en_core_web_md' model.
# In addition, when comparing the complaints to the similarities text, the scores are more varied in range with the 'en_core_web_sm’ model, which
# further supports that the 'en_core_web_sm’ model has a lower ability to detect similarity than the 'en_core_web_md' model.