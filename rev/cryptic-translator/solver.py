def decode(data):
    d = "ahduabpeedus"
    replacement = "010101010101"

    arr = data
    convertBinary = ""
    for i in range(0,6):
        for ele in arr:
            if ele == d[2*i]:
                convertBinary+=replacement[2*i]
            elif ele == d[2*i+1]:
                convertBinary+=replacement[2*i+1]

        print("i = "+str(i))

        arr = convertBinary
        convertBinary = ""

        for j in range(0,len(arr),8):
            substring = arr[j:j+8]
            decimal_value = int(substring,2)
            leftNibble = decimal_value>>4
            rightNibble = decimal_value & 0x0f
            character = chr((rightNibble<<4)| leftNibble )
            convertBinary+=character


        arr = convertBinary
        convertBinary=""

    return arr

with open("encoded",'r') as file:
    file_data = file.read()
    print(decode(file_data))