class IndexService:

    global indexedWords
    indexedWords = {}

    def isIndexed(self):

        # If is indexed and not indexedWords:
        #   indexedWords = read yaml
        # return True
        # else:
        #   call indexFiles
        #   return True
        # Except
        #   return False
        pass

    def indexFiles(self):
        pass

    def searchWord(self, word):

        if not indexedWords and self.isIndexed == True:

            self.isIndexed()
            self.searchWord(word)

        return indexedWords['index'][word]
