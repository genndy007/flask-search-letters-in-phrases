from flask import Flask, render_template, request
# Flask is main object
# render_template for returning html pages with jinja inserting
# request is for handling form parameters filled by user
from search import search4letters
# our function for finding letters


app = Flask(__name__)

# starting point, here we take prompt
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
        'entry.html',
        the_title='Welcome to Estus Letter Search!'
    )

# final destination and results showing
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    print(request.url)
    print(request.args)
    letters = request.form['letters']
    found = search4letters(phrase, letters)
    return render_template(
        'results.html',
        the_title='Estus results:',
        the_phrase=phrase,
        the_letters=letters,
        the_results=found
    )


# for deploying, in deploy app.run() is useless
if __name__ == '__main__':
    app.run(debug=True)


