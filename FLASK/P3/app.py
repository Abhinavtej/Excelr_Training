from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    result = f"Entered Prompt: {prompt}","Generated Text: This is a generated text based on the prompt."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)