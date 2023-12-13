from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the audio file from the request
    audio_file = request.files['file']
    # Get the label from the request
    label = request.form.get('label')

    # check if file is an audio file 
    # TODO (low priority)

    # preprocess the audio file
    # TODO
    preprocessed_audio_file = None

    # predict the audio file
    # TODO
    prediction = "alif"

    file_name = audio_file.filename
    print('The file name is: {}'.format(file_name))

    # return the prediction
    return prediction

if __name__ == '__main__':
    app.run(port=5000, debug=True)
