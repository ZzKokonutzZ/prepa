import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Im1=[[255,0,128],
#      [64,200,0]]

# Im2=[[[255,0,0],[0,255,0],[0,0,255]],
#      [[128,128,128],[255,255,255],[255,255,0]]]

# plt.imshow(Im1,cmap="gray")
# plt.figure()
# plt.imshow(Im2)


image=mpimg.imread("images TP/chaton_programmeur.png")

# for x in range(198,274) :
#     for y in range(182,220) :
#         image[y][x]=0

def dim(img) :
    return (len(img),len(img[0]))

def neg(img) :
    for y in range(len(img)) :
        for x in range(len(img[y])) :
            img[y][x]=1-img[y][x]
    return img
def miroir(img) :
    new=[]
    ratio=dim(img)
    for y in range(len(img)) :
        new+=[[]]
        for x in range(len(img[y])) :
            new[y]+=[img[y][ratio[1]-x-1]]
    return new

def rotation90gauche(img) :
    ratio=dim(img)
    new=np.zeros((ratio[1],ratio[0],3))
    for y in range(ratio[0]) :
        for x in range(ratio[1]) :
            for alpha in range(3) :
                new[x][y][alpha]=img[y][ratio[1]-x-1][alpha]
    return new

def filtre(ker,img) :
    ratio=dim(img)
    dimk=len(ker)
    min_d=dimk//2
    new=np.zeros((ratio[0],ratio[1],3))
    for y in range(min_d,ratio[0]-min_d) :
        for x in range(min_d,ratio[1]-min_d) :
            for i in range(dimk) :
                for j in range(dimk) :
                    for alpha in range(3) :
                        new[y][x][alpha]+=img[y+i-min_d-1][x+j-min_d-1][alpha]*ker[i][j]
    return new

def kuwahara(img,k) :
    ratio=dim(img)
    new=np.zeros((ratio[0],ratio[1],3))
    for y in range(k,ratio[0]-k) :
        for x in range(k,ratio[1]-k) :
            sensor=np.zeros((2,4,3))
            for i in range(k) :
                for j in range(k) :
                    sensor[0][0]+=img[y-i][x-j]
                    sensor[0][1]+=img[y-i][x+j]
                    sensor[0][2]+=img[y+i][x+j]
                    sensor[0][3]+=img[y+i][x-j]
            sensor/=k**2
            for i in range(k) :
                for j in range(k) :
                    sensor[1][0]+=abs(img[y-i][x-j]-sensor[1][0])
                    sensor[1][1]+=abs(img[y-i][x+j]-sensor[1][1])
                    sensor[1][2]+=abs(img[y+i][x+j]-sensor[1][2])
                    sensor[1][3]+=abs(img[y+i][x-j]-sensor[1][3])
            c=0
            for i in range(4) :
                if sum(sensor[1][c]**2)>sum(sensor[1][i]**2) :
                    c=i
            new[y][x]=sensor[0][c]
            
    return new

box=np.ones((5,5))/25
gauss=np.array([[1,2,1],[2,4,2],[1,2,1]])/16


                    
            
    

new=kuwahara(image,10)

plt.imshow(new)

plt.show()



print(dim(image))