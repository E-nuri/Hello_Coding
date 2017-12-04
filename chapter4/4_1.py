# 재귀함수 연습...
# TODO: 재귀함수 예제를 찾아보고 그것을 직접 '노트에 손으로 풀어본 뒤' 코드로 옮겨보기


sum_value = [0]

def sum_list(list):

    def add_value(list):
        if(len(list) == 0):
            return sum_value
        else:
            sum_value[0] = int(sum_value[0]) + int(list[0])
            list.pop(0)
            sum_list(list)

    add_value(list)

sum_list([1,2,3,4])
print(sum_value)