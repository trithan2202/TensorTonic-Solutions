def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    N = len(actual_tokens)
    total_log_prob = 0.0
    
    # Tính tổng log(p) cho tất cả các vị trí
    for i in range(N):
        # Lấy danh sách xác suất tại vị trí i
        dist = prob_distributions[i]
        # Lấy chỉ số của token thực tế tại vị trí i
        token_idx = actual_tokens[i]
        # Lấy xác suất p tương ứng
        p = dist[token_idx]
        total_log_prob += math.log(p)
    
    cross_entropy = - (1 / N) * total_log_prob
    result = math.exp(cross_entropy)
    
    return result