def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Khởi tạo từ điển để lưu trữ kết quả
    counts = {}
    
    # Duyệt qua từng danh sách con (từng câu) trong sentences
    for sentence in sentences:
        # Duyệt qua từng từ (token) trong câu đó
        for word in sentence:
            # Nếu từ đã tồn tại trong dict, tăng giá trị lên 1
            if word in counts:
                counts[word] += 1
            # Nếu từ chưa có, khởi tạo giá trị là 1
            else:
                counts[word] = 1
                
    return counts