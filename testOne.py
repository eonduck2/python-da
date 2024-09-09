a = "이종수"
b = "바보"


def string_merge():
    return a + b


print(a, b)


# * 맨날 이름쓰기 힘듦
def example():
    return "예제"


another_example = lambda value, value2: value + value2
print(another_example("이", "asd"))

result = (lambda x, y: x + y)(5, 10)

array = ["ㅎㅇ", "ㅂㅇ"]
obj = {"호": "날두", "메": "시", "크흠": "야 !!"}

print(array[0])
print(obj["메"])

another_obj = ("음바페", "페란", "올모", "올모")

print(another_obj)


def testDef(someDef):
    print(someDef)
    print(someDef(1, 2))


testDef((lambda x, y: x + y))
print(another_obj[0])
# print("테스트 디프", testDef((lambda x, y: x + y)(5, 10)))
