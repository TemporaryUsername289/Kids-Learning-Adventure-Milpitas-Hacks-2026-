from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Expanded Lesson Database (10 items each)
LESSON_DATA = {
    "letters": [
        {"visual": "a", "answer": "Apple"}, {"visual": "b", "answer": "Bear"},
        {"visual": "c", "answer": "Cat"}, {"visual": "d", "answer": "Dog"},
        {"visual": "e", "answer": "Egg"}, {"visual": "f", "answer": "Fish"},
        {"visual": "g", "answer": "Giraffe"}, {"visual": "h", "answer": "Hat"},
        {"visual": "i", "answer": "Ice"}, {"visual": "j", "answer": "Jam"}
    ],
    "colors": [
        {"visual": "🟥", "answer": "Red"}, {"visual": "🟦", "answer": "Blue"},
        {"visual": "🟨", "answer": "Yellow"}, {"visual": "🟩", "answer": "Green"},
        {"visual": "🟧", "answer": "Orange"}, {"visual": "🟪", "answer": "Purple"},
        {"visual": "🟫", "answer": "Brown"}, {"visual": "⬛", "answer": "Black"},
        {"visual": "⬜", "answer": "Gray"}, {"visual": "🩷", "answer": "Pink"}
    ],
    "items": [
        {"visual": "🪑", "answer": "Chair"}, {"visual": "🛏️", "answer": "Bed"},
        {"visual": "🥄", "answer": "Spoon"}, {"visual": "🔑", "answer": "Key"},
        {"visual": "⌚", "answer": "Watch"}, {"visual": "📱", "answer": "Phone"},
        {"visual": "📖", "answer": "Book"}, {"visual": "🎒", "answer": "Bag"},
        {"visual": "🖊️", "answer": "Pen"}, {"visual": "☂️", "answer": "Umbrella"}
    ],
    "shapes": [
        {"visual": "⭕", "answer": "Circle"}, {"visual": "🟥", "answer": "Square"},
        {"visual": "🔺", "answer": "Triangle"}, {"visual": "⭐", "answer": "Star"},
        {"visual": "💎", "answer": "Diamond"}, {"visual": "⬠", "answer": "Pentagon"},
        {"visual": "⬡", "answer": "Hexagon"}, {"visual": "🟨", "answer": "Square"},
        {"visual": "🌙", "answer": "Crescent"}, {"visual": "🔲", "answer": "Square"}
    ],
    "math": [
        {"visual": "1+1", "answer": "2"}, {"visual": "2+2", "answer": "4"},
        {"visual": "3+1", "answer": "4"}, {"visual": "5+5", "answer": "10"},
        {"visual": "10-2", "answer": "8"}, {"visual": "6+4", "answer": "10"},
        {"visual": "5-2", "answer": "3"}, {"visual": "8+1", "answer": "9"},
        {"visual": "7-3", "answer": "4"}, {"visual": "9-5", "answer": "4"}
    ],
    "feelings": [
        {"visual": "😊", "answer": "Happy"}, {"visual": "😢", "answer": "Sad"},
        {"visual": "😡", "answer": "Mad"}, {"visual": "😴", "answer": "Sleepy"},
        {"visual": "😲", "answer": "Surprised"}, {"visual": "😎", "answer": "Cool"},
        {"visual": "🤒", "answer": "Sick"}, {"visual": "🤔", "answer": "Thinking"},
        {"visual": "😱", "answer": "Scared"}, {"visual": "😍", "answer": "Loving"}
    ],
    "weather": [
        {"visual": "☀️", "answer": "Sunny"}, {"visual": "🌧️", "answer": "Rainy"},
        {"visual": "❄️", "answer": "Snowy"}, {"visual": "☁️", "answer": "Cloudy"},
        {"visual": "💨", "answer": "Windy"}, {"visual": "🌩️", "answer": "Stormy"},
        {"visual": "🌫️", "answer": "Foggy"}, {"visual": "🌈", "answer": "Rainbow"},
        {"visual": "🌡️", "answer": "Hot"}, {"visual": "🥶", "answer": "Cold"}
    ],
    "animals": [
        {"visual": "🐶", "answer": "Dog"}, {"visual": "🐱", "answer": "Cat"},
        {"visual": "🐮", "answer": "Cow"}, {"visual": "🦁", "answer": "Lion"},
        {"visual": "🐘", "answer": "Elephant"}, {"visual": "🦒", "answer": "Giraffe"},
        {"visual": "🐒", "answer": "Monkey"}, {"visual": "🐢", "answer": "Turtle"},
        {"visual": "🐰", "answer": "Rabbit"}, {"visual": "🐦", "answer": "Bird"}
    ],
    "vehicles": [
        {"visual": "🚗", "answer": "Car"}, {"visual": "🚂", "answer": "Train"},
        {"visual": "✈️", "answer": "Airplane"}, {"visual": "🚲", "answer": "Bicycle"},
        {"visual": "🚁", "answer": "Helicopter"}, {"visual": "⛵", "answer": "Boat"},
        {"visual": "🚜", "answer": "Tractor"}, {"visual": "🚑", "answer": "Ambulance"},
        {"visual": "🚀", "answer": "Rocket"}, {"visual": "🚌", "answer": "Bus"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/lesson/<category>')
def get_lesson(category):
    if category not in LESSON_DATA:
        return jsonify({"error": "Not found"}), 404
    
    items = LESSON_DATA[category]
    lesson = random.choice(items)
    
    # Generate 3 wrong answers (total of 4 options)
    all_answers = [i["answer"] for i in items]
    wrong_answers = [a for a in all_answers if a != lesson["answer"]]
    options = [lesson["answer"]] + random.sample(wrong_answers, 3)
    random.shuffle(options)
    
    return jsonify({
        "visual": lesson["visual"],
        "correct": lesson["answer"],
        "options": options
    })

if __name__ == '__main__':
    app.run(debug=True)