from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
recipes = []

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        recipes.append({'name': name, 'ingredients': ingredients, 'steps': steps})
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/view/<int:id>')
def view_recipe(id):
    recipe = recipes[id]
    return render_template('view_recipe.html', recipe=recipe)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
