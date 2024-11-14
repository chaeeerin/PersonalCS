from crawlingfromnews import download_images
#input.txt 파일에서 입력 읽어오기
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

#현재 읽어야 할 줄을 나타내는 인덱스
line_idx = 0

#클래스 개수
count = int(lines[line_idx].strip())
line_idx += 1

#클래스 개수만큼 반복
for i in range(count):
    #어떤 톤인지 입력
    tone_type = int(lines[line_idx].strip())
    line_idx += 1

    #해당 톤의 인물 수
    count_tone = int(lines[line_idx].strip())
    line_idx += 1

    #인물별로 검색 및 이미지 다운로드 수행
    for j in range(count_tone):
        # 검색할 인물 이름
        keyword = lines[line_idx].strip()
        line_idx += 1
        # 이미지 다운로드 함수 호출
        download_images(keyword, tone_type)