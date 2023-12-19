from flask import Flask, request, jsonify
import os

from utils.preprocess import process_audio_to_spectrogram

app = Flask(__name__)

model_list = [
    './model/model_full_inception_90.tflite',
    './model/model_polos_inception_98.tflite'
]

@app.route("/")
def index():
    return "Hello World!"


@app.route("/predict", methods=["POST"])
def predict():
    # Authenticate the request
    # TODO (mid priority)

    # Get the audio file from the request
    audio_file = request.files["file"]
    # Get the label from the request
    label = request.form.get("label")
    # Get the model from the request (based on the moduleId)
    model = request.form.get("model")

    # check if file is an audio file
    # TODO (low priority)

    # preprocess the audio file
    # di file preprocess sudah kutambahin
    # ku edit dikit dari kode anak ml biar gk usah import tensorflow
    preprocessed_audio_file = process_audio_to_spectrogram(audio_file)

    # predict the audio file (use tflite model)
    # TODO
    prediction = "alif"

    file_name = audio_file.filename
    print("The file name is: {}".format(file_name))

    # return the prediction
    return prediction


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    app.run(debug=True, host="0.0.0.0", port=8080)
