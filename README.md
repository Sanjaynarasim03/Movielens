# 🎬 MovieLens Recommendation System

A Flask-based web application that suggests personalized movie recommendations to users based on collaborative filtering. Built using the MovieLens 100K dataset and the Surprise library.

---

## 🧠 Features

* Uses Singular Value Decomposition (SVD) for collaborative filtering.
* Interactive web interface to select a user and get top 10 movie recommendations.
* Clean, responsive frontend using HTML and CSS.

---

## 📂 Project Structure

```
MovieLens-Recommender/
├── movielens_recommendation_backend.py   # Flask backend
├── templates/
│   └── movielens_recommendation_frontend.html  # Frontend UI
├── u.data                                # Ratings file (MovieLens 100K)
├── u.item                                # Movies file (MovieLens 100K)
├── requirements.txt                      # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository or extract the ZIP

```bash
git clone https://github.com/your-username/movielens-recommender.git
cd movielens-recommender
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Ensure you have the dataset files

Place the following files in the project directory:

* `u.data` — ratings
* `u.item` — movie titles

You can download the MovieLens 100K dataset from: [https://grouplens.org/datasets/movielens/100k/](https://grouplens.org/datasets/movielens/100k/)

### 4. Run the app

```bash
python movielens_recommendation_backend.py
```

Then open a browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🚀 Deployment Guide

To deploy this project publicly:

### Option 1: Deploy on Render

1. Create a GitHub repo and push your code.
2. Go to [https://render.com](https://render.com) and create a new Web Service.
3. Connect your GitHub repo and set:

   * Environment: Python 3
   * Start Command: `python movielens_recommendation_backend.py`
4. Add a `requirements.txt` and `render.yaml` (optional) for configuration.

### Option 2: Deploy on Heroku

1. Create a `Procfile` with:

```
web: python movielens_recommendation_backend.py
```

2. Initialize a git repo and commit all files.
3. Create Heroku app and deploy:

```bash
heroku create
git push heroku main
```

---

## 🙋‍♂️ Author

Sanjay Narasimhan.
