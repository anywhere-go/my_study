weather ="비" #weather 변수에 값 할당
print("비가 오나요?", weather =="비")
if weather == "비":
    print("우산을 가져간다.")
elif weather =="맑음":
    print("날씨가 좋다.")
else: #조건문이 False면 실행
    print("우산을 가져가지 않는다.")