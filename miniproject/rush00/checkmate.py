def checkmate(board):
    try:
        # แปลงสตริงบอร์ดให้เป็น list ของ list
        lines = board.strip().split('\n')
        
        # ตรวจสอบว่าบอร์ดเป็นสี่เหลี่ยมจัตุรัสหรือไม่
        if not lines:
            print("Error: Empty board!")
            return
            
        size = len(lines[0])
        for line in lines:
            if len(line) != size:
                print("Error: Invalid board shape!")
                return
        
        # หา King ในบอร์ด
        king_pos = None
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == 'K':
                    if king_pos is not None:  # มี King มากกว่า 1 ตัว
                        print("Error: Multiple Kings found!")
                        return
                    king_pos = (i, j)
        
        # ไม่มี King
        if king_pos is None:
            print("Error: No King found!")
            return
        
        king_row, king_col = king_pos
        
        # โดนรุกหรือไม่
        if is_attacked_by_pawn(lines, king_row, king_col) or \
           is_attacked_by_rook(lines, king_row, king_col) or \
           is_attacked_by_bishop(lines, king_row, king_col) or \
           is_attacked_by_queen(lines, king_row, king_col):
            print("Checkmate!")
        else:
            print("King save!")
            
    except Exception:
        print("Error: Something went wrong!")


def is_attacked_by_pawn(board, king_row, king_col):
    """Pawn โจมตีได้แนวทแยง """
    # ตรวจสอบทแยงซ้าย
    if king_row > 0 and king_col > 0:
        if board[king_row - 1][king_col - 1] == 'P': 
            return True
    
    # ตรวจสอบทแยงขวา
    if king_row > 0 and king_col < len(board[0]) - 1:
        if board[king_row - 1][king_col + 1] == 'P':
            return True
    
    return False


def is_attacked_by_rook(board, king_row, king_col):
    """Rook โจมตีเป็นรูปบวก"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # บน, ล่าง, ซ้าย, ขวา
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        
        # เดินไปในทิศทางนั้นจนกว่าจะเจอสิ่งกีดขวางหรือขอบบอร์ด
        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            piece = board[row][col]
            
            if piece != '.' and piece != ' ':  # เจอหมากหรือสิ่งกีดขวาง
                if piece == 'R':
                    return True
                break  #หยุดเดิน
            
            row += dr
            col += dc
    
    return False


def is_attacked_by_bishop(board, king_row, king_col):
    """Bishop โจมตีได้แนวทแยง"""
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # ทแยง 4 ทิศ
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        
        # เดินไปในทิศทางนั้นจนกว่าจะเจอสิ่งกีดขวางหรือขอบบอร์ด
        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            piece = board[row][col]
            
            if piece != '.' and piece != ' ':  # เจอหมากหรือสิ่งกีดขวาง
                if piece == 'B':
                    return True
                break  
            
            row += dr
            col += dc
    
    return False


def is_attacked_by_queen(board, king_row, king_col):
    """Queen (รวม Rook + Bishop)"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),    # แนวตั้งและแนวนอน
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]   # แนวทแยง
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        
        # เดินไปในทิศทางนั้นจนกว่าจะเจอสิ่งกีดขวางหรือขอบบอร์ด
        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            piece = board[row][col]
            
            if piece != '.' and piece != ' ':  # เจอหมากหรือสิ่งกีดขวาง
                if piece == 'Q':
                    return True
                break  #หยุดเดิน
            
            row += dr
            col += dc
    
    return False
def print_board(board: str) :
    rows = board.strip().split("\n")
    print("Chess Board :")
    for row in rows :
        print(" ".join(row))
    print()