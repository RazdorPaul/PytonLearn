def all_var(text):
    len_slice = 1
    while len_slice <= len(text):
        start = 0
        stop = len_slice
        while stop <= len(text):
            yield text[start:stop]
            start +=1
            stop +=1
        len_slice +=1

a = all_var("abcde")
for i in a:
    print(i)