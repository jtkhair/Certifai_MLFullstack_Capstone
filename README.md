# Passenger ship powering prediction web application with Scikit-learn, Jinja, boostrap, FastAPI and Docker container 

## Introduction
This web application is developed based on the joint work between the [Marine Technology Centre](http://www.mtc-utm.my/)
, Universiti Teknologi Malaysia (UTM) and the [Hiekata Laboratory](https://is.edu.k.u-tokyo.ac.jp/top), University of 
Tokyo (UTokyo). The details of ship powering prediction modelling is described in the 
[research paper](https://bit.ly/3mL96kz) presented in the International Conference on Design and Concurrent Engineering 
2021 & Manufacturing System Conference 2021

> _Adi Maimun, Hiekata Kazuo, Jauhari Khairuddin, Siow Chee Loon and Arifah Ali, : "Estimation of Ship Powering in
> Preliminary Ship Design Using Graph Theory and Machine Learning Method". In the International Conference on Design
> and Concurrent Engineering 2021 & Manufacturing System Conference 2021, Sep 2021, Japan_

## Getting started
1. Clone the repo by running this command in the terminal:

```
git clone https://github.com/jtkhair/Certifai_MLFullstack_Capstone
```

2. Make sure to run the command git pull (if you already cloned this repo). In the cloned repo directory, run this 
command in the terminal:
```
git pull https://github.com/jtkhair/Certifai_MLFullstack_Capstone
```

3. Build docker image by running below commands in the terminal (make sure docker is running):
```
docker build -t aishipwebapp:1.0 .
```

4. Run the docker container by running below command in the terminal:
```
docker run -d --name aishipwebapp -p 80:80 aishipwebapp:1.0
```

5. Go to the link http://127.0.0.1:80 to use the web app

6. Input dataset *.csv file and click submit to perform the prediction. Note that the *.csv file must follow the set 
format

## Input data format, range and description

Parameter | LWL | B | T | L/B | B/T | Disp | CB |Vs | Fn | P | 
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |
Range | 80 - 240 | 15 - 32 | 3 - 8 | 3.5 - 9.0 | 3.0 - 5.5 | 2500 - 32000 | 0.5 - 0.7 | 14.5 - 30.5 | 0.20 - 0.40 | 3000 - 70000 | 

### Acronym
- Waterline Length in m, LWL
- Breadth in m, B
- Draught in m, T
- Length-to-Breadth ratio, L/B
- Breadth-to-Draught ratio, B/T
- Displacement in t, Disp
- Block Coefficient, CB
- Service Speed in kn, Vs
- Froude Number, Fn
- Brake KiloWatt Power in kW, P
