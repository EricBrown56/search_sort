from flask import Flask, request, jsonify

#http://127.0.0.1:5000/search?title=some-movie

app = Flask(__name__)
@app.route('/search', methods=['GET'])

def search():
    video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]
    title = request.args.get('title')
    if title in video_titles:
        print(title)
        return jsonify('success'), 200
    else:
        print('Error retrieving title')
        return jsonify('Title not found'), 404




if __name__ == '__main__':
    app.run(debug=True)