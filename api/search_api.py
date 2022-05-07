from flask import Blueprint, request, redirect, url_for, render_template
from constants.global_constants import GC
import spacy
from services.app_service import AppService


search_blueprint = Blueprint('search', __name__, template_folder="templates")


@search_blueprint.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':

        return render_template("search.html")
    else:
        requestWord = request.form.get('search', None)

        lemmatizedObject = GC.SPACYLEMMATIZER(requestWord)

        searchWord = lemmatizedObject[0].lemma_

        print("SEARCHING FOR", searchWord)

        if not searchWord:
            return render_template("search.html", response="Enter a search word")

        response = AppService().searchWord(searchWord)

        print(response)

        return render_template("search.html", response=response)
