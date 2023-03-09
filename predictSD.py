import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

##
# Author: sohanjs111
#
#
##

# Read the models
bot_sr_y1_model = joblib.load("./Models/bot_sr_y1.sav")
bot_sr_y2_model = joblib.load("./Models/bot_sr_y2.sav")
bot_poly_y1_model = joblib.load("./Models/bot_poly_y1.sav")
bot_poly_y2_model = joblib.load("./Models/bot_poly_y2.sav")
evo_sr_y1_model = joblib.load("./Models/evo_sr_y1.sav")
evo_sr_y2_model = joblib.load("./Models/evo_sr_y2.sav")
evo_sr_y3_model = joblib.load("./Models/evo_sr_y3.sav")
evo_poly_y1_model = joblib.load("./Models/evo_poly_y1.sav")
evo_poly_y2_model = joblib.load("./Models/evo_poly_y2.sav")
evo_poly_y3_model = joblib.load("./Models/evo_poly_y3.sav")

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
      poly_obj= PolynomialFeatures(degree=2)
      return evo_poly_y1_model.predict(poly_obj.fit_transform(np.array([[speed]])))
    elif (drive_on == 2):
      poly_obj= PolynomialFeatures(degree=2)
      return evo_poly_y2_model.predict(poly_obj.fit_transform(np.array([[speed]])))
    elif (drive_on == 3):
      poly_obj= PolynomialFeatures(degree=2)
      return evo_poly_y3_model.predict(poly_obj.fit_transform(np.array([[speed]])))
    else:
      return -1

# Which robot?
def which_robot():
  print("Estimate the standard deviation for \n 1. TurtleBot \n 2. Evocortex")
  robot_no = input()
  robot_no = int(robot_no)
  if robot_no == 1 or robot_no == 2:
    return robot_no
  else: 
    print("Wrong choice! We only have model for Turtlebot and Evocortex \n")
    return -1 


# driving surface 
def surface_on(bot_or_evo):
  if bot_or_evo == 1: 
    print("What is the robot driving on? \n 1. Green Carpet \n 2. Floor")
    drive_on = input()
    drive_on = int(drive_on)
    if drive_on == 1 or drive_on == 2:
      return drive_on
    else: 
      print("Wrong choice! We only have Green carpet and floor SD for Turtlebot \n")
      return -1 
  elif bot_or_evo == 2:
    print("What is the robot driving on? \n 1. Green Carpet \n 2. Floor \n 3. Foam")
    drive_on = input()
    drive_on = int(drive_on)
    if drive_on == 1 or drive_on == 2 or drive_on == 3:
      return drive_on
    else: 
      print("Wrong choice! We only have Green carpet, floor and foam SD for Evocortex \n")
      return -1 

# Speed of the robot
def robot_speed():
  print("What is the speed of the Robot?")
  speed = input()
  speed = float(speed)
  return speed

if __name__ == "__main__":
  # robot
  robot_no = -1
  while(robot_no == -1):
    robot_no = which_robot()
  # Surface
  surface_no = -1
  while(surface_no == -1):
    surface_no = surface_on(robot_no)
  # Speed
  speed = robot_speed()
  # model
  res_poly = stand_d_poly(robot_no, surface_no, speed)
  res_lr = stand_d_sr(robot_no, surface_no, speed)
  if res_poly == -1 or res_lr == -1:
    print("Can not predict for this combination")
  else:
    print("Using Polynomial Regression the predicted standard devitation is", res_poly[0])
    print("\n")
    print("Using Linear Regression the predicted standard devitation is", res_lr[0])