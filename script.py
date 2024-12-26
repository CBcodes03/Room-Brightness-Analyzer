def check_brightness(image_path):
    import cv2
    import numpy as np
    # Load the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the average brightness
    average_brightness = np.mean(gray_image)
    print(f"Average Brightness: {average_brightness:.2f}")
    if average_brightness < 50:
        print("Lighting is Poor.")
    elif 50 <= average_brightness <= 200:
        print("Lighting is Good.")
    else:
        print("Lighting is Bright.")

if __name__ == '__main__':
    check_brightness(image_path='dark.jpeg')#update path here to check brightness level
