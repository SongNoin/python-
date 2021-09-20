# weather = input("오늘날씨는 어때요? ") 
# if weather == "비" or weather == "눈": # if 조건이 맞으면 출력 # or
#     print("우산을 챙기세요.")
# elif weather == "미세먼지": # if 조건에 맞지않으나 elif 조건에 맞으면 출력
#     print("마스크를 챙기세요.")
# else: # 모든 조건이 맞지않으면 출력
#     print("준비물 필요 없어요.")


temp = int(input("기온은 어때요? ")) #int 정수 #input은 입력
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")