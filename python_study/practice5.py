# 거꾸로 배열해도 같은 단어 또는 문장이 되는 회문(palindrome)인지 판별하는 함수를 정의하세요
# 함수에 문자열을 입력받고 회문이면 True 아니면 False를 반환하도록 정의하세요
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False

# def is_plindrome(input_string):

    # 기러기
    # 소주 만병만 주소
    # length = len(input_string)
    # for i in range(length//2):
    #     length - 1
    #     if input_string[i] != input_string[length - 1 - i]:
    #         return False
    # return True
# 위에 것은 띄어쓰기 때문에 오류가능

# 다시 합창합시다

# def is_plindrome(input_string):

#     # 기러기
#     # 소주 만병만 주소
#     input_string = input_string.replace(" ", "")
#     length = len(input_string)
#     for i in range(length//2):
#         length - 1
#         if input_string[i] != input_string[length - 1 - i]:
#             return False
#     return True

#
# def is_plindrome(input_string):

    # 기러기
    # 소주 만병만 주소
    # input_string = input_string.replace(" ", "") #문자열 중간에 있는 공백 제거
    # length = len(input_string)
    # for i in range(length//2):
    #     length - 1
    #     if input_string[i] != input_string[length - 1 - i]: 
    #         return False
    # return True
#     return input_string == input_string[::-1]
# result = is_plindrome("소주 만병만 주소")
# print(result)


# reversed("안녕하세요")
# li1 = [1,2,3,4,5]
# li1.reverse()
# li2 = reversed(li1)
# print(li1)



# string1 ="안녕하세요"
# string2 = reversed(string1) #reversed는 새롭게 입력되는 값
# for i in string2:
#     print(i)
# print(string2)  #한 글자씩 반대로 출력
# string3 = "".join(string2)
# print(string3)


