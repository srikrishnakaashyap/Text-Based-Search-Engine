from flask import Blueprint, request, redirect, url_for, render_template
# from flask_login import login_required, current_user

from services.app_service import AppService
# from constants.app_constants import GC

search_blueprint = Blueprint('search', __name__, template_folder="templates")


@search_blueprint.route('/', methods=['GET', ])
def home():

    AppService().isIndexed()

    return render_template("search.html")
