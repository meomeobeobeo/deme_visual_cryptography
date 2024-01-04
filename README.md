## Two Step Encryption
### Introduction
Giới thiệu

Áp dụng kỹ thuật Steganography, sau đó là Mật mã hình ảnh. Triển khai dựa trên bài nghiên cứu có tiêu đề "Combine use of Steganography and Visual Cryptography for Secured Data hiding in Computer Forensics"

Steganography là phương pháp ẩn dữ liệu bí mật bên trong bất kỳ dạng phương tiện kỹ thuật số nào. Ý tưởng chính đằng sau kỹ thuật giấu tin là che giấu sự tồn tại của dữ liệu trong bất kỳ phương tiện nào như âm thanh, video, hình ảnh, v.v.

Mật mã hình ảnh là một kỹ thuật mã hóa cho phép thông tin hình ảnh (hình ảnh, văn bản, v.v.) được mã hóa theo cách mà thông tin được giải mã xuất hiện dưới dạng hình ảnh trực quan.

Ngành kiến ​​​​trúc

### Architecture
![image](https://i.imgur.com/nh0J1Sn.png)

### Project
##### Structure
```
.
├── images
├── main.py
├── README.md
├── Reference_paper.pdf
├── requirements.txt
└── src
    ├── lsb_stegno.py
    └── n_share.py
```

##### File description
| File          | Description                                    |
|---------------|-----------------------------------------------------------|
| lsb_stegno.py | Methods to Encode and Decode data using LSB Steganography |
| n_share.py    | Methods to Split and Compress LSB Encoded images          |

### Algorithms
##### Steganography
###### Encoding data in image
```python
# Putting modified pixels in the new image
newimg.putpixel((x, y), pixel)
if (x == w - 1):
    x = 0
    y += 1
else:
    x += 1
```

###### Decoding data from image
```python
# string of binary data
binstr = ''

for i in pixels[:8]:
    if (i % 2 == 0):
        binstr += '0'
    else:
        binstr += '1'

data += chr(int(binstr, 2))
if (pixels[-1] % 2 != 0):
    return data
```
##### Visual Cryptography
###### Generating shares
```python
#Tách hình ảnh dựa trên yếu tố ngẫu nhiên
n = int(np.random.randint(data[i, j, k] + 1))
img1[i, j, k] = n
img2[i, j, k] = data[i, j, k] - n
```

###### hợp nhất
```python
img[i, j, k] = img1[i, j, k] + img2[i, j, k]
```

##### Usage
###### Setup
Install dependencies
```
pip install -r requirements.txt
```
Run using python
```
streamlit run main.py
```

