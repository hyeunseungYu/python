from pdf2image import convert_from_path

# PDF 파일 경로 지정
pdf_path = "/Users/yuhyeonseung/Desktop/4차 설계반 QR.pdf"


# PDF를 이미지로 변환
images = convert_from_path(pdf_path)

# 이미지를 PNG로 저장
for i, image in enumerate(images):
    image.save(f"/Users/yuhyeonseung/Desktop/output_{i+1}.png", "PNG")
