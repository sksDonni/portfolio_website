from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/work')
def work():
	return render_template('work.html')

@app.route('/my_life')
def my_hobbies():
	return render_template('life.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

if __name__ == '__main__':
	app.run(debug=1)