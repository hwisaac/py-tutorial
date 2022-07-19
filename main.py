from alba import extract_alba_brands, scraping_all_jobs
from save import save_to_brands_file


#알바몬 첫페이지에서 회사 목록을 구하기
brands = extract_alba_brands()
# 회사목록 저장하기
save_to_brands_file(brands)

#brands 에서 모든 brand 의 일자리 저장하기
scraping_all_jobs(brands)
