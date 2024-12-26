# Room-Brightness-Analyzer
A Python-based tool to analyze room brightness using OpenCV. This script calculates average pixel intensity in an image to determine lighting conditions (poor, good, or bright). Ideal for basic lighting quality assessments.
<h1>How It Works</h1>
<p>Grayscale Conversion:<br>
Converts the image to a single channel, where pixel intensities range from 0 (black) to 255 (white).</p>
<p>Brightness Calculation:<br>
np.mean(gray_image) computes the mean pixel intensity, which represents the overall brightness of the image.</p>
<p>Thresholds:<br>
Adjust the thresholds (<50, 50–200, >200) based on your lighting conditions and requirements.</p>
