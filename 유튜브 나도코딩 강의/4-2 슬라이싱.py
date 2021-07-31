jumin = "990120-1234567"

print("성별 : " + jumin[7]) #jumin[7] = jumin에서 7번째 있는 글자 (0번째부터 시작)
print("연 : " + jumin[0:2]) #jumin[0:2] = jumin에서 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4]) #jumin[2:4] = jumin에서 2 부터 4 직전까지 (2, 3)
print("일 : " + jumin[4:6]) #jumin[4:6] = jumin에서 4 부터 6 직전까지 (4, 5)
print("생년월일 : " + jumin[:6]) #jumin[:6] = jumin에서 처음부터 6 직전까지 (0 ~ 5)
print("뒤 7자리 : " + jumin[7:]) #jumin[7:] = jumin에서 7 부터 마지막까지 (7 ~)
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨뒤에서 7번째부터 맨 끝까지