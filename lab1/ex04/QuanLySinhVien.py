from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
        
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh vien: ")
        sex = input("Nhập giới tinh sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        pointAVG = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, pointAVG)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)


    