import cv2

# Read the image
image = cv2.imread('img.jpg')

# Define the text properties
text = "Hello, OpenCV!"
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 1.0
color = (255, 255, 255)  # BGR color format
thickness = 2

# Get the size of the text
(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

# Calculate the position to place the text
x = int((image.shape[1] - text_width) / 2)
y = int((image.shape[0] + text_height) / 2)

# Place the text on the image
cv2.putText(image, text, (x, y), font, font_scale, color, thickness)

# Display the image
cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
