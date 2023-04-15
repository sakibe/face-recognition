from flask import Flask, render_template, request
import face_recognition

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('face.html') 

@app.route('/compare', methods=['POST','GET'])
def compare():
    if request.method == 'POST':
        known_image = face_recognition.load_image_file("D:\\Desktop\\face reco\\static\\sam.jpg")
        known_encoding = face_recognition.face_encodings(known_image)[0]

        file = request.files['file']
        unknown_image = face_recognition.load_image_file(file)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)

        return render_template('results.html', result=results[0])

if __name__ == "__main__":
    app.run(debug=True)
