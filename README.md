# PersonalCS
Personal Color analysis and Style recommendation Deep Learning Model Team Project

---
### face-parsing


#### [Face Parsing GitHub 저장소](https://github.com/yakhyo/face-parsing/tree/main)를 기반으로 클론하여 구현되었습니다. 얼굴 이미지를 입력으로 받아 피부 영역을 추출하고, K-Means를 활용하여 피부가 아닌 영역을 피부 영역의 대표 색상으로 채우는 이미지 처리 과정을 포함합니다.

```
git clone https://github.com/chaeeerin/PersonalCS.git
```

```
cd face-parsing
```

colab 환경에서 진행하여 requirement.txt 다운로드 없이 진행했습니다.

```
python inference.py \
    --model resnet18 \
    --weight weights/resnet18.pt \
    --input /path/to/input/images \
    --output /path/to/output/images
```

원본 이미지
![image](https://github.com/user-attachments/assets/1008b8fd-66f0-490a-a928-b823b7a24293)

전처리 후 이미지
![image](https://github.com/user-attachments/assets/ab99fec6-8fb0-4bb2-bf81-d67a517c7539)
