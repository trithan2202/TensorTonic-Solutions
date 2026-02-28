def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stop_set = set(stopwords)

    result = [t for t in tokens if t not in stop_set]
    
    return result