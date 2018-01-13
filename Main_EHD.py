# Sikandar 13 - 1 - 2018 (Saturday)
# Querry Image Search Using Edge Histogram Descriptor (EHD)
# Generate EHD of all the MirFlickr images (25k images, jpg format)

#libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from EdgeHistogramComputer import EdgeHistogramComputer

# read image

img = cv2.imread('im1.jpg')

#cv2.imshow('image', img)
#cv2.waitKey(0)

computer = EdgeHistogramComputer(4,4)
descriptor = computer.compute(img) #so descriptor is a vector of 2 x 2 x 32 dimensions
print descriptor.tolist()
print len(descriptor)

descriptor_reshaped = descriptor.reshape(16,5)
print descriptor_reshaped

print "Vertical"
# add vertical group
vert = np.zeros([4,5])
for i in range(0,4):
    vert[i,:] = sum(descriptor_reshaped[range(i,16,4),:])/4

print vert

print "horizontal"
hori = np.zeros([4,5])
for i in range(0,4):
    hori[i,:] =  sum (descriptor_reshaped[i*4+0:i*4+4,:])/4


print hori


print "neighbors"
neighbor1 = (descriptor_reshaped[0,:] + descriptor_reshaped[1,:] + descriptor_reshaped[4,:] + descriptor_reshaped[5,:])/4# 1 2 5 6 (in python 0 1 4 5)
print neighbor1

neighbor2 = (descriptor_reshaped[2,:] + descriptor_reshaped[3,:] + descriptor_reshaped[6,:] + descriptor_reshaped[7,:])/4# 3 4 7 8 (in python 2 3 6 7)
print neighbor2

neighbor3 = (descriptor_reshaped[8,:] + descriptor_reshaped[9,:] + descriptor_reshaped[12,:] + descriptor_reshaped[13,:])/4# 9 10 13 14 (in python 8 9 12 13)
print neighbor3

neighbor4 = (descriptor_reshaped[10,:] + descriptor_reshaped[11,:] + descriptor_reshaped[14,:] + descriptor_reshaped[15,:])/4# 11 12 15 16 (in python 10 11 14 15)
print neighbor4

neighbor5 = (descriptor_reshaped[5,:] + descriptor_reshaped[6,:] + descriptor_reshaped[9,:] + descriptor_reshaped[10,:])/4# 6 7 10 11 (in python 5 6 9 10)
print neighbor5

print "global"
global_des =  sum(descriptor_reshaped[:,:])/16
print global_des

print "concatinate"
#EHD_vector = descriptor_reshaped
#EHD_vector.append(vert)
#EHD_vector = np.concatenate((descriptor_reshaped,vert))
EHD_vector1 = np.append(descriptor_reshaped,vert)
EHD_vector2 = np.append(hori,neighbor1);
EHD_vector3 = np.append(neighbor2,neighbor3)
EHD_vector4 = np.append(neighbor4,neighbor5)
EHD_vector5 = np.append(global_des,[])
EHD_vector = np.concatenate((EHD_vector1,EHD_vector2,EHD_vector3,EHD_vector4,EHD_vector5))#,neighbor1,neighbor2,neighbor3,neighbor4,global_des
EHD_vector_list =list(EHD_vector)
print (EHD_vector_list)

EHD_matrix = EHD_vector.reshape(30,5)
print EHD_matrix


print "writing in text file"
text_file_vector = open("C:/Users/musi0010/Desktop/jobs/zedge_task/mirflickr/meta/features/EHD_vector.txt","w")
text_file_vector.write("1,")
delimitar_list =','.join(map(str,EHD_vector_list))
text_file_vector.write(delimitar_list)
text_file_vector.write("\n")
text_file_vector.close()

#np.savetxt('C:/Users/musi0010/Desktop/jobs/zedge_task/mirflickr/meta/features/EHD_vector.txt', EHD_vector_list, fmt ='%0.3f',)
#np.savetxt('C:/Users/musi0010/Desktop/jobs/zedge_task/mirflickr/meta/features/EHD_matrix.txt', EHD_matrix, fmt ='%0.3f')

#text_file_matrix = open("C:/Users/musi0010/Desktop/jobs/zedge_task/mirflickr/meta/features/EHD_matrix.txt","w")
#text_file_vector.write("1,  ")
#text_file_matrix.write("1  ")
#s1 =','.join(map(str,EHD_vector_list))
#text_file_vector.write(s1)
#text_file_vector.write("\n")
#text_file_matrix.write(EHD_matrix)
#text_file_matrix.write("\n")
#text_file_vector.close()