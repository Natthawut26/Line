import cv2
import numpy as np

# สร้างฟังก์ชันสำหรับวาดเส้นตรง
def draw_line(image, start_point, end_point, color=(0, 0, 255), thickness=2):
    return cv2.line(image, start_point, end_point, color, thickness)

# โหลดรูปภาพ
image = cv2.imread('image.jpg')

# กำหนดตำแหน่งเริ่มต้นและสิ้นสุดของเส้นตรง (ตัวอย่างเลือกตำแหน่งแบบสุ่ม)
start_point = (100, 100)
end_point = (400, 400)

# วาดเส้นตรงบนภาพ
draw_line(image, start_point, end_point)

# แสดงภาพที่มีเส้นตรง
cv2.imshow("Line on Image", image)

# สร้าง kernel สำหรับ Convolution (ตัวอย่างใช้ kernel 3x3)
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]], dtype=np.float32)

# ทำการ Convolution กับภาพ
convolution_result = cv2.filter2D(image, -1, kernel)


# แสดงผลลัพธ์ของ Convolution
cv2.imshow("Convolution Result", convolution_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
