# Setup Instructions 

### 1. clone the repo
```shell
git clone https://github.com/a-b-h-a-y-s-h-i-n-d-e/Assignment_TechPranee.git
```
### 2. change the current directory
```shell
cd Assignment_TechPranee
```
### 3. install dependencies 
```shell
pip install -r requirements.txt
```
### 4. start the uvicorn server
```shell
uvicorn main:app --reload
```


# Test the API endpoints

### 1. /upload
```shell
curl -X POST "http://127.0.0.1:8000/upload"  -F "file=@dataset/realistic_machine_downtime_data.csv" && echo
```
![upload](/output1.png)
### 2. /train
```shell
curl -X POST "http://127.0.0.1:8000/train" && echo
```
![upload](/output2.png)
### 3. /predict
```shell
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"Temperature": 80, "Run_Time": 120}' && echo
```
![upload](/output3.png)
