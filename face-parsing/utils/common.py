import cv2
import numpy as np
from sklearn.cluster import KMeans

ATTRIBUTES = [
    'skin',
    'l_brow',
    'r_brow',
    'l_eye',
    'r_eye',
    'eye_g',
    'l_ear',
    'r_ear',
    'ear_r',
    'nose',
    'mouth',
    'u_lip',
    'l_lip',
    'neck',
    'neck_l',
    'cloth',
    'hair',
    'hat'
]

COLOR_LIST = [
    [0, 0, 0],
    [255, 85, 0],
    [255, 170, 0],
    [255, 0, 85],
    [255, 0, 170],
    [0, 255, 0],
    [85, 255, 0],
    [170, 255, 0],
    [0, 255, 85],
    [0, 255, 170],
    [0, 0, 255],
    [85, 0, 255],
    [170, 0, 255],
    [0, 85, 255],
    [0, 170, 255],
    [255, 255, 0],
    [255, 255, 85],
    [255, 255, 170],
    [255, 0, 255],
]

def fill_background_kmeans(image, segmentation_mask, save_image=False, save_path="result.png", filename=' '):
    # 원본 이미지를 numpy 배열로 변환
    skin_class_index=1
    k_clusters=4
    # 원본 이미지를 numpy 배열로 변환
    image = np.array(image).copy()  # (H, W, 3) 형식의 RGB 이미지

    # 피부 이진 마스크 생성 (피부 부분: 1, 나머지: 0)
    skin_mask = (segmentation_mask == skin_class_index).astype(np.uint8)

    # 피부 픽셀이 없는 경우
    if np.sum(skin_mask) == 0:
        print(f"Skipping image: {filename} (No skin detected)")
        return None  # 건너뜀

    # 피부 부분 픽셀 추출
    skin_pixels = image[skin_mask == 1].reshape(-1, 3)  # (N, 3) 형태로 변환

    if len(skin_pixels) < k_clusters:
        print(f"Skipping image: {filename} (Not enough skin pixels for K-Means)")
        return None

    # K-Means로 클러스터링
    kmeans = KMeans(n_clusters=k_clusters, random_state=42).fit(skin_pixels)
    cluster_labels, cluster_centers = kmeans.labels_, kmeans.cluster_centers_

    # 가장 큰 클러스터 찾기
    unique_labels, label_counts = np.unique(cluster_labels, return_counts=True)
    largest_cluster_index = unique_labels[np.argmax(label_counts)]  # 가장 큰 클러스터
    representative_color = cluster_centers[largest_cluster_index].astype(np.uint8)

    # 피부가 아닌 부분에 대표 색상 적용
    non_skin_mask = 1 - skin_mask  # 피부가 아닌 부분
    result_image = image.copy()
    result_image[non_skin_mask == 1] = representative_color  # 피부가 아닌 부분에 대표 색상 적용

    # 저장 옵션
    if save_image:
        cv2.imwrite(save_path, cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR))

    return result_image


def vis_parsing_maps(image, segmentation_mask, save_image=False, save_path="result.png"):
    # Create numpy arrays for image and segmentation mask
    image = np.array(image).copy().astype(np.uint8)
    segmentation_mask = segmentation_mask.copy().astype(np.uint8)

    # Create a color mask
    segmentation_mask_color = np.zeros((segmentation_mask.shape[0], segmentation_mask.shape[1], 3))

    num_classes = np.max(segmentation_mask)

    for class_index in range(1, num_classes + 1):
        class_pixels = np.where(segmentation_mask == class_index)
        segmentation_mask_color[class_pixels[0], class_pixels[1], :] = COLOR_LIST[class_index]

    segmentation_mask_color = segmentation_mask_color.astype(np.uint8)

    # Convert image to BGR format for blending
    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Blend the image with the segmentation mask
    blended_image = cv2.addWeighted(bgr_image, 0.6, segmentation_mask_color, 0.4, 0)

    # Save the result if required
    if save_image:
        cv2.imwrite(save_path, segmentation_mask)
        cv2.imwrite(save_path, blended_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    return blended_image


def letterbox(image, target_size, fill_color=(0, 0, 0)):
    w, h = image.size

    # calculate scale factor based on target aspect ratio
    scale = min(target_size[0] / w, target_size[1] / h)

    # new image dimensions based on scale
    new_w = int(w * scale)
    new_h = int(h * scale)

    # resize the image with antialiasing for better quality
    resized_image = image.resize((new_w, new_h), resample=Image.BILINEAR)

    # calculate padding dimensions
    pad_w = target_size[0] - new_w
    pad_h = target_size[1] - new_h

    # create a new image with target size and fill color
    letterbox_image = Image.new("RGB", target_size, fill_color)

    # paste the resized image at the center of the letterbox image
    letterbox_image.paste(resized_image, (pad_w // 2, pad_h // 2))

    return letterbox_image
