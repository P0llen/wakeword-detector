import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split

# Load extracted features
wakeword_features = np.load(os.path.expanduser("~/wakeword_project/features/wakeword.npy"))
not_wakeword_features = np.load(os.path.expanduser("~/wakeword_project/features/not_wakeword.npy"))

# Create labels: 1 for wakeword, 0 for not-wakeword
X = np.vstack((wakeword_features, not_wakeword_features))
y = np.hstack((np.ones(len(wakeword_features)), np.zeros(len(not_wakeword_features))))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

# Define a simple neural network
class WakewordModel(nn.Module):
    def __init__(self):
        super(WakewordModel, self).__init__()
        self.fc1 = nn.Linear(13, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

# Initialize model, loss function, and optimizer
model = WakewordModel()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
epochs = 50
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# Save the trained model
torch.save(model.state_dict(), "wakeword_model.pth")
print("Model training complete! Saved as wakeword_model.pth")

