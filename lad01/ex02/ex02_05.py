so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tiêu_chuan = 44   #Só giờ làm tiêu chuẩn mỗi tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tiêu_chuan)  #Số giờ làm vượt chuẩn mỗi tuần
thuc_linh = gio_tiêu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5  #Tính thù lao thực lĩnh
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")
