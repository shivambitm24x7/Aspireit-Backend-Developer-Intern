from flask import Blueprint, request, jsonify
from textblob import TextBlob

ml = Blueprint('ml', __name__)

@ml.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']
    analysis = TextBlob(text).sentiment
    return jsonify({'polarity': analysis.polarity, 'subjectivity': analysis.subjectivity}), 200
