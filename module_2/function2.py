def middle(data):
    print("Executing middle()")
    for i in range(0,len(data)):
        #print(data[i])
        #print(f"\tInteger i = {i}")
        #print(f"\t\tData = {data[i]}")
        data[i] = data[i] + 1
    return data