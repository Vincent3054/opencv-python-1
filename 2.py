import cv2
# 載入分類器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 讀取圖片
img = cv2.imread('a.jpeg')
# 轉成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測臉部
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.08,
    minNeighbors=5,
    minSize=(32, 32))
# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#(0, 255, 0)欄位可以變更方框顏色(Blue,Green,Red)
# 顯示成果
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
cv2.imshow('img', img)                     #秀出圖片
cv2.imwrite( "result.jpg", img )           #保存圖片
cv2.waitKey(0)                             #等待按下任一按鍵
cv2.destroyAllWindows()  