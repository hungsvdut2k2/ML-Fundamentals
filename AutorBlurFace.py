# import the opencv library
import cv2
import numpy as np

# define a video capture object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vid = cv2.VideoCapture(0)


while True:

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    kernel = np.ones((9, 9), np.float32) / 81.0
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        roi = frame[y : y + h, x : x + w]
        roi = cv2.filter2D(roi, cv2.CV_8U, kernel)
        roi = cv2.filter2D(roi, cv2.CV_8U, kernel)
        roi = cv2.filter2D(roi, cv2.CV_8U, kernel)
        frame[y : y + h, x : x + w] = roi

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
