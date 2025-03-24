# Step 1: Import packages, functions, and classes
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import util as util
import csv

# Step 2: Get data
def organize_data(directory):
    plastics = []
    array = []
    currstr = ""
    # load csv file
    with open(directory, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (currstr!=row["PARTICLE"]):
                plastics.append(util.stringtofloat(array))
                array = []
                currstr=row["PARTICLE"]
            array.append(row["INTENSITY"])
        plastics.append(util.stringtofloat(array))

    return plastics

plastics = organize_data("Algorithm/PlasticData.csv")
plastics.pop(0)

array = []

x = np.array(plastics)
for i in range (len(plastics)):
    array.append(i%2)
y = np.array(array)

# Step 3: Create a model and train it
model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x, y)
#Step 4: Evaluate the model
p_pred = model.predict_proba(x)
y_pred = model.predict(x)
score_ = model.score(x, y)
conf_m = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)

cm = confusion_matrix(y, model.predict(x))

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()

print('p_pred:', p_pred, sep='\n', end='\n\n')