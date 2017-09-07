from flask import Flask 
#/usr/lib/python2.7/dist-packages/flask

app = Flask(__name__) #make instance

@app.route('/')
def index():
	return 'This is the Homepage'

@app.route('/profile/<username>')
def profile(username):
	return 'Hey there %s' % username

@app.route('/post/<int:post_id>')
def post(post_id):
	return '<h2>Post ID is %d</h2>' % post_id

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888) 
