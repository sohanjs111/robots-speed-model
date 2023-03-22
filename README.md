# robots-speed-model
Regression model to find the standard deviation for robot speed with different friction coefficient

To run this clone the repository and run predictSD.py file.

## Contents
The repository contains The dataset the model that was trained with and the models iteself. 

### [Datasets](https://github.com/sohanjs111/robots-speed-model/tree/main/Dataset)
1. Evocortex.csv - contains the Standard Deviation for Evocortex robot with friction coefficient to that of Green carpet, Floor and the Foam with respect to speed.
2. Turtlebot3.csv - contains the Standard Deviation for Turtlebot3 robot with friction coefficient to that of Green carpet, Floor with respect to speed. 
3. evocortex_ml.csv - contains the Standard Deviation for Evocortex robot with friction coefficient and speed. (two dependable variable)

### [Models](https://github.com/sohanjs111/robots-speed-model/tree/main/Models)
1. bot_sr_y1.sav - Simple Linear regression model for Turtlebot3 on the Green carpet
2. bot_sr_y2.sav - Simple Linear regression model for Turtlebot3 on the Floor
3. evo_sr_y1.sav - Simple Linear regression model for Evocortex on the Green carpet
4. evo_sr_y2.sav - Simple Linear regression model for Evocortex on the Floor
5. evo_sr_y3.sav - Simple Linear regression model for Evocortex on the Foam
6. bot_poly_y1.sav - Polynomial Linear regression model for Turtlebot3 on the Green carpet
7. bot_poly_y2.sav - Polynomial Linear regression model for Turtlebot3 on the Floor
8. evo_poly_y1.sav - Polynomial Linear regression model for Evocortex on the Green carpet
9. evo_poly_y2.sav - Polynomial Linear regression model for Evocortex on the Floor
10. evo_poly_y3.sav - Polynomial Linear regression model for Evocortex on the Foam
11. evo_ml.sav - Multiple Linear regression model for Evocortex for different Friction coefficient

## To run the program:
### Run the file
```
python3 predictSD.py
```
### Install the necessary packages to run predictSD.py
1. Scikit library to the model
```
pip3 install -U scikit-learn scipy matplotlib
```
2. numpy
```
pip3 install numpy
```
3. Joblib to read the models
```
pip3 install joblib
```

The Regression models were built using Juypter Notebook, while the prediction is done using only python 3.




