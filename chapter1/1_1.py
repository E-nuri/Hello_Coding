import random

lowNum = 1
highNum = 25
targetNum = 10

# 특정 범위 값 내의 랜덤 숫자 리스트 파일 생성
def generate_random_num_list(low, high):
    numList = []
    calibratedHighNum = high+1;

    # low부터 high+1 범위 내에서 숫자 리스트 생성
    for count in range(low, calibratedHighNum) :
        numList.append(count)
    random.shuffle(numList)

    mixedNumFile = open("mixedNumFile.txt", "w", encoding="utf-8")

    for number in numList :
        mixedNumFile.write(str(number)+" ")
    mixedNumFile.write('\n')

    mixedNumFile.close()
    return numList


# 리스트를 오름차순으로 정렬
def sorting_num_list(numList):
    sortedNumFile = open("sortedNumFile.txt", "w", encoding="utf-8")

    numList = [int(number) for number in numList]
    numList.sort()

    for number in numList:
        sortedNumFile.write((str(number))+" ")
    sortedNumFile.write('\n')

    sortedNumFile.close()

    return numList


# 이진 탐색으로 목표 값을 탐색
def binary_search(targetNum, lowNum, highNum, numList):

    if (targetNum < lowNum) or (targetNum > highNum):
        return "찾는 값이 없습니다."
    else:
        while lowNum <= highNum:
            midNum = int((lowNum + highNum) / 2)
            isTargetNumber = numList[midNum]

            if isTargetNumber == targetNum:
                return midNum
            elif isTargetNumber > targetNum:
                highNum = midNum-1
            else:
                lowNum = midNum+1


generatedNumList = generate_random_num_list(lowNum, highNum)
print(lowNum, "부터", highNum, "까지의 값 리스트 생성\n", generatedNumList)
sortedNumList = sorting_num_list(generatedNumList)
print(lowNum, "부터", highNum, "까지의 값 오름차순 정렬\n", sortedNumList)
searchingResult = binary_search(10, lowNum, highNum, sortedNumList)
print("찾고 있는", targetNum, "의 위치는", searchingResult,"번째에 있습니다")
