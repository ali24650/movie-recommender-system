from flask import Flask, render_template, request
from data_loader import load_videos
from recommender import recommend_videos

app = Flask(__name__)

VIDEOS = load_videos("videos.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        user_input = {
            "skill_level": request.form["skill_level"],
            "instrument": request.form["instrument"],
            "goal": request.form["goal"],
            "difficulty": int(request.form["difficulty"])
        }

        recommendations = recommend_videos(VIDEOS, user_input)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
