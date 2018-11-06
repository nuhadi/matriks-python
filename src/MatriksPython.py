import pygame
import math
import sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = []
simpanan = []
edges = []
surf = []
surfa = ()
surfaces = []

def Baca(i,x,y):
    verticies.insert(i,((x/100),(y/100)))
    simpanan.insert(i,((x/100),(y/100)))
    if i>0:
        edges.insert(i,(i,i-1))

def bacapermukaan(sisi):
    i = 0
    for every in verticies:
        surf.insert(0,i)
        i = i+1
    surfa = tuple(surf)
    surfaces.insert(0,surfa)
    
def translate(a,b): #fungsi tranlasi pada titik
    for n,i in enumerate(verticies):
        (x,y)=verticies[n]
        x=x+(a/100)
        y=y+(b/100)
        verticies[n]=(x,y)

def dilate(k):  #fungsi dilatasi objek dengan faktor scalling k
    for n,i in enumerate(verticies):
        (x,y)=verticies[n]
        x=x*k
        y=y*k
        verticies[n]=(x,y)

def rotate(deg,a,b): #fungsi rotasi searah jarum jam sebesar deg derajat terhadap titik a,b 
    for n,i in enumerate(verticies):
        (x,y) = verticies[n]
        c = x-(a/100)
        d = y-(b/100)
        x = (((c)*(math.cos(math.radians(deg)))) - ((d)*(math.sin(math.radians(deg)))))+a
        y = (((c)*(math.sin(math.radians(deg)))) + ((d)*(math.cos(math.radians(deg)))))+b
        verticies[n]=(x,y)

def reflect(param):
    if param == 'x':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            y = -y
            verticies[n]=(x,y)
    elif param == 'y':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            x = -x
            verticies[n]=(x,y)
    elif param == 'y=x':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            a = x
            x = y
            y = a
            verticies[n]=(x,y)
    elif param == 'y=-x':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            a = x
            x = -y
            y = -a
            verticies[n]=(x,y)
    else:        #param=(a,b)
        i = []
        for t in param.split():
            try:
                i.append(float(t))
            except ValueError:
                pass
        a = i[0]
        b = i[1]
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
             x = 2*(a/100) - x
            y = 2*(b/100) - y
            verticies[n]=(x,y)

def shear(param,k):
    if param == 'x':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            x = x + (k/100)*y
            verticies[n]=(x,y)
    if param == 'y':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            y = y + (k/100)*x
            verticies[n]=(x,y)

def stretch(param,k):
    if param == 'x':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            x = x*k
            verticies[n]=(x,y)
    if param == 'y':
        for n,i in enumerate(verticies):
            (x,y) = verticies[n]
            y = y*k
            verticies[n]=(x,y)    


def custom(a,b,c,d):    #melakukan transformasi linier pada objek dengan matriks
    for n,i in enumerate(verticies):
        (x,y) = verticies[n]
        e = x
        f = y
        x = (a*e + f*c)/100
        y = (b*e + f*d)/100
        verticies[n]=(x,y)

def multiple(n):
    operasi = []
    i = 0
    print("Menu transformasi:")
    print("1. Translate")
    print("2. Dilate")
    print("3. Rotate")
    print("4. Reflect")
    print("5. Shear")
    print("6. Stretch")
    print("7. Custom")
    while i < n:
        s=int(input())
        operasi.insert(i, s)
        i=i+1
    i = 0
    for n,i in enumerate(operasi):
        if operasi[n]==1:        #masuk fungsi translate
            print('Ketik: translate <sumbux> <sumbuy>')
            pilihan = input('')
            i = []
            for t in pilihan.split():
                try:
                    i.append(float(t))
                except ValueError:
                    pass
            a = i[0]
            b = i[1]
            translate(a,b)
        if operasi[n]==2:        #Masuk fungsi dilate
            print('Ketik: dilate <faktor>')
            pilihan = input('')
            i = []
            for t in pilihan.split():
                try:
                    i.append(float(t))
                except ValueError:
                    pass
            k = i[0]
            dilate(k)
        if operasi[n]==3:        #Masuk fungsi rotate
            print('Ketik: rotate <deg> <korx> <kory>')
            pilihan = input('')
            i = []
            for t in pilihan.split():
                try:
                    i.append(float(t))
                except ValueError:
                    pass
            a = i[0]
            b = i[1]
            c = i[2] 
            rotate(a,b,c)
        if operasi[n]==4:        #Masuk fungsi reflect
            print('Pilihan pencerminan: ')
            print('1. x')
            print('2. y')
            print('3. y=x')
            print('4. y=-x')
            print('5. ( a , b )')
            print('Masukan paramenter contoh: reflect y=x | reflect ( a , b )')
            pilihan = input('reflect ')
            reflect(pilihan)
        if operasi[n]==5:        #Masuk fungsi Shear
            sumbu = input('Masukan sumbu: ')
            k = int(input('Masukan faktor pergeseran: '))
            shear(sumbu,k)
        if operasi[n]==6:        #Masuk fungsi Stretch
            sumbu = input('Masukan sumbu: ')
            k = int(input('Masukan faktor stretch: '))
            shear(sumbu,k)
        if operasi[n]==7:        #Masuk fungsi Custom
            print('Ketik: custom <a> <b> <c> <d>')
            pilihan = input('')
            i = []
            for t in pilihan.split():
                try:
                    i.append(float(t))
                except ValueError:
                    pass
            a = i[0]
            b = i[1]
            c = i[2]
            d = i[3] 
            custom(a,b,c,d)

def reset():
    for n,i in enumerate(verticies):
            verticies[n]=simpanan[n]

def exit():
    False
    sys.exit(0)

def menu():       #memunculkan tampilan menu          
    print("Menu transformasi:")
    print("0. Change value")
    print("1. Translate")
    print("2. Dilate")
    print("3. Rotate")
    print("4. Reflect")
    print("5. Shear")
    print("6. Stretch")
    print("7. Custom")
    print("8. Multiple")
    print("9. Reset")
    print("10. Exit")
    s = int(input("Masukkan nomor pilihan: "))
    if s==0:
        i = int(input("Masukkan banyaknya sudut: "))
        count = 0
        while count <=(i-1):
            x = float(input("Masukkan koordinat x ke-%d: "%(count+1)))
            y = float(input("Masukkan koordinat y ke-%d: "%(count+1)))
            Baca(count,x,y)
            count=count+1
        edges.insert(0,(count-1,0))
    if s==1:        #masuk fungsi translate
        print('Ketik: translate <sumbux> <sumbuy>')
        pilihan = input('')
        i = []
        for t in pilihan.split():
            try:
                i.append(float(t))
            except ValueError:
                pass
        a = i[0]
        b = i[1]
        translate(a,b)
    if s==2:        #Masuk fungsi dilate
        print('Ketik: dilate <faktor>')
        pilihan = input('')
        i = []
        for t in pilihan.split():
            try:
                i.append(float(t))
            except ValueError:
                pass
        k = i[0]
        dilate(k)
    if s==3:        #Masuk fungsi rotate
        print('Ketik: rotate <deg> <korx> <kory>')
        pilihan = input('')
        i = []
        for t in pilihan.split():
            try:
                i.append(float(t))
            except ValueError:
                pass
        a = i[0]
        b = i[1]
        c = i[2] 
        rotate(a,b,c)
    if s==4:        #Masuk fungsi reflect
        print('Pilihan pencerminan: ')
        print('1. x')
        print('2. y')
        print('3. y=x')
        print('4. y=-x')
        print('5. ( a , b )')
        print('Masukan paramenter contoh: reflect y=x | reflect ( a , b )')
        pilihan = input('reflect ')
        reflect(pilihan)
    if s==5:        #Masuk fungsi Shear
        sumbu = input('Masukan sumbu: ')
        k = int(input('Masukan faktor pergeseran: '))
        shear(sumbu,k)
    if s==6:        #Masuk fungsi Stretch
        sumbu = input('Masukan sumbu: ')
        k = int(input('Masukan faktor stretch: '))
        stretch(sumbu,k)
    if s==7:        #Masuk fungsi Custom
        print('Ketik: custom <a> <b> <c> <d>')
        pilihan = input('')
        i = []
        for t in pilihan.split():
            try:
                i.append(float(t))
            except ValueError:
                pass
        a = i[0]
        b = i[1]
        c = i[2]
        d = i[3] 
        custom(a,b,c,d)
    if s==8:        #fungsi multiple
        banyak = int(input('Masukan banyak operasi yang diinginkan: '))
        multiple(banyak)
    if s==9:        #Masuk fungsi reset
        reset()
    if s==10:        #Masuk fungsi exit
        exit()

print("__________________________________________________________________________")
print("__________________________________________________________________________")
print("___________   ___.                      _____  .__                        ")
print("\__    ___/_ _\_ |__   ____   ______   /  _  \ |  |    ____   ____  ____  ")
print("  |    | |  |  \ __ \_/ __ \ /  ___/  /  /_\  \|  |   / ___\_/ __ \/  _ \ ")
print("  |    | |  |  / \_\ \  ___/ \___ \  /    |    \  |__/ /_/  >  ___(  <_> )")
print("  |____| |____/|___  /\___  >____  > \____|__  /____/\___  / \___  >____/ ")
print("                   \/     \/     \/          \/     /_____/      \/       ")
print("__________________________________________________________________________")
print("          BY: Nuha Adinata(13516120) & Dias Akbar Nugraha(13516142)       ")
print("__________________________________________________________________________")
                                                                                                                  



i = int(input("Masukkan banyaknya sudut: "))
count = 0
while count <=(i-1):
    x = float(input("Masukkan koordinat x ke-%d: "%(count+1)))
    y = float(input("Masukkan koordinat y ke-%d: "%(count+1)))
    Baca(count,x,y)
    count=count+1
bacapermukaan(verticies)
edges.insert(0,(count-1,0))

def Kotak():
    glBegin(GL_POLYGON)
    for surface in surfaces:
        glColor3fv((0,1,0))  
        for vertex in surface:
            glVertex2fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(verticies[vertex])
    glEnd()

pygame.init()
display = (600,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluPerspective(90, (display[0]/display[1]), 4, 500.0)

glTranslatef(0.0,0.0,-5)
glRotatef(0,0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-400.0, 0.0)
    glVertex2f(400.0, 0.0)
    glVertex2f(400.0, 0.0)
    glVertex2f(300.0, 100.0)
    glVertex2f(400.0, 0.0)
    glVertex2f(300.0, -100.0)
    glEnd()
    glFlush()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, -400.0)
    glVertex2f(0.0, 400.0) 
    glVertex2f(0.0, 400.0)
    glVertex2f(100.0, 300.0)
    glVertex2f(0.0, 400.0)
    glVertex2f(-100.0, 300.0)
    glEnd()
    glFlush()
    glColor3f(0.0, 1.0, 0.0)
    Kotak()

    pygame.display.flip()
    pygame.time.wait(10)
    menu()
