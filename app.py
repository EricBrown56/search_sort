from flask import Flask, request, jsonify
from merge_sort import merge_sort
from binary_search import binary_search

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
    merge_sort(video_titles)
    print(video_titles)
    title = request.args.get('title')
    binary_search(video_titles, title)
    result = binary_search(video_titles, title)
    if result != -1:
        print(title)
        return jsonify('success'), 200
    else:
       print('Error retrieving title')
       return jsonify('Title not found'), 404

    
    #return str(binary_search(video_titles, title))

if __name__ == '__main__':
    app.run(debug=True)