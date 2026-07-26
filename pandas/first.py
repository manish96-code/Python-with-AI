# Pandas : Pandas is an open-source data analysis and manipulation library for Python. It provides data structures like DataFrames and Series, which are designed for handling structured data efficiently. Pandas is widely used in data science, machine learning, and statistical analysis due to its powerful capabilities for data cleaning, transformation, and analysis.


import pandas as pd

mydataset = {
    "name": ["Manish", "Ramesh", "Suresh", "Rajesh"],
    "age": [25, 30, 35, 40],
}
newdataset = pd.DataFrame(mydataset)
print(newdataset)




