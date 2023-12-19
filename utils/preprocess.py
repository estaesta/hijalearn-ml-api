import skimage.transform
import librosa
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_io as tfio


def process_audio_to_spectrogram(file_path, target_length=18000):
    # if not file_path.endswith(".wav"):
    #     raise ValueError("File path must be a .wav file")
    #
    wav, sr = librosa.load(file_path, sr=None)

    # Set a custom threshold for trimming (adjust as needed)
    custom_top_db = 20
    # Trim leading and trailing silence with a custom threshold
    wav, _ = librosa.effects.trim(wav, top_db=custom_top_db)

    # wav = tf.convert_to_tensor(wav, dtype=tf.float32)
    # sr = tf.convert_to_tensor(sr, dtype=tf.int32)
    wav = tfio.audio.resample(wav, rate_in=sr, rate_out=16000)
    # wav = librosa.resample(wav, orig_sr=sr, target_sr=16000)

    # Adjust the length of the audio sequence
    if len(wav) < target_length:
        # Zero-pad if the sequence is shorter than the target length
        pad_size = target_length - len(wav)
        # wav = tf.pad(wav, paddings=[[0, pad_size]])
        wav = np.pad(wav, (0, pad_size), mode="constant")
    elif len(wav) > target_length:
        # Trim if the sequence is longer than the target length
        wav = wav[:target_length]
    wav = np.array(wav)

    #         sr = float(sr)
    # Size of the Fast Fourier Transform (FFT), which will also be used as the window length
    n_fft = 1024

    # Step or stride between windows. If the step is smaller than the window length, the windows will overlap
    hop_length = 320
    #         sr = float(sr)
    window_type = "hann"
    mel_bins = 128
    # fmin = 0
    # fmax = None
    Mel_spectrogram = librosa.feature.melspectrogram(
        y=wav,
        sr=sr,
        n_fft=n_fft,
        hop_length=hop_length,
        win_length=n_fft,
        window=window_type,
        n_mels=mel_bins,
        power=2.0,
    )

    mel_spectrogram_db = librosa.power_to_db(Mel_spectrogram, ref=np.max)

    # change to rgb image
    cmap = plt.get_cmap("jet")  # You can choose other colormaps
    mel_spectrogram_db = cmap(mel_spectrogram_db / np.min(mel_spectrogram_db))[:, :, :3]

    # Resize Image
    # mel_spectrogram_db = tf.image.resize(mel_spectrogram_db, size=(128, 75)).numpy()
    desired_size = (128, 75)
    mel_spectrogram_db = skimage.transform.resize(
        mel_spectrogram_db,
        output_shape=desired_size,
        mode="edge",
        order=1,
        preserve_range=True,
    )

    return mel_spectrogram_db
