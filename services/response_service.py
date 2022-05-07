from constants.global_constants import GC
from flask import jsonify, make_response
import json


class ResponseService:

    @staticmethod
    def create_empty_response():
        response = {}

        response["files"] = {}

        response["searchResults"] = {}

        return response

    @staticmethod
    def create_response(word):

        response = {}

        response["files"] = GC.INDEXEDWORDS["files"]

        # Sort searchResults based on the lenth of the occurrence list
        response["searchResults"] = GC.INDEXEDWORDS["index"][word]

        return response
