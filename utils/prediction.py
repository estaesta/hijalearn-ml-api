import tflite_runtime.interpreter as tflite
import numpy as np
import csv

# import os


def load_labels_from_csv(csv_file_path):
    labels = []

    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if present

        labels.extend(row[0] for row in csv_reader)
    return labels


def load_model(model_path):
    return tflite.Interpreter(model_path=model_path)


def predict(model, spectrogram):
    model.allocate_tensors()
    # X = np.float32(X)
    input_details = model.get_input_details()
    output_details = model.get_output_details()

    spectrogram_expanded = np.expand_dims(spectrogram, axis=0)
    input_data = np.array(spectrogram_expanded, dtype=np.float32)
    model.set_tensor(input_details[0]["index"], input_data)
    model.invoke()
    result = model.get_tensor(output_details[0]["index"])
    return result


def inference(spectrogram, model_path, label_path):
    loaded_model = load_model(model_path)
    loaded_labels = load_labels_from_csv(label_path)

    result = predict(loaded_model, spectrogram)

    top_predict_index = np.argmax(result, axis=1)
    label_name = loaded_labels[int(top_predict_index)]
    probability = result[0,top_predict_index]

    return label_name, probability
