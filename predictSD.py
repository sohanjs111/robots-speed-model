import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Read the models
bot_sr_y1_model = joblib.load("./Models/bot_sr_y1.sav")
bot_sr_y2_model = joblib.load("./Models/bot_sr_y2.sav")
bot_poly_y1_model = joblib.load("./Models/bot_poly_y1.sav")
bot_poly_y2_model = joblib.load("./Models/bot_poly_y2.sav")
evo_sr_y1_model = joblib.load("./Models/evo_sr_y1.sav")
evo_sr_y2_model = joblib.load("./Models/evo_sr_y2.sav")
evo_sr_y3_model = joblib.load("./Models/evo_sr_y3.sav")

# fucntion for predicting SD for LR
def stand_d_sr(bot_or_evo, drive_on, speed):
  if (bot_or_evo == 1):
    if (drive_on == 1):
      return bot_sr_y1_model.predict(np.array([[speed]]))
    elif (drive_on == 2):
      return bot_sr_y2_model.predict(np.array([[speed]]))
    else:
      return -1
  if (bot_or_evo == 2):
    if (drive_on == 1):
      return evo_sr_y1_model.predict(np.array([[speed]]))
    elif (drive_on == 2):
      return evo_sr_y2_model.predict(np.array([[speed]]))
    elif (drive_on == 3):
      return evo_sr_y3_model.predict(np.array([[speed]]))
    else:
      return -1

# fucntion for predicting SD for LR
def stand_d_poly(bot_or_evo, drive_on, speed):
  if (bot_or_evo == 1):
    if (drive_on == 1):
      poly_obj= PolynomialFeatures(degree=3)
      return bot_poly_y1_model.predict(poly_obj.fit_transform(np.array([[speed]])))
    elif (drive_on == 2):
      poly_obj= PolynomialFeatures(degree=7)
      return bot_poly_y2_model.predict(poly_obj.fit_transform(np.array([[speed]])))
    else:
      return -1
  if (bot_or_evo == 2):
    if (drive_on == 1):
      return evo_sr_y1_model.predict(np.array([[speed]]))
    elif (drive_on == 2):
      return evo_sr_y2_model.predict(np.array([[speed]]))
    elif (drive_on == 3):
      return evo_sr_y3_model.predict(np.array([[speed]]))
    else:
      return -1

# Which robot?
print("Estimate the standard deviation for \n 1. TurtleBot \n 2. Evocortex")
bot_or_evo = input()
bot_or_evo = int(bot_or_evo)

# driving surface 
if bot_or_evo == 1: 
  print("What is the robot driving on? \n 1. Green Carpet \n 2. Floor")
  drive_on = input()
  drive_on = int(drive_on)
elif bot_or_evo == 2:
  print("What is the robot driving on? \n 1. Green Carpet \n 2. Floor \n 3. Foam")
  drive_on = input()
  drive_on = int(drive_on)
else: 
  print("Wrong choice! We only have model for Turtlebot and Evocortex")

# Speed of the robot
print("What is the speed of the Robot?")
speed = input()
speed = float(speed)

res = stand_d_poly(bot_or_evo, drive_on, speed)
#res = stand_d_sr(bot_or_evo, drive_on, speed)
if res == -1:
  print("Can not predict for this combination")
else:
  print("The predicted standard devitation is", res[0])