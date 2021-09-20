# Passenger Ship Powering Prediction App

## Passenger ship powering prediction web application with Scikit-learn, Jinja, boostrap and  FastAPI


## Getting started
1. Clone the repo by running this command at the terminal:

```
git clone https://github.com/jtkhair/Certifai_MLFullstack_Capstone
```


2. Before running this web app, make sure to run the command git pull (if you already cloned this repo). <br/>
In your directory(the cloned repo) run this command at terminal:
```
git pull https://github.com/jtkhair/Certifai_MLFullstack_Capstone
```

3. Install the latest requirements as follows:
```
pip install -r requirements.txt
```

4. To run the app, simply change the current working directory to app, and run the uvicorn as follows in the terminal:
```
cd app
uvicorn main:app --reload
```

5. Go to the link http://127.0.0.1:8000 to use the web app

6. Input dataset *.csv file and click submit to perform the prediction

## Input data format, range and description

Parameter | LWL | B | T | L/B | B/T | Disp | CB |Vs | Fn | P | 
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |
Range | 80 - 240 | 15 - 32 | 3 - 8 | 3.5 - 9.0 | 3.0 - 5.5 | 2500 - 32000 | 0.5 - 0.7 | 14.5 - 30.5 | 0.20 - 0.40 | 3000 - 70000 | 

### Acronym
- Waterline Length, LWL
- Breadth, B
- Draught, T
- Length-to-Breadth ratio, L/B
- Breadth-to-Draught ratio, B/T
- Displacement, Disp
- Block Coefficient, CB
- Service Speed, Vs
- Froude Number, Fn
- Brake KiloWatt Power, P
