print (1+1) # 2
print (3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 나머지 1
print(5//3) # 몫 1
print(10//3) # 몫 3

print(10>3) #True
print (4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

#== 앞과 뒤가 같은지 판단해준다.
print(3 == 3) # 3=3 True
print(4 == 2) # False
print(3 + 4 == 7) #True

# != 같지않다
print(1 != 3) #True
print(not(1 !=3)) #False

# and, & 앞뒤 수식이 다 맞는지 판단해준다.
print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

# or, | 앞이나 뒤의 수식중 하나라도 맞는지 판단해준다.
print((3>0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

#연속되어도 가능
print(5 > 4 > 3) #True
print(5 > 4 > 7) #False