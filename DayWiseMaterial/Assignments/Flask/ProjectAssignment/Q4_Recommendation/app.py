from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy movie data with categories
movie_data = {
    'movie1': {'action', 'comedy'},
    'movie2': {'drama', 'comedy'},
    'movie3': {'action', 'drama'},
    'movie4': {'horror'},
    'movie5': {'comedy'},
    'movie6': {'action'},
    'movie7': {'horror', 'comedy'},
}

def recommend_movies(category):
    recommended_movies = []
    for movie, categories in movie_data.items():
        if category in categories:
            recommended_movies.append(movie)
    return recommended_movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    category = request.form['category']
    recommended_movies = recommend_movies(category)
    return render_template('recommendations.html', category=category, recommendations=recommended_movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)
