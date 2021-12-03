from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
app.secret_key = 'bofa'

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def visit():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.post('/count')
def count():
    if request.form['change'] == 'plus':
        session['count'] += 1
    elif request.form['change'] == 'reset':
        session['count'] = 0
    return redirect('/')
    
@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')    

@app.errorhandler(404)
def error(error):
    return f'Page not found'

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
