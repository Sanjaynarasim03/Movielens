from flask import Flask, render_template, request
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

app = Flask(__name__)

# Load MovieLens 100K dataset (assumes u.data & u.item files available)
rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=rating_cols, encoding='latin-1')

movie_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
              'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
              'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
              'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv('u.item', sep='|', names=movie_cols, encoding='latin-1', usecols=[0, 1])

# Prepare dataset for Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

# Train SVD model
model = SVD()
model.fit(trainset)

# Get all unique user_ids and movie_ids
user_ids = ratings['user_id'].unique().tolist()
movie_id_to_title = dict(zip(movies.movie_id, movies.title))

@app.route('/')
def home():
    return render_template('movielens_recommendation_frontend.html', user_ids=user_ids)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])

    # Recommend movies the user hasn't rated yet
    user_rated_movies = ratings[ratings['user_id'] == user_id]['movie_id'].tolist()
    unseen_movies = [mid for mid in movie_id_to_title if mid not in user_rated_movies]

    # Predict ratings for unseen movies
    predictions = [(mid, model.predict(user_id, mid).est) for mid in unseen_movies]
    top_predictions = sorted(predictions, key=lambda x: x[1], reverse=True)[:10]
    recommended_titles = [movie_id_to_title[mid] for mid, _ in top_predictions if mid in movie_id_to_title]

    return render_template(
        'movielens_recommendation_frontend.html',
        user_ids=user_ids,
        selected_user=user_id,
        recommendations=recommended_titles
    )

if __name__ == '__main__':
    app.run(debug=True)
