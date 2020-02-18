import glob
import os
import tqdm
import PIL.Image as Image

def crop_image(image_path):
    im = Image.open(image_path) 
    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = im.size 
    
    new_height = new_width = 256

    # Setting the points for cropped image 
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    
    # Cropped image of above dimension 
    im1 = im.crop((left, top, right, bottom)) 
    return im1

def save_image(img, original_path_name, output_dir):
    save_name = os.path.basename(original_path_name)
    save_path = output_dir+save_name
    img = img.save(save_path, mode='RGB') 

if __name__ == "__main__":
    search_dir = 'E:/Documents/Development/Datasets/Patterns/Raw/patterns_modern/*.png'
    output_dir = 'E:/Documents/Development/Datasets/Patterns/Preprocessed/patterns_modern/'

    img_list = [f for f in glob.glob(search_dir)]
    for image_path in tqdm.tqdm(img_list):
        try:
            cropped_image = crop_image(image_path)
            save_image(cropped_image, image_path, output_dir)
        except:
            continue