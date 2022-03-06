import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getDataSource(data_path):
    days_present = []
    percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days_present.append(float(row["Days Present"]))
            percentage.append(float(row["Marks In Percentage"]))

    return {"x" : days_present, "y": percentage}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks vs Days Present :-  \n--->",correlation[0,1])

data_path  = "Student Marks vs Days Present.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)

with open(data_path)as f:
  df = pd.read_csv(f)
  fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
  fig.show()