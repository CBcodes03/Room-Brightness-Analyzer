<h3>Approach for Calculating Room Brightness</h3>

<h4>1. Preprocessing the Image</h4>
<p>The preprocessing stage involves improving the quality of the image to make the brightness analysis more accurate:</p>
<ul>
    <li><strong>Denoising:</strong> The image is denoised using <code>cv2.fastNlMeansDenoisingColored()</code> to remove random noise, which could otherwise affect brightness measurements.</li>
    <li><strong>Contrast Enhancement (CLAHE):</strong> <code>cv2.createCLAHE()</code> is applied to enhance the contrast, especially in low-light areas, making it easier to distinguish between different lighting regions.</li>
    <li><strong>Gaussian Blur:</strong> <code>cv2.GaussianBlur()</code> is used to smooth the enhanced image and reduce small fluctuations in pixel intensity, which could introduce noise into the brightness calculation.</li>
</ul>

<h4>2. Dividing the Image into Regions</h4>
<p>Once the image is preprocessed, it is divided into smaller regions (grid-based segmentation). This helps in calculating brightness locally in different sections of the room:</p>
<ul>
    <li>The image is divided into a grid, typically 3x3, resulting in 9 regions. The number of rows and columns can be adjusted based on the desired granularity.</li>
    <li>Each region's average brightness is calculated, providing a localized measure of how bright each part of the image is.</li>
</ul>

<h4>3. Assessing Brightness Variance</h4>
<p>We calculate the variance in brightness across the regions:</p>
<ul>
    <li>The variance helps determine whether the image has uniform or uneven lighting.</li>
    <li>If the variance is above a certain threshold, the lighting is considered uneven, indicating that some regions are significantly brighter or darker than others.</li>
    <li>If the variance is low, the lighting is uniform, and the brightness is consistent across regions.</li>
</ul>

<h4>4. Adaptive Brightness Scoring</h4>
<p>Based on the calculated brightness variance, we choose between using the median or the average for the final brightness score:</p>
<ul>
    <li><strong>If Uneven Lighting (High Variance):</strong> When the variance is high, it indicates uneven lighting in the image (such as a bright light source or dark shadow). In this case, the <strong>median</strong> brightness is used because it is less sensitive to extreme values, such as very bright or dark regions.</li>
    <li><strong>If Even Lighting (Low Variance):</strong> If the variance is low, indicating that the lighting is consistent throughout the image, the <strong>average</strong> brightness is used, as it provides a more accurate reflection of the overall room brightness.</li>
</ul>

<h4>5. Summary of Brightness Calculation</h4>
<ul>
    <li>The <strong>average</strong> approach works well when the lighting is uniform, providing a straightforward and accurate representation of overall brightness.</li>
    <li>The <strong>median</strong> approach is more robust and effective when the lighting is uneven, as it minimizes the impact of extremely bright or dark regions.</li>
    <li>The adaptive method ensures the best approach is chosen depending on the image's lighting conditions.</li>
</ul>

<h4>6. Final Brightness Score</h4>
<p>The final brightness score is determined based on the chosen method (median or average) and is returned as the overall brightness of the room.</p>
