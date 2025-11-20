import torch
import torch.nn as nn

class QuickDraw(nn.Module):
    def __init__(self, input_size=28, num_classes=15):
        super().__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 32, 5, bias=False),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(32, 64, 5, bias=False),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2)
        )
        # Output size: 64 × 4 × 4 = 1024
        self.flatten_dim = 64 * 4 * 4
        self.fc1 = nn.Sequential(nn.Linear(self.flatten_dim, 512), nn.Dropout(0.5))
        self.fc2 = nn.Sequential(nn.Linear(512, 128), nn.Dropout(0.5))
        self.fc3 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.fc2(x)
        return self.fc3(x)
