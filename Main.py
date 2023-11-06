# pip install opencv-python deepface
import threading
import cv2
from deepface import DeepFace

# Tạo đối tượng video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

counter = 0
# Cờ để chỉ ra xem có kết quả phù hợp với khuôn mặt hay không
face_match = False
# Tải ảnh tham chiếu
img = cv2.imread("loc.jpg")

# Hàm kiểm tra kết quả phù hợp với khuôn mặt
def check_face(frame):
    global face_match
    try:
        # Nếu có khuôn mặt được xác minh, đặt face_match thành Trueq
        if DeepFace.verify(frame,img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        # print("Lỗi trong quá trình nhận dạng khuôn mặt:", str(e))
        face_match = False


# tao vong' lap
while True:
    ret,frame = cap.read()
    if ret:
        if counter % 38 == 8:
            # xu ly ngoai le
            try:
                threading.Thread(target = check_face,args = (frame.copy(),)).start()
            except ValueError:
                pass

        counter += 1
    
        #  neu nhan dien dung' return TRUE vao' duoi khung camera >< return FALSE
        #font = 2
        # mau RGB=(0,255,0)=> green = 255  
        # do day = 3
        if face_match:
            cv2.putText(frame,"Match",(20,450), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,"No Match",(20,450), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)

     
        # hien khung 
        cv2.imshow("video",frame)


    # nhan' 1 thi' se nhan dang
    key = cv2.waitKey(1)
    # nhan' q thi break
    if key == ord('q'):
        break
cv2.destroyAllWindows()


# vì video ở tốc độ 30 khung hình/giây, nên chúng tôi 
# có thể thấy kết quả trùng khớp/không khớp sau mỗi 30 khung hình, tức là cứ sau 1 giây