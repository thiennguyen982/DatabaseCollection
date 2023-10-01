from mysql.connector import connect, Error

conn = connect(
    host = 'localhost',
    user='root',
    password='',
    database='quanlysinhvien',
    port=3306
)

cursor = conn.cursor()

# Call procedure
# args = ['C00', None, None]
# results = cursor.callproc('find_student_by_id', args)
# print(results[1], results[2])
# conn.close()

# Execute
# sql = 'SELECT * FROM sinhvien'
# cursor.execute(sql)
# for row in cursor:
#     print(row)
# conn.close()

# sql1 = 'SELECT version()'
# sql2 = 'SELECT * FROM sinhvien WHERE HocBong > %s AND GioiTinh = %s'
# sql3 = 'SELECT 1+1'

# HocBong = int(input("Input HocBong: "))
# GioiTinh = int(input("Input GioiTInh (1. Nam - 0.Nu): "))

# list_sql = [sql1, sql2, sql3]
# data = (HocBong, GioiTinh)

# results = cursor.execute(';'.join(list_sql), data, multi=True)
# count = 1
 
# for result in results:
#     print("Query {count}: {result.statement}")
#     if result.with_rows:
#         for row in result:
#             print(row)
#         count += 1
#     else:
#         print("No result found")
#     print()

# cursor.close()


# sql = \
# """
#     UPDATE sinhvien SET HocBong = %(hoc_bong)s, DiaChi = %(dia_chi)s WHERE SinhVienID = %(sinh_vien_id)s
# """

# list_data = [
#     {'hoc_bong': 300000, 'dia_chi': 'TPHCM', 'sinh_vien_id': 'C01'},
#     {'hoc_bong': 400000, 'dia_chi': 'Ha Noi', 'sinh_vien_id': 'T00'},
#     {'hoc_bong': 500000, 'dia_chi': 'Long An', 'sinh_vien_id': 'T03'},
# ]

# for data in list_data:
#     cursor.execute(sql, data)

# cursor.close()

# Execute many

# sql = \
# """
#     UPDATE sinhvien SET HocBong = %(hoc_bong)s, DiaChi = %(dia_chi)s WHERE SinhVienID = %(sinh_vien_id)s
# """

# list_data = [
#     {'hoc_bong': 30000, 'dia_chi': 'TPHCM', 'sinh_vien_id': 'C01'},
#     {'hoc_bong': 40000, 'dia_chi': 'Ha Noi', 'sinh_vien_id': 'T00'},
#     {'hoc_bong': 50000, 'dia_chi': 'Long An', 'sinh_vien_id': 'T03'},
# ]

# cursor.executemany(sql, list_data)

# cursor.close()

# sql = \
# """
#     INSERT INTO sinhvien VALUES (%(sinh_vien_id)s, %(ho_sinh_vien)s, %(ten_sinh_vien)s, %(ngay_sinh)s,\
#         %(gioi_tinh)s, %(dia_chi)s, %(hoc_bong)s, %(khoa_id)s)
# """

# list_data = [
#     {'sinh_vien_id': 'TE1', 'ho_sinh_vien': 'Trần Thị','ten_sinh_vien': 'Thắm', 'ngay_sinh': '1900-05-21', 
#      'gioi_tinh': 0, 'dia_chi': 'Hai Phong', 'hoc_bong': 800000, 'khoa_id': 'VL'},
#     {'sinh_vien_id': 'TE2', 'ho_sinh_vien': 'Trần Thị','ten_sinh_vien': 'Thúy', 'ngay_sinh': '1900-05-21', 
#      'gioi_tinh': 0, 'dia_chi': 'Kien Giang', 'hoc_bong': 800000, 'khoa_id': 'VL'}
# ]

# cursor.executemany(sql, list_data)

# cursor.close()