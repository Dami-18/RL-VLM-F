import pickle
import numpy as np

# Specify the path to your pickle file
file_path = "//home/theya/RL/RL-VLM-F/test_dummy/button-press-topdown/expert/data.pkl"
data_dict = {"observations": [], "actions": [], "images": [], "terminals": [], "images_path": []}
# Open and load the pickle file
with open(file_path, "rb") as f:
    data = pickle.load(f)
    data_dict["observations"].append(data["observations"])
    data_dict["actions"].append(data["actions"])
    data_dict["images"].append(data["images"])
    data_dict["terminals"].append(data["terminals"])
    data_dict["images_path"].append(data["images_path"])
    
data_dict["observations"] = np.concatenate(data_dict["observations"])
data_dict["actions"] = np.concatenate(data_dict["actions"])
data_dict["terminals"] = np.concatenate(data_dict["terminals"])
data_dict["images"] = np.concatenate(data_dict["images"])  
data_dict["images_path"] = np.concatenate(data_dict["images_path"])     

observations = data_dict['observations']
actions = data_dict['actions']
terminals = data_dict['terminals']
images = data_dict['images']
images_path = data_dict['images_path']

print("Images path: ", images_path)
# Print or use the loaded data
# print[data["images"].shap]
# print(data["images"][0])