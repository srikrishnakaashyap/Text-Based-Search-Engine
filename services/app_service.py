from os import listdir
from os.path import isfile, join
import os
from constants.global_constants import GC
import json


class AppService:

    global indexedWords
    indexedWords = {}

    def isIndexed(self, first=True):

        index_file_path = os.path.join(os.path.join(
            os.getcwd(), GC.DATASET_FOLDER), GC.JSON_FILE)

        with open(index_file_path) as idxfile:
            index_file = json.load(idxfile)

            actual_file_list = self.get_files_in_directory(
                os.path.join(os.getcwd(), GC.DATASET_FOLDER))

            index_file_file_list = index_file.get("files", None)

            # if not index_file_file_list and first:
            #     self.indexFiles()
            #     return self.isIndexed(False)
            # elif not index_file_file_list:
            #     return False

            for i in actual_file_list:
                if i.split(".")[1] in GC.DATASET_DIRECTORY_IGNORE_LIST:
                    actual_file_list.remove(i)

            print(actual_file_list)

    def indexFiles(self):
        files_list = self.get_files_in_directory(
            os.path.join(os.getcwd(), GC.DATASET_FOLDER))

        print(files_list)

        pass

    def searchWord(self, word):

        if not indexedWords and self.isIndexed == True:

            self.isIndexed()
            self.searchWord(word)

        return indexedWords['index'][word]

    @staticmethod
    def get_files_in_directory(path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles


if __name__ == "__main__":
    ise = AppService()

    ise.isIndexed()
