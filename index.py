import requests
import re
import os

p = re.compile('\S')
q = re.compile('https?://')
ans = "y"


while ( True ):
    #    google. com   , https://www.naver.com ,   http://www.daum . net , nnnave.com 
    # 텍스트 입력받기
    input_text = input("Please write a URL or URLs you want to check. (separated by comma [,]) \n")

    # 정규표현식으로 행렬로 
    result = p.findall(input_text)
    # 행렬을 다시 문자열로
    result = "".join(s for s in result)

    #문자열을 컴마를 기준으로 쪼개서 행렬로
    result = result.split(',')

    #https:// 안붙은것은 붙여주기
    for i in range(len(result)):
        if q.match(result[i]) == None :
            result[i] = "https://" + result[i]


    #requests로 유효성 체크하기
    for i in result:
        try :
            if requests.get(i).status_code ==200:
                print(i ,'is UP! ^_^d')
        except :
            print( i , "is down!")
    
    ans = input('Do you want to start over? [y or not]')
    if (ans != "y"):
        break
    else:
        os.system('clear')
