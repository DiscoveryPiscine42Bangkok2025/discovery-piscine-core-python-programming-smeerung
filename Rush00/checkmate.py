def checkmate(board):
    # เปลี่ยน board จาก string ให้เป็น list 2 มิติเพื่อให้อ่านง่าย (ถ้าจำเป็น)
    board = board.strip().split('\n')
    size = len(board)
    
    # 1. หาตำแหน่งของ King (K)
    k_x, k_y = -1, -1
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                k_x, k_y = r, c
                break
    
    if k_x == -1:
        return # กรณีไม่พบ King

    # 2. ฟังก์ชันตรวจสอบทิศทาง (Raycasting)
    # ทิศทาง: (row_delta, col_delta, pieces_that_can_kill)
    directions = [
        # แนวตั้ง-แนวนอน (Rook, Queen)
        (-1, 0, "RQ"), (1, 0, "RQ"), (0, -1, "RQ"), (0, 1, "RQ"),
        # แนวทะแยง (Bishop, Queen)
        (-1, -1, "BQ"), (-1, 1, "BQ"), (1, -1, "BQ"), (1, 1, "BQ")
    ]

    for dr, dc, enemies in directions:
        r, c = k_x + dr, k_y + dc
        step = 1
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            
            if piece != '.':
                # ตรวจสอบ Pawn (กินทะแยงเฉพาะด้านหน้า 1 ช่อง)
                # หมายเหตุ: ในโจทย์นี้ Pawn ศัตรูมักเดินลง (-1 ในแกน Y ของมัน) 
                # ดังนั้นถ้า King อยู่ที่ (r, c) Pawn ที่กินได้จะอยู่ที่ (r-1, c-1) หรือ (r-1, c+1)
                if piece == 'P':
                    if step == 1 and dr == -1 and (dc == -1 or dc == 1):
                        print("Success")
                        return
                
                # ตรวจสอบ Rook, Bishop, Queen
                elif piece in enemies:
                    print("Success")
                    return
                
                # ถ้าเจอหมากตัวอื่นขวางทาง (รวมถึง K เอง) ให้หยุดมองทิศนี้
                break
            
            r += dr
            c += dc
            step += 1

    print("Fail")