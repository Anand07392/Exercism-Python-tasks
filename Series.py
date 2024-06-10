def slices(series, length):
    if len(series)>0:
        if length==0:
            raise ValueError("slice length cannot be zero")
        elif length<0:
            raise ValueError("slice length cannot be negative")
        elif length>len(series):
            raise ValueError("slice length cannot be greater than series length")
        substrings=[]
        for i in range(len(series)-length+1):
            substring=series[i:i+length]
            substrings.append(substring)
        return substrings               
    else:
        raise ValueError("series cannot be empty")
