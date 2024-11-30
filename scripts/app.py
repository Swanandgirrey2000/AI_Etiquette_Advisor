from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Initialize Flask app and AI model
app = Flask(__name__)
etiquette_advisor = pipeline("text-generation", model="gpt2")

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API route for generating advice
@app.route('/get_advice', methods=['POST'])
def get_advice():
    data = request.json
    prompt = data.get('prompt', 'How to behave in general?')
    response = etiquette_advisor(prompt, max_length=50, num_return_sequences=1)
    return jsonify({"advice": response[0]['generated_text']})

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
