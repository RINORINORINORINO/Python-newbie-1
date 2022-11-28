# print ("Hello")
# # 우물정자가 바로 주석이다
# b = 1
# print (b)
# print (type(b))
# # 파이썬에서 변수는 항상 저장하고 입력해줘야 출력이 가능하다
# # +, -, * (** 는 제곱), / (// 는 몫만 출력, %는 나머지만 출력) 사칙연산
# # type() = 해당 문자열이 어떤 종류인지 출력해주는 함수 - 정수는 int, 실수는 float, 문자는 str

# a = "hello python"
# print (a) 
# print (type(a))

# # '',"","""""" = 문자형으로 만들 때 씀

# # syntax error 프로그래밍하면서 문장에 오류가 있을 때 나타내는 표시
# # \n = 파이썬은 한줄씩 처리하기 때문에 줄을 변환하고 싶을 때 쓰는 것 
# # \t = 문자열 사이 탭 간격을 줄 때 사용
# # \\ = \ 문자를 그대로 표현할 때 사용
# # \' / \" = 작은 따옴표(또는 큰 따옴표)를 그대로 표현할 때 사용
# # """ """ = 띄어쓰기를 해도 그대로 출력할 수 있음

# c = 'babo'
# print(c*100)

# # 인덱싱(indexing) = [], [ : : ]
# # 문자열 안에서 [] 안에 들어있는 번호의 문자를 출력\
# # [시작:끝:간격]

# d = 'Rino is coder'
# print(d[0])
# print(d[-1])
# print(d[ :3])
# print(d[3:])
# print(d[ : :2])
# print(d[ : :-2])

# # 문자열 포메팅 % = %d는 정수, %f는 실수, %s는 문자열
# # %숫자s,d,f 등 = 앞에 숫자만큼 띄어쓰기 하고 출력
# # %0.숫자f = 소수점 몇번째까지 나타낼지

# rino = 10   # 첫 번째, 변수 설정
# rinorino = "three" # 첫 번째, 변수 설정
# e = "RINO ate %d apples. So I was sick for %s days" %(rino, rinorino) #두 번째, 함수를 설정
# print(e)

# # 기초적 함수 = 변수.count, 변수.find(대용함수로 변수.index)
# f = "Rino"
# print(f.count('r'))
# print(f.count('R'))
# print(f.find('R'))

# # 기초적 함수 = 변수.join - 쪼개서 삽입, 변수.upper/lower - 대문자, 소문자로 바꾸기, 변수.strip - 공백 지우기

# g = 'o'.join("abcd")
# print(g)

# aa = "hoon"
# bb = "RINO"
# print(aa.upper())
# print(bb.lower())

# # 기초적 함수 = 변수.replace - 특정 변수를 변환, 변수.split - 정한 기준으로 값을 자름, 디폴트값은 띄어쓰기

# cc = "hoon is really babo"
# print(cc.split())
# print(cc.split("n"))

# # 리스트 = 여러 개의 변수를 하나의 상자에 담는 역할 - []
# # 리스트 안에 리스트 안에 리스트 안에 리스트 안에.... 넣을 수 있음 

# dd = [1,2,3,4,5,6]
# print(dd[1])
# print(dd[ :5])

# # 리스트 교체하기
# dd[ :3] = [7, 8, 9]
# print(dd)

# # 리스트 삭제하기
# dd[0:2] =[]
# print(dd)
# del dd[1]
# print(dd)

# # 리스트 맨뒤에 추가하기 - 변수.append()
# # 리스트 정렬하기 - 변수.sort()
# # 리스트 뒤집기 - 변수.reverse()
# # 리스트 위치 반환 - 변수.index()
# # 리스트 특정 위치에 추가하기 - 변수.insert(번호,추가할 값)
# # 리스트 요소 제거하기 - 변수.remove(값) - 여러 같은 값이 있는 경우 해당하는 가장 맨앞 값이 제거됨
# # 리스트 맨뒤 요소 빼기 - 변수.pop()
# # 리스트 카운팅 - 변수.count(값)
# # 리스트 확장하기(추가하기) - 변수.extend([리스트값])

# dic = {'name' : 'rino', 'age' : 15}
# print(dic['name'])

# a = {1: 'a'}
# a['name'] = "익명"
# del a[1]
# print(a)

# from copy import copy
# a = [1,2,3]
# b = copy(a)
# print(b)
# print(id(a))
# print(id(b))

# score = 70
# if score > 90:
#     message = "success"
# else:
#     message = "failure"
# print(message)

# message = "success" if score > 90 else "failure"
# print(message)

# buger = 10
# money = 10000
# while money:
#     print("햄버거 받아가세요!")
#     buger = buger - 1
#     print("햄버거가 %d개 남았습니다" % buger)
#     if not buger:
#         print("햄버거가 오링남")
#         break

# s = 0
# while s < 30:
#     print("s를 더 하고 싶다!!!")
#     s = s + 1
#     if s % 5 == 0:
#         print("나 이번은 못해!")
#         continue
#     print("더 할 수 있어")

number = 0
for i in [90, 65, 77, 53, 20]:
    number = number + 1
    if i > 60: continue
    print("%d번 학생 합격입니다!" % number)

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = "")
    print('')

result = [x * y for x in range(2,10) for y in range(1,10)]
print(result)

result = []
for x in range(2,10):
    for y in range(1,10):
        result.append(x*y)
print(result)

money = 1
card = 1
if money:
    print("Taxi!")
elif card:
    print("Bus!")
else:
    print("just walk...")

def say_myself(name, age, man=True):
    print("나는 %s입니다!" % name)
    print("나이는 %d살 입니다!" % age)
    if man: 
        print("나는 남자입니다!")
    else:
        print("나는 여자입니다!")
say_myself('rino', 31)
say_myself('hoon', 34, False)

def add(a,b):
    return a+b

add = lambda a,b: a+b

f = open("new file.txt", "w", encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다!\n" % i
    f.write(data)
f.close()


