#Dependencies
from flask import Flask,render_template,session,redirect,url_for, request, jsonify,send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# App
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"

#Create a Form Class
class NameForm(FlaskForm):
    user_id = StringField("Put your id", validators=[DataRequired()])
    submit = SubmitField("Login")

class ArticleForm(FlaskForm):
    articles = [StringField("Article 1"), StringField("Article 2"), StringField("Article 3"), StringField("Article 4")]
    submit = SubmitField("Save")

    def get_articles(self):
        article_list = []
        for article in self.articles:
            if article.data:
                article_list.append(article)
        return article_list
    
    def save(self):
        articles = []
        for data in self.get_articles():
            article = Article(**data) #la classe Article dans common article.py
            articles.append(article)
        self.__class__.repositorysaveArticles(self, articles)


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

#user page / 10 articles
@app.route("/articles", methods=['GET', 'POST'])
def user(self):
    articles = None
    form = ArticleForm()
    name = session.get('name')
    print(f'Got session name: {name}')
    if not name:
        return redirect(url_for('login'))
    if request.method == "POST":
        form.save()
        form.articles.data = ''
    return render_template('user.html', user_id=name, articles=articles)

#Détail d'un article
@app.route("/articles/<article_id>", methods=['GET'])
def article(self, article_id):
    result = self.__class__.repository.findOneArticle(article_id)

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