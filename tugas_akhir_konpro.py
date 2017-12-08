# Perkalian
num = int(input("Tampilkan tabel perkalian dari? "))  
   
for i in range(1,11):  
   print(num,'x',i,'=',num*i)
   
   
# Calender
import calendar
# Enter the month and year  
yy = int(input("Masukkan Tahun: "))  
mm = int(input("Masukkan Bulan: "))  
  
# display the calendar  
print(calendar.month(yy,mm))