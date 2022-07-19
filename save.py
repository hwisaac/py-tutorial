import csv
import alba

def save_to_brands_file(brands):
    # open 함수는 파일을 열어준다. 없으면 생성해준다. 쓰기모드 사용.
    file = open('brands.csv', mode='w')
    writer = csv.writer(file)

    writer.writerow(["company", "title", "link"])
    for brand in brands:
        # company 의 value 들을 리스트로 만들기
        writer.writerow(list(brand.values()))

    return

def save_to_jobs_file(brand):
    link = brand['link']
    company_name = brand['company']

    jobs = alba.extract_alba_jobs(link)

    file = open(f'{company_name}.csv', mode='w')
    writer = csv.writer(file)
    
    writer.writerow(["local", "title","company","pay" ,"reg_date"])

# brand -> company.csv 에 jobs 저장
def save_to_jobs_file(brand):
    company = brand['company']
    link = brand['link']
    print( company, link)
    # open 함수는 파일을 열어준다. 없으면 생성해준다. 쓰기모드 사용.
    file = open(f'jobs/{company}.csv', mode='w')
    writer = csv.writer(file)

    writer.writerow(["local", "title", "company", "pay", "reg_date"])
    jobs = alba.extract_alba_jobs(link)
    for job in jobs:
        # job 의 value 들을 리스트로 만들어서 csv 파일에 저장
        writer.writerow(list(job.values()))
    
