# Muh Isfahani Ghiyath
# Monday, March 13 2017

# firstGuess:
a = input('insert a : ')
b = input('insert b : ')

def fungsi(x):
    return (x * x) - 4 # func: x^2 - 4

def hitungC(a, b):
    return a + ((b - a) / 2)

c = hitungC(a, b)
fa = fungsi(a)
fb = fungsi(b)
fc = fungsi(c)

for x in range(1, 6): # 1 until 5
    if (fc == 0): break
    print "===== ", x, " ====="
    if (x == 1):
        print "a :", a, ", f(a) :", fa
        print "b :", b, ", f(b) :", fb
        print "c :", c, ", f(c) :", fc
    else:
        if (fa * fc) < 0:
            b = c
            fb = fungsi(b)
            c = hitungC(a, b)
            fc = fungsi(c)
            print "a :", a, ", f(a) :", fa
            print "b :", b, ", f(b) :", fb
            print "c :", c, ", f(c) :", fc
        elif (fc * fb) < 0:
            a = c
            fa = fungsi(a)
            c = hitungC(a, b)
            fc = fungsi(c)
            print "a :", a, ", f(a) :", fa
            print "b :", b, ", f(b) :", fb
            print "c :", c, ", f(c) :", fc

print "\nHasil : ", c
