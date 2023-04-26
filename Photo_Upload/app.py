from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    image = request.files['image']
    image.save('uploads/' + image.filename)
    return 'Image uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)

    