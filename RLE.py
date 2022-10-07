def RLE_encode(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j +1]):
                count = count +1
                j = j +1
            else:
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string
    
def RLE_decode(our_message):
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(our_message)-1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        for j in range(run_count):
            decoded_message = decoded_message + run_word
            j = j + 1
        i = i +2
    return decoded_message
    
f = open('RLEread.txt','r',encoding='UTF-8')
text = RLE_encode(str(*f))
print(text)
my_file = open("RLEencoded.txt","w")
my_file.write(text)
my_file.close()
f = open('RLEencoded.txt', 'r')
text = RLE_decode(str(*f))
my_file = open("RLEdecoded.txt", "w")
my_file.write(text)
my_file.close()