from constants.global_constants import GC
import os
import json


class InitializeApp:

    def __init__(self):

        GC.INDEXEDWORDS = self.loadIndex()

    def loadIndex(self):

        index_file_path = os.path.join(os.path.join(
            os.getcwd(), GC.DATASET_FOLDER), GC.JSON_FILE)

        mode = 'r+' if os.path.exists(index_file_path) else 'w+'

        index_file = {}
        with open(index_file_path, mode) as idxfile:
            try:
                index_file = json.load(idxfile)
            except:
                print("Index File is Blank or of wrong format")
            print(index_file, type(index_file))
            return index_file
