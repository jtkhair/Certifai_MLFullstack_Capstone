>**Copyright &copy; 2021 Jauhari Khairuddin**<br>
>
>This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
> 
>This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
> 
>    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.<br>

# Powering Prediction App

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

4. To run the app, simply change the current working directory to app, and run the uvicorn as follows:
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
