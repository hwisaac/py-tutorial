import requests
from bs4 import BeautifulSoup
import re
import csv
import save

# re_exp = re.compile('[^/\\:?*"><|.%]')
nre_exp_str = '[/\\:?*"><|.%]'
URL = 'http://www.alba.co.kr/'

brand_test_url='http://footlockerkr.alba.co.kr/'

# brand -> {company, title, link} 정보 dict 를 반환한다.
def extract_company_info(brand)->dir:
    company = brand.find("span", {'class': 'company'}).string

    company = re.sub(nre_exp_str,'_', company)

    title = brand.find('span', {'class': 'title'}).string
    link = brand.find('a')['href']

    return {'company':company, 'title': title, 'link' : link}

# ()-> brands 메인페이징에서 brands 뽑아내기
def extract_alba_brands() ->list: 
    data = requests.get(URL)
    # 데이터 추출해서 html 알려주기
    soup = BeautifulSoup( data.text , 'html.parser')
    brands = []

    # ul 태그의 클래스명 goodsBox 찾아 행렬로 반환하고 1인덱스 선택하여 테이블 선택 
    goodsBox = soup.find_all("ul" , {'class' : 'goodsBox'})[1]
    # 테이블 내에서 impact 클래스에 해당하는 회사들을 각각 선택
    company_infos = goodsBox.find_all('li', {'class' : 'impact'})

    # goodsBox-info 에서 company정보와 title정보 추출하고 result 리스트에 저장
    for info in company_infos:
        x= extract_company_info(info)
        if x != None :
            brands.append(x)

    return brands



# brand_link -> jobs={local,title,company,pay}각각의 brand 사이트 마다 jobs 정보 뽑기 
def extract_alba_jobs(brand_link) -> dir:
    jobs=[]
    result = requests.get(brand_link)

    # 자료를 뽑자
    soup = BeautifulSoup( result.text , 'html.parser')
    data = soup.find_all("tr", {'style': ""})
    data = data[1:]
    for da in data:
        local  = da.find("td", {'class': 'local'})
        if local == None:
            local = "None"
        else:
            local = local.text

        title = da.find("span", {'class': 'title'})
        if title == None:
            title = "None"
        else:
            title = title.text

        company = da.find("span", {'class': 'company'})
        if company == None:
            company = "None"
        else:
            company = company.text
            # company = re_exp.match(company).group()
            company = re.sub(nre_exp_str,'_', company)

        pay = da.find("span", {'class': 'number'})
        if pay == None:
            pay = "None"
        else:
            pay = pay.text
            
        reg_date = da.find("td", {'class': 'regDate'})
        if reg_date == None:
            reg_date = "None"
        else:
            reg_date = reg_date.text

        time = da.find("span" , {'class': 'time'})
        if time == None:
            time = "None"
        else:
            time = time.text

        jobs.append( {'local':local, 'title':title, 'company':company, 'pay':pay, 'reg_date':reg_date} )
    
    return jobs


# 모든 브랜드 사이트에서 모든 jobs 을 저장하기.
def scraping_all_jobs(brands):
    
    for brand in brands:
        save.save_to_jobs_file(brand)