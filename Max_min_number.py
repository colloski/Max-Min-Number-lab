def find_max_min(element):
    min_max = []
    max_num = max(element)
    min_num = min(element)
    
    if isinstance(element, list):
        if max_num == min_num:
            min_max.append(max_num)
            return min_max
        else:
            min_max.append(min_num)
            min_max.append(max_num)
            return min_max
    else:
        return None
