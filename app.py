from flask import Flask, render_template, url_for, request, redirect, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' # for wtf forms

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
