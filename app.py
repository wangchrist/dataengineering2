#Dependencies
from flask import Flask,render_template,session,redirect,url_for, request, jsonify,send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired

from common.article import Article
from common.repository import ArticleRepository
from ingest.producer import send_to_producer

# App
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"

#Create a Form Class
class NameForm(FlaskForm):
    user_id = StringField("Put your id", validators=[DataRequired()])
    submit = SubmitField("Login")

class ArticleForm(FlaskForm):

    repository: ArticleRepository = None

    link = StringField("Put your link", validators=[DataRequired()])
    submit = SubmitField("Save")
    
    def save(self):
        # link = Article(**self.link) #la classe Article dans common article.py
        # self.__class__.repository.saveArticles(self, link)
        send_to_producer(self.link)


#Routers

#Home
@app.route("/",methods=["GET"])

def home():
    return render_template("home.html")

#login
@app.route("/login", methods=['GET', 'POST'])
def login():
    name = None
    form = NameForm()
    #Validate Form
    if  request.method == 'POST':
        name = form.user_id.data
        form.user_id.data = ''
        session['name'] = name
        print(f'Setting session name to {name}')
        return redirect(url_for('user'))
    print(f'Invalid form data: {form.errors}')
    return render_template("login.html",
                           form=form)

#user page / save articles
@app.route("/articles", methods=['GET', 'POST'])
def user():
    form = ArticleForm()
    name = session.get('name')
    print(f'Got session name: {name}')
    if not name:
        return redirect(url_for('login'))
    if request.method == "POST":
        form.save()
        form.link.data = ''
    return render_template('user.html', user_id=name, form=form)

#Create custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


#Run
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)