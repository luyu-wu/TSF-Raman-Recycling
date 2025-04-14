import numpy as np
from numpy.linalg import norm
import csv


def load_data(directory, parameter):
    values = []
    # load csv file
    with open(directory, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # If we are looking for "Intensity", have array only include values with -4000<Wavenumber<0
        if parameter == "Intensity":
            for row in reader:
                if -4000 < float(row["Wavenumber"]) <= 0:
                    values.append(row[parameter])
        # Get all values of the CSV column into an array
        else:
            for row in reader:
                values.append(row[parameter])
    return values


# Convert an array of strings to type float
def stringtofloat(array):
    float_array = [float(string) for string in array]
    return float_array


# Retun cosine similarity value of two arrays
def cosine_similarity(A, B):
    cosine = np.dot(A, B) / (norm(A) * norm(B))
    return cosine


def r_squared(actual, predicted):
    SSR = 0
    SST = 0
    sum_y = 0

    for i in range(len(actual)):
        r2 = (actual[i] - predicted[i]) ** 2
        SSR += r2
        sum_y += actual[i]

    avg_y = sum_y / len(actual)

    for i in range(len(actual)):
        SST += (actual[i] - avg_y) ** 2

    return 1 - SSR / SST
