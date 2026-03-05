def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    result = []
    # Tính bước nhảy (khoảng cách giữa các điểm bắt đầu)
    step = chunk_size - overlap
    
    # Duyệt qua danh sách với bước nhảy 'step'
    for i in range(0, len(tokens), step):
        # Lấy một đoạn từ vị trí i đến i + chunk_size
        chunk = tokens[i : i + chunk_size]
        result.append(chunk)
        
        # Nếu đoạn vừa lấy đã chạm hoặc vượt quá cuối danh sách, dừng lại
        if i + chunk_size >= len(tokens):
            break
            
    return result