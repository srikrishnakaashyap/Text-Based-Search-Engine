from constants.global_constants import GC


class ResponseService:

    @staticmethod
    def create_response(word):

        response = {}

        response["files"] = GC.INDEXEDWORDS["files"]

        # Sort searchResults based on the lenth of the occurrence list
        response["searchResults"] = GC.INDEXEDWORDS["index"][word]

        return response
