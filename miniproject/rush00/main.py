from checkmate import checkmate,print_board

def main():
    """
    ฟังก์ชันหลัก - ใช้ตัวอย่างง่ายๆ สำหรับทดสอบ
    """
    # ตัวอย่างจากโจทย์
    board = """\
.B..
K...
.....
....\
"""
    print_board(board)
    checkmate(board)

if __name__ == "__main__":
    main()