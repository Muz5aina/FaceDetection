# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import cv2
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    print(ret)
    g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f = cascade_face.detectMultiScale(g, 1.3, 4)

    for (x,y,w,h) in f:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
