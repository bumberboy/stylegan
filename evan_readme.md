# How to do stuff with this spaghetti monster

## 1. Dataset Pre-Preparation
The raw images must beet the following criteria:
1. They must be sRGB
2. They must be square shaped 
(at least in this repo, it can be modified to train/output on rectangles but it takes work)
3. Height/Width must be a power of 2 (ie. 2\*\*8 = 256, 2\*\*9 = 512)

A quick and dirty training script that I used is available at `pattern_utils/crop_images_256.py`
Just substitute `search_dir` and `output_dir` with your directory of images.
(Although the script is supposedly supposed to save images in sRGB,
for some reason during the next step, some of them turn out to have
more then 3 channels. I drop them via a try/except statement)

## 2. Dataset Prepration
Run the provided `dataset_tool.py`, using the `create_from_images` argument

[The readme provides instructions on how to use this script](README.md#Preparing-datasets-for-training)

## 3. Training
I've edited `train.py` to feed from a dataset I generated on my computer but you'll need to change the `dataset_dir` argument on `line 38`

For the rest of the info you need, [it's available in the readme as well](README.md#Training-networks)