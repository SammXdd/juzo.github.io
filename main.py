from flask import Flask, render_template
import kmovies
import movies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4k')
def haha():
    return render_template('4k.html', movies=kmovies.cinefetch_4kmovies)

@app.route('/movies')
def hehe():
    return render_template('movies.html', movies=movies.cinefetch_movies)


# 4k Routes 🤍🤍

@app.route('/rednotice')
def rednotice():
    movie = 'Red Notice'  # this line to define the movie variable
    return render_template('4kmovies/rednotice/index.html', movie=movie, movies=kmovies.cinefetch_4kmovies)

@app.route('/extraction2')
def extraction2():
    movie = 'Extraction 2' # this line to define the movie variable
    return render_template('4kmovies/extraction2/index.html', movie=movie, movies=kmovies.cinefetch_4kmovies)

@app.route('/spidermanhc')
def spidermanhc():
    movie = 'Spiderman hc'  # this line to define the movie variable
    return render_template('4kmovies/spiderman-hc/index.html', movie=movie, movies=kmovies.cinefetch_4kmovies)

# 4k Routes Ends 🤍🤍

# --------------------------------------

# Movies Routes 💜💜

@app.route('/lupin')
def lupin():
    movie = 'Lupin'  # this line to define the movie variable
    return render_template('movies/lupin/index.html', movie=movie, movies=movies.cinefetch_movies)






# Movies Routes Ends 💜💜

# --------------------------------------

# Webseries Routes 🧡🧡



# Webseries Routes Ends 🧡🧡

if __name__ == '__main__':
    app.run(debug=True)
