# USAGE
# python detect_color.py --image pokemon_games.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
	([232, 232, 225], [247, 247, 247]), #white
	([0, 0, 0], [25, 25, 25]), #black
	([119, 0, 222], [247, 234, 255]), #pink
	([27, 46, 45], [173, 222, 158]), #green
	([0, 5, 100], [169, 56, 247]), #red
	([86, 51, 107], [237, 116, 195]), #purple
	([0, 121, 87], [160, 206, 170]), #gray, complicated color
	([0, 146, 190], [233, 247, 255]), #yellow
	([36, 0, 50], [255, 80, 80]) #blue
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
