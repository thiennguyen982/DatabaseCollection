from mysql.connector import connect, Error
import pymysql

%load_ext sql

host = 'localhost'
user = 'root'
password = ''
database = 'quanlysinhvien'

cnnx_str = f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'

%sql $cnnx_str

data = %sql select * from sinhvien where KhoaID = 'VL' 