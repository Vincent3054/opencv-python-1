# openCV-pythone 環境建立

### 環境安裝
1. Visual Studio Code
2. 安裝 python 3.6.8
3. 安裝 openCV 相關套件
```
pip install numpy scipy matplotlib scikit-learn jupyter
pip install opencv-python
```
:::success
### 假設import cv2噴錯誤
1. 在VScode按: CTRL + Shift + P
2. 選擇：開啟設定json
3. 最後一段新增："python.linting.pylintArgs": ["--generate-members"]
:::
4. 安裝dlib函式庫
```
pip install dlib
```

:::success
### 假設安裝 dlib 噴錯誤
建議可以直接到 Pypi 官網找更早期的版本來安裝
找到先前的版本 dlib-19.8.1-cp36-cp36m-win_amd64.whl
右鍵複製連結，將連結貼在 pip install 後面
像是這樣：
```
python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf
```
:::
### 測試安裝
```python=
import cv2
cv.__version__
import dlib
dlib.__version__
```
---
## 1.影像辨識(基礎) 
[原文網址](https://medium.com/@yanweiliu/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%B8%80-%E4%BD%BF%E7%94%A8open-cv%E8%BE%A8%E8%AD%98%E5%9C%96%E7%89%87%E5%8F%8A%E5%BD%B1%E7%89%87%E4%B8%AD%E7%9A%84%E4%BA%BA%E8%87%89-527ef48f3a86)
### 安裝模組
```pip install opencv-python```
下載haarcascade_frontalface_default.xml放在目錄　[下載網址](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
### 圖片人臉
```python=
import cv2
# 載入分類器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 讀取圖片
img = cv2.imread('a.jpg')
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
cv2.destroyAllWindows()                    #關閉視窗
```
### 影片人臉
```python=
import cv2
# 載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 從視訊盡頭擷取影片
cap = cv2.VideoCapture(0)
或者....
# 使用現有影片
cap = cv2.VideoCapture('filename.mp4')
while True:
    # Read the frame
    _, img = cap.read()
# 轉成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測臉部
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# 繪製人臉部份的方框
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# 顯示成果
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
cv2.imshow('img', img)                     #秀出圖片
# Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
```
---
## 2.文字辨識
[原文網址](https://medium.com/@yanweiliu/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%BA%8C-%E6%96%87%E5%AD%97ocr%E8%BE%A8%E8%AD%98-6566058e0a43)
### 安裝模組
> 步驟１
```
pip install pillow
pip install pytesseract
```
> 步驟２

安裝Tesseract-OCR [OCR下載網址](https://digi.bib.uni-mannheim.de/tesseract/)
（tesseract-ocr-w64-setup-v4.1.0.20190314 (rc1)）
> 備註1

#記得OCR的安裝路徑：C:\Program Files\Tesseract-OCR
#安裝時要選取中文語言包才能辨識中文

或者至以下連結下載語言包資料 [語言包下載網址](https://github.com/tesseract-ocr/tessdata
)
存至路徑：C:\Program Files\Tesseract-OCR\tessdata

> 備註2

錯誤解決pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path 
找到pytesseract模組裡的pytesseract.py文件，進行修改
找到：tesseract_cmd = 'tesseract'
改成：tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tesseract_cmd所賦予的值其實就是tesseract的安裝路徑

:::info
1.pytesseract可以辨識多種格式，如：tiff,pdf,jpg,png等
2.若tesseract無法辨識出結果，可用Pillow進行對比或亮度處理
:::
### 辨識英文
![](https://i.imgur.com/CBoqRga.png)
```python=
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open(r'C:\Users\Yanwei\Desktop\新增資料夾\a.png')
code = pytesseract.image_to_string(image)
print(code)
```
### 辨識中文
![](https://i.imgur.com/MWGQlGp.png)
```python=
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open(r'C:\Users\Yanwei\Desktop\新增資料夾\a.png')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)
```
