python = "Python is Amazing"
print(python.lower()) #소문자로 표시
print(python.upper()) #대문자로 표시
print(python[0].isupper()) #n번째 자리가 대문자인지
print(len(python)) #글자수 세기 (띄어쓰기 포함)
print(python.replace("Python", "Java")) #단어 대체하기

index = python.index("n") # 문장에서 첫번째 n 찾기
print(index)
index = python.index("n", index + 1) # 문장에서 두번째 n 찾기 

print(python.find("Java")) # -1 = Java 가 없다는 뜻
#print(python.index("Java")) #에러 = Java가 없다는 뜻


print(python.count("n")) #문장에 n이 몇개?