def S_P():
    SV = input('서비스 종류를 입력하세요, a/b/c: ')
    VA = input('부가세를 포함합니까? y/n: ')
    if VA == 'y': #if 문을 이용하여 부가세 포함 여부를 판단
        if SV == 'a': #서비스의 종류를 파악하는 if문
            RE = 23 * 1.1
        if SV == 'b':
            RE = 40 * 1.1
        if SV == 'c':
            RE = 67 * 1.1
    if VA == 'n':
        if SV == 'a':
            RE = 23
        if SV == 'b':
            RE = 40
        if SV == 'c':
            RE = 67
    print(round(RE,1),'만 원입니다') #print()를 이용하여 반올림한 RE값을 출력
    
S_P() #함수 사용


'''
서비스의 종류와 부가세 포함 input()에서 if문에 정의되지 않은 다른 문자를
입력하게 되면 에러가 발생하는 경우가 있어 else 문을 추가하여 예외처리를
할 수 있게 하면 더 좋은 프로그램이 되지 않을까 싶습니다.

else:
    print("정확하게 입력해 주시기 바랍니다") a/b/c 또는 y/n 이외 다른 것을 입력한 경우
'''
