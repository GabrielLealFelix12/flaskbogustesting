from flask import Blueprint, render_template
PageHome = Blueprint('PageHome', __name__, template_folder='templates')

@PageHome.route('/PageHome')
def RenderHomePage():
    return render_template('PageHome/HomePageContent.html', content = 'ohio') 