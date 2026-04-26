import sys
from checkmate import checkmate

def main():
    # รับ Input ทั้งหมดจาก stdin
    input_data = sys.stdin.read()
    
    if not input_data.strip():
        return

    # แยกบรรทัดแรกที่เป็นตัวเลขขนาดกระดานออก (ถ้ามี)
    lines = input_data.strip().split('\n')
    
    # ตรวจสอบว่าบรรทัดแรกเป็นตัวเลขหรือไม่
    if lines[0].isdigit():
        size = int(lines[0])
        board_lines = lines[1:]
    else:
        board_lines = lines
    
    # ตรวจสอบว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่ (Undefined behavior check)
    if not board_lines:
        return
        
    board_str = '\n'.join(board_lines)
    checkmate(board_str)

if __name__ == "__main__":
    main()