import sys
global huff

def huffman_encoding(data):
    global huff
    huff = {}
    for char in data:
        huff[char] = huff.get(char, 0) + 1
    tree = {}
    temp = '1'
    for num in sorted(huff.items(), key = lambda x: x[1]):
        tree[num[0]] = temp
        temp = '0' + temp

    encode = ''
    for d in data:
        encode += tree[d]
    return encode, tree

def huffman_decoding(data,tree):
    huff = {}
    for char in tree:
        huff[tree[char]] = char
    #print(huff)
    temp = ''
    decode = ''
    for d in data:
        if d == '1':
            decode += huff[temp + d]
            temp = ''
        else:
            temp += d
    return decode

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # print(tree)
    # print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
