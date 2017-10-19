from flask import Flask, render_template, url_for, request, redirect, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bienvenue@17@localhost/recipes'
app.config['SECRET_KEY'] = 'hard to guess string' # for wtf forms
db = SQLAlchemy(app)

#db_connect = create_engine('sqlite:///chinook.db')
#app = Flask(__name__)
#api = Api(app)

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(80), unique=True)

    def getUsers(Resource):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from users") # This line performs query and returns json result
        return {'users': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

    

    

api.add_resource(Employees, '/user')
api.add_resource(Employees_Name, '/user/<uid>')
api.add_resource(Employees, '/category')
api.add_resource(Employees_Name, '/category/<cid>')
api.add_resource(Employees, '/recipe')
api.add_resource(Employees_Name, '/recipe/<rid>')
     

    def __repr__(self):
        return '<Role %r>' % self.name

class Categories(db.Model):
    __tablename__ = 'categories'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  index=True)
    description = db.Column(db.String(255),  index=True)

    def getCategories(Resource):
        passconn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    

    def __repr__(self):
        return '<User %r>' % self.name

class Recipes(db.Model):
    __tablename__ = 'recipes'
    rid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True)
    ingredients = db.Column(db.String(255), index=True)
    steps = db.Column(db.String(255), index=True)
    
    def getRecipes(Resource):
        conn = db_connect.connect()
        query = conn.execute("select * from users where uid =%d "  %int(uid))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/signIn')
def showSignIn():
    return render_template('signIn.html')

@app.route('/signUp')
def showSignUp():
    return render_template('signUp.html')

@app.route('/categories')
def showCategory():
    return render_template('categories.html')

@app.route('/recipes')
def showRecipe():
    return render_template('recipes.html')

@app.route('/<name>')
def homeReturn(name):
    if name == 'index':
        return redirect(url_for('index'))

@app.route('/addCategory')
def showAddCategory():
    return render_template('addCategory.html')

@app.route('/editCategory')
def showEditCategory():
    return render_template('editCategory.html')

@app.route('/addRecipe')
def showAddRecipe():
    return render_template('addRecipe.html')

@app.route('/editRecipe')
def showEditRecipe():
    return render_template('editRecipe.html')

@app.route('/send', methods=['GET', 'POST'])
def signIn():
    error = None
    if request.method == 'POST':
        email = request.form['inputEmail']
        pwd = request.form['inputPassword']
        if email != 'admin@admin.com' or pwd != 'admin':
            error = "Invalid credentials entered, Try again"
        else:
            session['logged_in'] = True
            return redirect(url_for('showCategory'))
    
    return render_template('signin.html', error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
