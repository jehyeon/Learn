from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

# ? What is Blueprint 
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
  # ! render_template -> project_name/app/templates/main/index.html
  return render_template('/main/index.html')