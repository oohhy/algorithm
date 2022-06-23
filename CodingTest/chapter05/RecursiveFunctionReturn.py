def recursive_funcion(i):
    if i == 100:
        return

    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    # i==100까지 이 줄까지 수행하다가 return조건 충족하면 
    recursive_funcion(i + 1)
    # 여기부터 다시 역순으로 올라가면서 출력
    print(i, "번째 재귀 함수를 종료합니다.")

recursive_funcion(1)