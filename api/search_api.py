from flask import Blueprint, request, redirect, url_for, render_template
# from flask_login import login_required, current_user
from constants.global_constants import GC
import spacy
from services.app_service import AppService
# from constants.app_constants import GC
# from spacy.lemmatizer import Lemmatizer, ADJ, NOUN, VERB


search_blueprint = Blueprint('search', __name__, template_folder="templates")


@search_blueprint.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':

        return render_template("search.html")
    else:
        searchWord = request.form.get('search', None)

        # lemmatizer = GC.SPACYLEMMATIZER.vocab.morphology.Lemmatizer

        # searchWord = lemmatizer(searchWord)

        print(searchWord)

        if not searchWord:
            return render_template("search.html", response="Enter a search word")

        response = AppService().searchWord(searchWord)

        print(response)

        return render_template("search.html", response=response)
