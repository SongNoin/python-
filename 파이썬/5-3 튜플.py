menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 에러, 튜플은 add 기능을 제공하지 않음


# 일반적으로 하나하나 지정해줘야 하지만
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 튜플은 이렇게 서로 다른 값을 지정할 수 있다.
(name, age, hobby) = "김종국", 20, "코딩"
print(name, age, hobby)