from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
import pandas as pd
import numpy as np
import io

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import train_test_split




app = FastAPI()
model = None
X_train = None
y_train = None

# datatype for input ( if int then will convert into float )
class PredictRequest(BaseModel):
    Temperature: float
    Run_Time: float





# this endpoint is use to upload the dataset
@app.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    global X_train, y_train 

    try:
        
        # reading csv file into pandas dataframe
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # for this case , we will check if relevant columns are present or not
        if 'Temperature' not in df.columns or 'Run_Time' not in df.columns or 'Downtime_Flag' not in df.columns:
            raise HTTPException(status_code=400, detail="Missing required columns in dataset.")
        
        X = df[['Temperature', 'Run_Time']]
        y = df['Downtime_Flag']

        # splitting the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        
        return {"message": "Dataset uploaded successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



# endpoint to train the model 
@app.post("/train")
async def train_model():
    global X_train, X_test, y_train, y_test, model


    # just for checking 
    if X_train is None or y_train is None:
        raise HTTPException(status_code=400, detail="No dataset uploaded.")
    
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    # testing on training set
    y_pred = model.predict(X_train)

    # here is the main part , to calculate performance metrics
    accuracy = accuracy_score(y_train, y_pred)
    f1 = f1_score(y_train, y_pred)


    return {
        "message": "Model trained successfully",
        "accuracy": accuracy,
        "f1_score": f1
    }


# now to predict 
@app.post("/predict")
async def predict_downtime(request: PredictRequest):

    global model
    
    if model is None:
        raise HTTPException(status_code=400, detail="Model is not trained.")
    
    # converting user input to np array
    input_data = np.array([[request.Temperature, request.Run_Time]])

    prediction = model.predict(input_data)
    # binary classification
    downtime = "Yes" if prediction[0] == 1 else "No"

    return {"Downtime": downtime}


