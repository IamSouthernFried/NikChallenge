from PIL import Image
import numpy as np

# Load the image
image_path = r'C:\Users\sfrie\Pictures\southernfried.nfts_surreal_ethereal_cute_good_vibes_happy_Chris_02c24189-e686-4166-b390-9666020e286e~2.jpg'
original_image = Image.open(image_path)
original_image_array = np.array(original_image)

# Define the color percentage for the altered images
blue_percentage = 0.60  # 60% blue

# Calculate the number of pixels to change
total_pixels = original_image_array.shape[0] * original_image_array.shape[1]
blue_pixels = int(total_pixels * blue_percentage)

# Create 10 images
for i in range(10):
    # Copy the original image array to avoid cumulative changes
    image_array = np.array(original_image_array)

    # Only alter 6 images (60% of 10 images = 6 images)
    if i < 6:  # Modify the first 6 images
        # Randomly select pixels and change their colors to blue
        indices = np.random.permutation(total_pixels)[:blue_pixels]
        for idx in indices:
            x, y = divmod(idx, image_array.shape[1])
            image_array[x, y] = [0, 0, 255]  # Blue color
    
    # Save the image
    modified_image = Image.fromarray(image_array)
    modified_image.save(f'image_{i+1}.jpg')
