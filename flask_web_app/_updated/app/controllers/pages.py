from flask import render_template, Blueprint, request
from app.forms import *

blueprint = Blueprint('pages', __name__)


################
#### routes ####
################


@blueprint.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@blueprint.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

