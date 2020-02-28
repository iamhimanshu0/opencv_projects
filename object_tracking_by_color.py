import cv2 as cv 
import numpy as np 
import imutils

def main():
	cap = cv.VideoCapture(0)


	if cap.isOpened():
		ret , frame = cap.read()

	else:
		ret = False

	while ret:
		ret, frame = cap.read()
		frame = imutils.resize(frame, width=450)
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
		
		# blur range
		b_low = np.array([100,50,50])
		b_high = np.array([140,255,255])

		# green range
		sensitivity = 15;
		g_low = np.array([40, 100, 50])
		g_high = np.array([100, 255, 255])

		# red range
		r_low = np.array([170,25,20])
		r_high = np.array([179,255,255])

		# make mask
		img_mask_b = cv.inRange(hsv,b_low,b_high)
		img_mask_g = cv.inRange(hsv,g_low,g_high)
		img_mask_r = cv.inRange(hsv,r_low,r_high)
		# bitwise operation
		output_b = cv.bitwise_and(frame,frame,mask=img_mask_b)
		output_g = cv.bitwise_and(frame,frame,mask=img_mask_g)
		output_r = cv.bitwise_and(frame,frame,mask=img_mask_r)
		cv.imshow('blue',output_b)
		cv.imshow('green',output_g)
		cv.imshow('red',output_r)
		cv.imshow('original',frame)
		if cv.waitKey(1) == ord('q'):
			break

	cv.destroyAllWindows()
	cap.release()

if __name__ == '__main__':
	main()

