import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def checkup(i,j):
	if i>0 :
		return True
	else :
		return False
def checkdown(m,i,j):
	if i<m-1:
		return True
	else :
		return False
def  checkright(i,j,n):
	if j<n-1:
		return True
	else :
		return False
def checkleft(i,j):
	if j>0:
		return True
	else:
		return False

	
	
def nearby(dist, m,n,i,j):
	## move up if possible
	#print dist
	t = []
	check = []
	tup = [i,j]
	t.append(tup)
	check.append(tup)
	while (len(t)>0):
		#print "Runiing loop"
		temp = t[0]
		ii = temp[0]
		jj = temp[1]
		del t[0]
		if (ii>1 and jj<n-1):
			if  (checkup(ii,jj) and dist[ii-1][jj]==1 and ii<m-1):
				dist[ii-1][jj] = 0
			#	print check
				return (dist,[ii-1,jj])
			elif (checkup(ii,jj) and dist[ii-1][jj] ==0):
				temp1 = [ii-1,jj]
				if (temp1 not in check):
					t.append(temp1)
					check.append(temp1)
		if (ii<m-2 and jj<n-1):
			if(checkdown(m,ii,jj)and dist[ii+1][jj]==1):
				dist[ii+1][jj]=0
			#	print (ii+1,jj)
				return(dist,[ii+1,jj])
			elif(checkdown(m,ii,jj) and dist[ii+1][jj]==0):
				temp1=[ii+1,jj]
				if(temp1 not in check):
					t.append(temp1)	
					check.append(temp1)
		if (ii<m-1 and jj<n-2):
			if  (checkright(ii,jj,n) and dist[ii][jj+1]==1):
				dist[ii][jj+1] = 0
			#	print check
				return (dist,[ii,jj+1])
			elif (checkright(ii,jj,n) and dist[ii][jj+1] ==0):
				temp1 = [ii,jj+1]
				if (temp1 not in check):
					t.append(temp1)
					check.append(temp1)
		if (ii>m-1 and jj<0 and jj<n-1):
			if  (checkleft(ii,jj) and dist[ii][jj-1]==1  and jj<n-1):
				dist[ii][jj-1] = 0
	     		#	print check 
				return (dist,[ii,jj-1])
			elif (checkleft(ii,jj) and  dist[ii][jj-1] ==0):
				temp1 = [ii,jj-1]
				if (temp1 not in check):
					t.append(temp1)
					check.append(temp1)

		if(checkup(ii,jj) and checkright(ii,jj,m)==True):
			if(ii>0 and ii<m-1 and jj<n-2 and jj>0):
				if(dist[ii-1][jj+1]==1):
					dist[ii-1][jj+1]=0
					return(dist,[ii-1,jj+1])
				else:
					temp1 = [ii-1,jj+1]
					if (temp1 not in check):
						t.append(temp1)
						check.append(temp1)

		if(checkup(ii,jj) and checkleft(ii,jj)==True):
			if(ii>0 and ii<m-1 and jj>0 and jj<n-1):
				if(dist[ii-1][jj-1]==1):
					dist[ii-1][jj-1]=0
					return(dist,[ii-1,jj-1])
				else:
					temp1 = [ii-1,jj-1]
					if (temp1 not in check):
						t.append(temp1)
						check.append(temp1)

		if(checkdown(m,ii,jj) and checkright(ii,jj,n)==True):
			if (ii<m-2 and jj<n-2):
				if(dist[ii+1][jj+1]==1):
					dist[ii+1][jj+1]=0
					return(dist,[ii+1,jj+1])
				else:
					temp1 = [ii+1,jj+1]
					if (temp1 not in check):
						t.append(temp1)
						check.append(temp1)

		if(checkdown(m,ii,jj) and checkleft(ii,jj)==True):
			if(ii<m-2 and jj>0 and jj<n-1):			
				if(dist[ii+1][jj-1]==1):
					dist[ii+1][jj-1]=0
					return(dist,[ii+1,jj-1])
				else:
					temp1 = [ii+1,jj-1]
					if (temp1 not in check):
						t.append(temp1)
						check.append(temp1)

	return (dist,(-1,-1))



def Sobel(arr,rstart, cstart,masksize, divisor):
  sum = 0;
  x = 0
  y = 0

  for i in range(rstart, rstart+masksize, 1):
    x = 0
    for j in range(cstart, cstart+masksize, 1):
        if x == 0 and y == 0:
            p1 = arr[i][j]
        if x == 0 and y == 1:
            p2 = arr[i][j]
        if x == 0 and y == 2:
            p3 = arr[i][j]
        if x == 1 and y == 0:
            p4 = arr[i][j]
        if x == 1 and y == 1:
            p5 = arr[i][j]           
        if x == 1 and y == 2:
            p6 = arr[i][j]
        if x == 2 and y == 0:
            p7 = arr[i][j]
        if x == 2 and y == 1:
            p8 = arr[i][j]
        if x == 2 and y == 2:
            p9 = arr[i][j]
        x +=1
    y +=1
  return np.abs((p1 + 2*p2 + p3) - (p7 + 2*p8+p9)) + np.abs((p3 + 2*p6 + p9) - (p1 + 2*p4 +p7)) 


def padwithzeros(vector, pad_width, iaxis, kwargs):
   vector[:pad_width[0]] = 0
   vector[-pad_width[1]:] = 0
   return vector

im = Image.open('e.jpg')
img = np.asarray(im)
img.flags.writeable = True
p = 1
k = 2
m = img.shape[0]
n = img.shape[1]
masksize = 3
img = np.lib.pad(img, p, padwithzeros) #this function padds image with zeros to cater for pixels on the border.
x = 0
y = 0
f=np.zeros(shape=(m,n))
h=np.zeros(shape=(m,n))
for row in img:
  y = 0
  for col in row:
    if not (x < p or y < p or y > (n-k) or x > (m-k)):
        a1 = Sobel(img, x-p,y-p,masksize,masksize*masksize)
	h[x][y]=a1
#	if (a1[1]+a1[2]+a1[3])/3>100:
	if a1>100:
		f[x][y]=1
	else:
		f[x][y]=0
    y = y + 1
  x = x + 1
print x
print y
			
t = []
temp = [0,0]
while ((temp[0])!=-1):
	f,temp = nearby(f,x-1,y-1,temp[0],temp[1])
	t.append(temp)
del t[len(t)-1]
print t

img2 = Image.fromarray(h)
img2.show()
