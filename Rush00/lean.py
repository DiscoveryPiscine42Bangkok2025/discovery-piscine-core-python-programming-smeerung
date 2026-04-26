import sys
user_input = input("กรุณาใส่ข้อมูล: ")
print(user_input)
data = sys.stdin.read() # อ่านข้อมูลทั้งหมดจนกว่าจะจบไฟล์
print(data)