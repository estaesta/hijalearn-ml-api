TODO
---
- [ ] Authentication
- [x] Preprocessing
- [x] Prediction using tflite runtime
- [x] Dockerize

## Model
https://drive.google.com/drive/folders/14YmzV3eUagTSMGXVJ_qW6ETnQfW8sai1?usp=drive_link

## How to run
1. Clone this repository
2. Put the model in `models` folder
3. Run `docker build -t <image-name> .`
4. Run `docker run -p 5000:5000 <image-name>`

POST /predict
---
body (form-data):
- file: wav file
- model: model name("1" for polos, "2" for fathah, "3" for kasrah, "4" for dammah)

response:
```
{
	"prediction": "Tu",
	"probability": "83.68396759033203"
}
```
