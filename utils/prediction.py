import tflite_runtime.interpreter as tflite
import numpy as np
# import os


def load_model(model_path):
    model = tflite.Interpreter(model_path=model_path)
    return model


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
