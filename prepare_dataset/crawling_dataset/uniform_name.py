import os
season="winter"
#경로 설정
base_dir = "{local}\\dataset_origin\\winter"

#연예인 폴더를 가져오기
celeb_folders = [folder for folder in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, folder))]

#연예인 폴더에 따라 00~15 사이 인덱스 부여
for idx, celeb_folder in enumerate(celeb_folders):
    celeb_path = os.path.join(base_dir, celeb_folder)
    
    #연예인 번호는 00~15까지 부여
    celeb_number = str(idx).zfill(2)
    
    #해당 연예인 폴더 안의 이미지 파일 목록 가져오기
    image_files = [file for file in os.listdir(celeb_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    #이미지 파일 개수를 최대 200장으로 제한
    selected_images = image_files[:200]
    extra_images = image_files[200:]  #200장 이후 남은 사진들
    
    #파일 이름 변경
    for img_idx, image_file in enumerate(selected_images):
        old_path = os.path.join(celeb_path, image_file)
        new_name = f"{season}_{celeb_number}_{str(img_idx).zfill(3)}.png"  # winter_00_000 형식
        new_path = os.path.join(celeb_path, new_name)
        
        # 파일 이름 변경
        os.rename(old_path, new_path)
    
    #200장 이후의 파일 삭제
    for image_file in extra_images:
        os.remove(os.path.join(celeb_path, image_file))

    print(f"Processed {len(selected_images)} images in folder {celeb_folder} as {celeb_number}. Deleted {len(extra_images)} extra images.")