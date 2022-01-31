import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#import statsmodels
#from statsmodels.graphics.mosaicplot import mosaic

df = pd.read_csv("./parties/bar_locations.csv")

print(df.keys())

print(df.head())


for s in df["Borough"].unique():
    print("Class: "+s)
    print(df.loc[df["Borough"]==s]["num_calls"].value_counts())