from flask import Flask, session
from flask import jsonify
from flask import request

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return 'This is your homepage'


@app.route('/json')
def summary():
    d = {"key": "value"}
    return jsonify(d)

@app.route('/profile/<username>')
def profile(username):
    return 'Hello: %s' % username


@app.route('/user/<username>')
def show_user_profile(username):
    user = request.args.get('username')
    session["username"] = user
    return "OK"

@app.route('/user')
def show_user_args():
    user = request.args.get('username')
    session[user] = True
    return "OK: %s" % session


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/post_test', methods=["POST"])
def post_test():
    return "got: %s" % request.form['key']

@app.route('/delete_test/<username>', methods=["DELETE"])
def delete_test(username):
    return "got: %s" % username


if __name__ == "__main__":
    app.run(debug=True)
