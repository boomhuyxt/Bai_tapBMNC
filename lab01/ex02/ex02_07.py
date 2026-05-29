# Nhập các dòng từ người dùng 
print("Nhập các dòng văn bản (nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
# In ra các dòng đã nhập thành chữ hoa
print("Các dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())
    