import os

# Recorder and Data formatter
RATE = 16000
CHUNK = 512
CHANNELS = 1
DEVICE = -1
MAX_FREQ = 18
DURATION = 0.3
RECORDINGS_FOLDER = os.path.join(os.getcwd(), "./output/recordings")

# Trainer
FORMAT = ".npy"
DATA_PATH = os.path.join(os.getcwd(), "./output/data")
MODEL_PATH = os.path.join(os.getcwd(), "./output/vad.h5")
EPOCHS = 2500
BATCH_SIZE = 200
