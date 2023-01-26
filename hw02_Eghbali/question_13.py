n = int(input())
test_text = input()
result_text = input()

error_count=0

if len(test_text) != n:
    pass
else:
    for i in range(n):
        if test_text[i] != result_text[i]:
            error_count+=1
    print(error_count)
