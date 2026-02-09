#If
number = 15
if number > 0:
    print("The number is positive")

#Multiple Statements in If Block
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
    print("Welcome back!")



#Elif
#elif adalah cara Python untuk mengatakan
#"jika kondisi sebelumnya tidak benar, maka coba kondisi ini".
#sama seperti else if di C

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#Multiple Elif Statements
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

#When to Use Elif
'''
Gunakan `elif` ketika memiliki beberapa kondisi yang saling
eksklusif untuk diperiksa. Ini lebih efisien daripada
menggunakan beberapa pernyataan `if` terpisah karena Python 
berhenti memeriksa setelah menemukan kondisi yang benar.
'''


#Else
#else menangkap apa pun yang tidak tercakup oleh kondisi sebelumnya.
#contoh

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#How Else Works
#else bekerja sebagai default action jika kondisi sebelumnya tidak terpenuhi



#Short Hand If

#one line if-else
a = 2
b = 330
print("A") if a > b else print("B")

#Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#When to Use Shorthand If
    #Kondisi dan tindakannya sederhana
    #Meningkatkan keterbacaan kode
    #Ingin membuat asssignment cepat berdasarkan suatu kondisi



#Nested If
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#contoh lain
username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")



#The pass Statement
#Pernyataan if tidak boleh kosong, tetapi jika karena suatu alasan 
#Anda memiliki pernyataan if tanpa isi, masukkan pernyataan pass 
#untuk menghindari error.

a = 33
b = 200
if b > a:
    pass

#Why Use pass?
'''
1. Saat Anda membuat struktur kode tetapi belum mengimplementasikan
logikanya.
2. Ketika sebuah pernyataan diperlukan secara sintaksis tetapi tidak
ada tindakan yang dibutuhkan.
3. Sebagai tempat penampung untuk kode di masa mendatang selama 
pengembangan.
4. Dalam fungsi atau kelas kosong yang rencananya akan Anda 
implementasikan nanti.
'''

#contoh penggunaan dalam development
age = 16
if age < 18:
    pass  # TODO: Add underage logic later
else:
    print("Access granted")