from fastapi import FastAPI
from fastapi import UploadFile, File  # for file upload
import uvicorn  # Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.
from prediction import read_image, preprocess, predict

app = FastAPI()


@app.get('/index')
# get request api
# Similary, for post request we use app.post annotation
def hello_ikhomkodes(name: str):
    # return "Hello ikhomkodes!"
    return f"Hello {name}!"


# image classification api
@app.post('/api/predict')
def predict_image(file: UploadFile = File(...)):
    # Read the file uploaded by the user
    image = read_image(file)
    # after doing preprocessing
    image = preprocess(image)
    # make prediction
    image = predict(image)

    return image


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
