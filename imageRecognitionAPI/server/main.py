import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

from imageRecognitionAPI.prediction.imagePrediction import predict, read_imagefile
from imageRecognitionAPI.schema import Symptom
from imageRecognitionAPI.prediction import symptom_check

app_desc = """<h2>Try my Image Prediction app by uploading any image with `predict/image`</h2>
<h2>Also, Try Covid Symptoms Checker `api/covid-symptom-check`.</h2> 
<h2>Note that it's just a learning app demo</h2>
<a href="https://github.com/KhomZ">Contact Me</a> 
<p><br>Developer: <a href="https://khomz.github.io/">Khom Raj Thapa Magar</a></p>"""


# app = FastAPI()
app = FastAPI(title='Tensorflow FastAPI Starter Pack', description=app_desc)


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction


@app.post("/api/covid-symptom-check")
def check_risk(symptom: Symptom):
    return symptom_check.get_risk_level(symptom)


if __name__ == "__main__":
    uvicorn.run(app, debug=True)