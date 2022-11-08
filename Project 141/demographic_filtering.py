#Importing modules required
import numpy as np
import pandas as pd

#Reading the file
df = pd.read_csv("articles.csv")

# Sort
df = df.sort_values(['total_events'], ascending = [False])

# Get the top 20 articles stored in the output var
output = df[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()