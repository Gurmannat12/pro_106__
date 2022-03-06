import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x" : coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml VS sleep in hours :-  \n--->",correlation[0,1])

data_path  = "cups of coffee vs hours of sleep.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)

with open(data_path)as f:
  df = pd.read_csv(f)
  fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
  fig.show()