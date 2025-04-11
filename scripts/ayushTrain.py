import os
from PIL import Image
from tqdm import tqdm
import argparse
import pathlib

import torch
import clip
import pandas as pd


from load_aokvqa import load_aokvqa

dataset = pd.read_json("/Users/ayush/Desktop/Multimodal_Project/datasets/aokvqa/aokvqa_v1p0_train.json")

dataset.head