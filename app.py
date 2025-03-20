
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import USvisaData, USvisaClassifier
from src.pipline.training_pipeline import TrainPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.Age: Optional[str] = None
        self.Gender: Optional[str] = None
        self.Social_Media_Hours: Optional[str] = None
        self.Exercise_Hours: Optional[str] = None
        self.Sleep_Hours: Optional[str] = None
        self.Screen_Time_Hours: Optional[str] = None
        self.Survey_Stress_Score: Optional[str] = None
        self.Wearable_Stress_Score: Optional[str] = None
        self.Academic_Performance: Optional[str] = None
        

    async def get_usvisa_data(self):
        form = await self.request.form()
        self.Age = form.get("Age")
        self.Gender = form.get("Gender")
        self.Social_Media_Hours = form.get("Social_Media_Hours")
        self.Exercise_Hours = form.get("Exercise_Hours")
        self.Sleep_Hours = form.get("Sleep_Hours")
        self.Screen_Time_Hours = form.get("Screen_Time_Hours")
        self.Survey_Stress_Score = form.get("Survey_Stress_Score")
        self.Wearable_Stress_Score = form.get("Wearable_Stress_Score")
        self.Academic_Performance = form.get("Academic_Performance")

@app.get("/", tags=["authentication"])
async def index(request: Request):

    return templates.TemplateResponse(
            "usvisa.html",{"request": request, "context": "Rendering"})


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_usvisa_data()
        
        usvisa_data = USvisaData(
                                Age= form.Age,
                                Gender = form.Gender,
                                Social_Media_Hours = form.Social_Media_Hours,
                                Exercise_Hours = form.Exercise_Hours,
                                Sleep_Hours= form.Sleep_Hours,
                                Screen_Time_Hours= form.Screen_Time_Hours,
                                Survey_Stress_Score = form.Survey_Stress_Score,
                                Wearable_Stress_Score= form.Wearable_Stress_Score,
                                Academic_Performance= form.Academic_Performance,
                                )
        
        usvisa_df = usvisa_data.get_usvisa_input_data_frame()

        model_predictor = USvisaClassifier()

        value = model_predictor.predict(dataframe=usvisa_df)[0]

        status = None
        if value == 0:
            status = "Low"

        elif value == 1:
            status = "Moderate"
        
        else:
            status = "High"

        return templates.TemplateResponse(
            "usvisa.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)