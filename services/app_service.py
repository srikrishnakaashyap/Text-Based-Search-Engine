from operator import index
from os import listdir
from os.path import isfile, join
import os
from constants.global_constants import GC
import json
import spacy
spacy.prefer_gpu()


class AppService:

    # Already Indexed? Should index?
    def isIndexed(self, first=True) -> bool:

        actual_file_list = self.getFilesInDirectory(
            os.path.join(os.getcwd(), GC.DATASET_FOLDER))

        index_file_file_list = GC.INDEXEDWORDS.get("files", None)

        if not index_file_file_list and first:
            self.indexFiles()
            return self.isIndexed(False)
        elif not index_file_file_list:
            return False

        self.removeIgnoredFiles(actual_file_list)

        areArraysSame = self.areArraysSame(
            actual_file_list, index_file_file_list)

        if not areArraysSame and first:
            self.indexFiles()
            return self.isIndexed(False)
        elif not areArraysSame and not first:
            return False

        return True

# Preprocessing function
    def indexFiles(self):

        indexDictionary = {}
        lemmatizer = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

        files_list = self.getFilesInDirectory(
            os.path.join(os.getcwd(), GC.DATASET_FOLDER))

        print(files_list)

        self.removeIgnoredFiles(files_list)

        files_dictionary = {}
        ctr = 0
        for file in files_list:
            files_dictionary[file] = ctr
            ctr += 1

        indexDictionary["files"] = files_list

        indexDictionary["index"] = {}

        for file in files_list:

            # print(file)
            with open(os.path.join(os.path.join(os.getcwd(), GC.DATASET_FOLDER), file), 'r+') as f:
                lineNumber = 0
                for line in f:
                    lineNumber += 1
                    if not line:
                        continue

                    lemmatized_line = lemmatizer(line)
                    for words in lemmatized_line:
                        if words.lemma_ not in indexDictionary["index"]:
                            d = {}
                            d[files_dictionary[file]] = {}
                            d[files_dictionary[file]]["occurrence"] = [lineNumber]
                            indexDictionary["index"][words.lemma_] = d
                        else:
                            d = indexDictionary["index"][words.lemma_]
                            if files_dictionary[file] not in d:
                                d[files_dictionary[file]] = {}
                                d[files_dictionary[file]]["occurrence"] = [
                                    lineNumber]
                            else:
                                d[files_dictionary[file]]["occurrence"].append(
                                    lineNumber)
                            indexDictionary["index"][words.lemma_] = d

        GC.INDEXEDWORDS = indexDictionary
        self.writeToFile()

    # Given a word, Return the words Occurrences

    @staticmethod
    def writeToFile():
        index_file_path = os.path.join(os.path.join(
            os.getcwd(), GC.DATASET_FOLDER), GC.JSON_FILE)

        mode = 'w+'
        with open(index_file_path, mode) as idxfile:
            try:
                json.dump(GC.INDEXEDWORDS, idxfile)
            except:
                print("ERROR WRITING")

            idxfile.close()

    def searchWord(self, word):

        if not GC.INDEXEDWORDS and self.isIndexed == True:

            self.isIndexed()
            self.searchWord(word)

        return GC.INDEXEDWORDS['index'][word]

    @staticmethod
    def getFilesInDirectory(path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles

    @staticmethod
    def removeIgnoredFiles(listOfFiles):
        for file in listOfFiles:
            print(file, file.split(".")[-1])
            if file.split(".")[-1] in GC.DATASET_DIRECTORY_IGNORE_LIST:
                # print(file)
                listOfFiles.remove(file)
        # print(listOfFiles)

    # Array 1 -> Freshly Computed File List
    # Array 2 -> Existing File List

    @staticmethod
    def areArraysSame(array1, array2):
        return list(set(array1) - set(array2)) == None
