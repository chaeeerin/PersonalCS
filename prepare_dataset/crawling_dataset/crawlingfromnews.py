from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.request
import os


def download_images(keyword, tone):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)

    url = "https://www.naver.com/"
    driver.get(url)

    driver.implicitly_wait(10)  # 대기 시간 설정 (최대 10초 대기)

    #구글 이미지 사이트에서, 우리가 원하는 키워드를 입력하고, 검색을 진행
    #검색어 입력하는 요소를 찾음
    elem = driver.find_element(By.CSS_SELECTOR, "#query")
    elem.send_keys(keyword + Keys.ENTER)  #원하는 검색어 입력 후 엔터

    #이미지로 이동
    driver.find_element(By.CSS_SELECTOR, "#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(3) > a").click()

    #옵션 클릭
    driver.find_element(By.CSS_SELECTOR, "#snb > div.mod_group_option_filter.image_option._search_option_simple_wrap > div > div.option_filter > a").click()
    time.sleep(1)

    items=driver.find_elements(By.CSS_SELECTOR, "#snb > div.mod_group_option_sort._search_option_detail_wrap > ul > li.bx.source > div > div > a")
    time.sleep(1)
    for item in items:
        if item.text=="포토뉴스":
            item.click()
            time.sleep(5)
            break

    #결과 이미지를 다운로드 받을 부분
    elem = driver.find_element(By.TAG_NAME, "body")

    for i in range(37):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    links = []

    images = driver.find_elements(By.CSS_SELECTOR, "#main_pack > section > div.api_subject_bx._fe_image_tab_grid_root.ani_fadein > div > div > div.image_tile._fe_image_tab_grid > div > div > div > div > img")
    if not images:
        print("not find")

    for image in images:
        if image.get_attribute('src') is not None:
            links.append(image.get_attribute('src'))

    print("찾은 이미지 개수 :", len(links))

    #저장 경로 설정
    if tone==1:
        base_dir = "{local}\\dataset_origin\\spring"
    if tone==2:
        base_dir = "{local}\\dataset_origin\\summer"
    if tone==3:
        base_dir = "{local}\\dataset_origin\\fall"
    if tone==4:
        base_dir = "{local}\\dataset_origin\\winter"

    folder_dir = f"{base_dir}\\{keyword}"
    os.makedirs(folder_dir, exist_ok=True)
    for k, i in enumerate(links):
        order_n = i
        save_point = f"{folder_dir}\\{keyword}{str(k)}.jpg"
        urllib.request.urlretrieve(order_n, save_point)