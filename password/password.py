def process_data(data):

    total_sum = 0.0
    for element in data:
        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            try:
                num = float(element)
                total_sum += num
            except ValueError:
                print(f"Warning: Could not convert '{element}' to float.")
            else:
                print(f"Warning: Unsupported data type: {type(element)}")
       
    return total_sum

