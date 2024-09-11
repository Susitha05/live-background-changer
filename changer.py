!pip install cvzone
!pip install numpy
!pip install SeleSegmatation 
!pip install cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

listimag= os.listdir('img')
print(listimag)
ilist = []
def cam() :
    for imgPath in listimag:
        img1 = cv2.imread(f'img/{imgPath}')
        ilist.append(img1)
        print(len(ilist))

    imgindex = 1

    segmentor = SelfiSegmentation()
    while True:
        success, img = cap.read()

        input_image = segmentor.removeBG(img, (ilist[imgindex]), cutThreshold=0.7)
        imgstacked = cvzone.stackImages([img, input_image], 2, 1)

        cv2.imshow('cam', imgstacked)
        key = cv2.waitKey(1)
        if key == ord('f'):
            if imgindex < 1:
                imgindex -= 1

        elif key == ord('d'):
            if imgindex < len(ilist) - 1:
                imgindex += 1

        elif key == ord('w'):
            break

        else:
            print("happy happy happy")