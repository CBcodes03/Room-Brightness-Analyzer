import cv2
import numpy as np

def calculate_room_brightness(image_path, grid_rows=3, grid_cols=3, variance_threshold=300):
    """
    Calculates room brightness considering uneven lighting, with preprocessing steps.

    Parameters:
        image_path (str): Path to the image of the room.
        grid_rows (int): Number of rows to divide the image into.
        grid_cols (int): Number of columns to divide the image into.
        variance_threshold (float): Threshold to determine unevenness.

    Returns:
        dict: Brightness score, method, and regional brightness details.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    # Apply denoising
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

    # Convert to grayscale
    gray_image = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)

    # Enhance contrast using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(gray_image)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)

    # Get image dimensions
    height, width = blurred_image.shape

    # Calculate region size
    region_height = height // grid_rows
    region_width = width // grid_cols

    # Calculate brightness for each region
    regional_brightness = []
    for i in range(grid_rows):
        for j in range(grid_cols):
            start_y, end_y = i * region_height, (i + 1) * region_height
            start_x, end_x = j * region_width, (j + 1) * region_width
            region = blurred_image[start_y:end_y, start_x:end_x]
            avg_brightness = np.mean(region)
            regional_brightness.append(avg_brightness)

    # Assess brightness variation
    brightness_variance = np.var(regional_brightness)

    # Determine overall brightness score
    if brightness_variance > variance_threshold:
        # Uneven lighting: Use median
        brightness_score = np.median(regional_brightness)
        method = "Median (Uneven Lighting Detected)"
    else:
        # Even lighting: Use average
        brightness_score = np.mean(regional_brightness)
        method = "Average (Even Lighting Detected)"

        # Classify based on brightness score (out of 255)
    if brightness_score <= 51:
        brightness_class = "Very Dark"
    elif brightness_score <= 102:
        brightness_class = "Dark"
    elif brightness_score <= 153:
        brightness_class = "Moderately Lit"
    elif brightness_score <= 204:
        brightness_class = "Well Lit"
    else:
        brightness_class = "Very Bright"

    return {
        "brightness_score": brightness_score,
        "brightness_class":brightness_class,
        "method": method,
        "regional_brightness": regional_brightness,
        "brightness_variance": brightness_variance,
    }

image_path = "light.jpg"  
results = calculate_room_brightness(image_path)

print(f"Brightness Score: {results['brightness_score']:.2f}") # score is out of 255
print(f"Brightness Class: {results['brightness_class']}")
print(f"Calculation Method: {results['method']}")
print(f"Brightness Variance: {results['brightness_variance']:.2f}")
print(f"Regional Brightness: {results['regional_brightness']}")
