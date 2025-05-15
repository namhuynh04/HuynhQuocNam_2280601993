from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên bởi ID")
    print("3. Xóa sinh viên bởi ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo diểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    
    key = int(input("Nhập lựa chọn của bạn: "))
    if key == 1:
        print("Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công")
    elif key == 2:
        if(qlsv.soLuongSinhVien() > 0):
            print ("Cập nhật thông tin sinh viên")
            print("Nhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sách sinh viên trống")
    elif key == 3:
        if(qlsv.soLuongSinhVien() > 0):
            print ("Xóa sinh viên")
            print("Nhập ID: ")
            ID = int(input())
            if (qlsv.deleteSinhVien(ID)):
                print("\nSinh viên có id = ", ID, " đã được xóa")
            else:
                print("\nSinh viên có id = ", ID, " không tồn tại")
        else:
            print("Danh sách sinh viên trống")
    elif key == 4:
        if(qlsv.soLuongSinhVien() > 0):
            print ("Tìm kiếm sinh viên theo tên")
            print("Nhập tên: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sách sinh viên trống")
    elif key == 5:
        if(qlsv.soLuongSinhVien() > 0):
            print ("Sắp xếp sinh viên theo điểm trung bình (GPA)")
            qlsv.sortByPointAVG()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống")
    elif key == 6:
        if(qlsv.soLuongSinhVien() > 0):
            print ("Sắp xếp sinh viên theo tên chuyên ngành")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống")
    elif key == 7:
        if(qlsv.soLuongSinhVien() > 0):
            print ("Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống")
    elif key == 0:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")