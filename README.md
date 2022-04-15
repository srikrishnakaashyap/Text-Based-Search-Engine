
# Problem Statement

Given a collection of huge text files or word documents, give a scalable algorithm to search for a given word. If not an exact match, return the closest match.

For example, let's Assume the text document contains the word documents contain following sentences:

Word Document 1: """Following mice attacks, caring farmers were marching to Delhi for better living conditions. Delhi police on Tuesday fired water cannons and tear gas shells at protesting farmers as they tried to break barricades with their cars, automobiles, and tractors. """

Word Document 2: """Sometimes to understand a word's meaning you need more than a definition; you need to see the word used in a sentence. At YourDictionary, we give you the tools to learn what a word means and how to use it correctly. With this sentence maker, simply type a word in the search bar and see a variety of sentences with that word used in different ways. Our sentence generator can provide more context and relevance, ensuring you use a word the right way. """

Word Document 3: '""Whether it’s simple sentences for those just learning the English language or phrasing for an academic paper, this easy-to-use sentence generator will help you choose your words with confidence. """

If we wish to find the documents which contain the word “sentence”; clearly, the word is present in document 2 and document 3, then the algorithm should return both the documents along with the occurrences of the word in the document.

# Why is this a Problem?

Searching for the word linearly after getting a search request is not feasible because the best algorithm to do so is in the order O(N) where N is the number of words. For relatively big and denser documents, this approach is not feasible because the time it takes to retrieve the results is high. Through this project, we wish to retrieve the results in logarithmic time. And also, if a user is interested in the word “march”; the search should also be able to retrieve the words “marching”, “Marching”, “MARCH”, etc. which have the same meaning but have different letters or differ by case, tense, etc. This search is not possible through the Linear Search.

# Approach

The idea behind the algorithm is to preprocess the documents, perform reverse indexing on the words and store them as the key-value pairs. However, before performing the indexing, the words should be preprocessed to store the words in a single tense and single case. Therefore, the steps performed are as follows:

 1. Perform Lemmatization on the words as we read them: Lemmatization
    usually refers to doing things properly with the use of a vocabulary
    and morphological analysis of words, normally aiming to remove
    inflectional endings only and to return the base or dictionary form
    of a word, which is known as the lemma.
 2. After Lemmatization, we perform indexing of the words. The idea of
    indexing is to: Store the words in a key-value pair; where the key
    is the word and the value is the list of documents and lines in
    which the words occur. We store this information in a YAML file to
    avoid recomputation in sorted order.
3. When we get a search query, we check the HashMap for an exact match and try to retrieve the occurrence of the word in Constant Time. If the word is present in the hashmap, we retrieve all the occurrences of the word in all the documents at a constant time. If the exact word is not present in the HashMap, we perform Binary Search on the already stored sorted words to retrieve the closest word.
4. Therefore, if we find an exact match, we can retrieve the result in a **Constant time** and if we don't find the exact match, we retrieve the closest word in the documents in a **Log(N)** time where N is the number of unique words present in all the documents.
