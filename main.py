from flask import Flask, request, jsonify
import os
from utils.prediction import inference

from utils.preprocess import *

app = Flask(__name__)

model_list = [
    './model/model_full_inception_90.tflite',
    './model/model_polos_inception_98.tflite',
    './model/model_fathah_inception_93_2.tflite',
    './model/model_kasrah_inception_86.tflite',
    './model/model_dammah_inception_88.tflite'
]

label_csv_list = [
    "./labels_csv/full_labels.csv",
    "./labels_csv/polos_labels.csv",
    "./labels_csv/fathah_labels.csv",
    "./labels_csv/kasrah_labels.csv",
    "./labels_csv/dhammah_labels.csv",
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

    # override model
    # model = "0"

    # predict the audio file (use tflite model)
    labels_csv = label_csv_list[int(model)]
    model_path = model_list[int(model)]
    prediction, probability = inference(preprocessed_audio_file, model_path, labels_csv)

    probability = probability[0] * 100
    # to string
    probability = str(probability)

    # prediction = "alif"

    file_name = audio_file.filename
    print("The file name is: {}".format(file_name))

    # return the prediction
    response = {"prediction": prediction, "probability": probability}
    return jsonify(response)


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    app.run(debug=True, host="0.0.0.0", port=8080)
