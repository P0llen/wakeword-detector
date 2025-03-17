import torch
import librosa
import numpy as np
import os

class WakewordModel(torch.nn.Module):
    def __init__(self):
        super(WakewordModel, self).__init__()
        self.fc1 = torch.nn.Linear(13, 32)
        self.fc2 = torch.nn.Linear(32, 16)
        self.fc3 = torch.nn.Linear(16, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

# Load the trained model
model = WakewordModel()
model.load_state_dict(torch.load("wakeword_model.pth"))
model.eval()

# Function to extract features from a test sample
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

# Load the test sample
test_file_path = os.path.expanduser("~/wakeword_project/test/test_sample.wav")
if not os.path.exists(test_file_path):
    print(f"Error: {test_file_path} not found. Please record a test sample first!")
    exit()

features = extract_features(test_file_path)
input_tensor = torch.tensor(features, dtype=torch.float32).unsqueeze(0)

# Make a prediction
prediction = model(input_tensor).item()
print(f"Wake-word probability: {prediction:.4f}")

if prediction > 0.5:
    print("Wake word detected!")
else:
    print("No wake word detected.")

