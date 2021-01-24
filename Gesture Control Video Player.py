import cv2 as cv 
import numpy as np 
import pyautogui

cap = cv.VideoCapture(0)
cap.set(3,250)
cap.set(4,250)

y_low = np.array([22,93,0])
y_upper = np.array([45,255,255])


g_low = np.array([40, 100, 50])
g_upper = np.array([100, 255, 255])

prev_y = 0

while True:
	ret, frame = cap.read()

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	g_mask = cv.inRange(hsv,g_low, g_upper)
	y_mask = cv.inRange(hsv,y_low, y_upper)

	contours_g , hierarchy = cv.findContours(g_mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	contours_y , hierarchy = cv.findContours(y_mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	
	for c in contours_g:
		area = cv.contourArea(c)
		if area > 1000:
			# print(area)
			x, y, w, h = cv.boundingRect(c)
			# cv.drawContours(frame,c,-1, (0,255,0),2)
			cv.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)

			# check moving
			if y < prev_y:
				# print("Moving down")-
				# print(y)
				pyautogui.press('right',10)

			prev_y = y

	for c in contours_y:
		area = cv.contourArea(c)
		if area > 1000:
			# print(area)
			x, y, w, h = cv.boundingRect(c)
			# cv.drawContours(frame,c,-1, (0,255,0),2)
			cv.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)

			# check moving
			if y < prev_y:
				# print("Moving down")-
				# print(y)
				pyautogui.press('left',10)

			prev_y = y


	cv.imshow("frame",frame)
	# cv.imshow("maks",mask)
	if cv.waitKey(10) == ord('q'):
		break


cap.release()
cv.destroyAllWindows()