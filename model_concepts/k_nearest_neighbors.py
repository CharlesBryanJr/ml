'''file_name'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
print(" ")

'''

Type of Question:
- model concept

Question:
- Use the k-nearest neighbors algorithm 
to return the k nearest neighbors 
of the provided features.

These features are the result of a 
dimensionality reduction by PCA 
on some operating-system data related to processes 
and their intrusivity in some network.

You'll have access to an EXAMPLES dictionary, 
mapping each process identifier "pid_i"
to a respective dictionary
containing its associated features 
as well as a label 
representing whether the relevant process was intrusive
to the network. 
A label of 0 means that it wasn't intrusive, 
while a label of  1 means that it was intrusive.

Clarifying Questions / Insights:
- You should use the Euclidean distance as the distance metric when finding the k-nearest-neighbors.
- You shouldn't use any libraries that implement KNN for you.

Edge cases:
-

Base case:
-

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Ints
		- Arrays
			- Empty array
			- Nested or not nested
	
- If I knew / had this....
	-

Output:
-
'''

'''
Algo Time: O() | # Space: O():
-
-
    - Input:
        -
        -
    - Output:
'''
import math


# Time: O() | # Space: O()
# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nearest_neighbors = find_k_nearest_neighbors(examples, features, k)
    k_nearest_neighbors_labels = [examples[pid][label_key] for pid in k_nearest_neighbors]
    return round(sum(k_nearest_neighbors_labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    distances = {}
    for pid, features_label_map in examples.items():
        print("pid:", pid)
        print("features_label_map:", features_label_map)
        print("features_label_map:", features_label_map['features'])
        print("features:", features)
        distance = get_euclidean_distance(features, features_label_map['features'])
        print("distance:", distance)
        distances[pid] = distance
        print("distances[pid]:", distances[pid])
    return sorted(distances, key=distances.get)[0:k]


def get_euclidean_distance(features, other_features):
    if len(features) != len(other_features):
        raise ValueError("Features must have the same length as other_features")
    squared_difference = []
    for i in range(len(features)):
        squared_difference.append((other_features[i] - features[i]) ** 2)
    return math.sqrt(sum(squared_difference))


method = "find_k_nearest_neighbors"
examples = {
    "pid_0": {
        "features": [3.968642003034218, 3.9553899901567955, 3.8067717105202794],
        "is_intrusive": 0
    },
    "pid_1": {
        "features": [
            3.905930716908446, 3.9843869514613046, 3.999386668299634,
            4.064185093275078, 3.9867291766632458
        ],
        "is_intrusive": 0
    }
}
features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
k = 1
label_key = "is_intrusive"
print("method:", method)
print("features:", features)
print("k:", k)
print("predict_label:", predict_label(examples, features, k))
print(" ")
