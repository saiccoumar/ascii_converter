from convert_static import *
import time

testfile = "test/kitty.webp"

img = Image.open(testfile)
fa = 2.5
co=True
convfilt = 'sobel'

start = time.time()
convert_blackwhite(img,save=None,factor=fa)
end = time.time()
bnw_time = str(end-start)

start = time.time()
convert_grey(img,save=None,color=co,factor=fa)
end = time.time()
greyscale_time = str(end-start)

start = time.time()
convert_edge(img,cf=convfilt,save=None,factor=fa)
end = time.time()
edge_detection_time = str(end-start)

print("Black and White Execution Time:" + bnw_time)
print("Greyscale Execution Time:" + greyscale_time)
print("Edge Detection Execution Time:" + edge_detection_time)

