import ctypes
import glob
import sys
import random
from math import sqrt 
from collections import namedtuple
import time
import serial
import struct
try: 
    import Image
except ImportError:
    from PIL import Image


Point = namedtuple('Point', ('coords','n','ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

ser = serial.Serial("COM3", 115200, timeout = 1)

SPI_SETDESKWALLPAPER = 20
PATH = r'C:\Users\Shoaib\Desktop\Wallpaper'
ext = ['png', 'jpg']

def get_points(img):
    points= []
    w, h = img.size
    for count, color in img.getcolors(w*h):
        points.append(Point(color, 3, count))
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

def colorz(filename, n=3):
    img = Image.open(filename)
    img.thumbnail((200, 200))
    points = get_points(img)

    clusters = kmeans(points, n, 1)
    rgbs = [map(int, c.center.coords) for c in clusters]
    return map(rtoh, rgbs)

def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n) 
            new= Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break
    return clusters

def read_wallpaper():
    # read and store all wallpapers at once upon start of program
    files = []
    [files.extend(glob.glob(PATH+r'\*.'+ e)) for e in ext]
    return files

def getwallcolor(wallfiles, hexobj = []):
    # get the color of all the wallpapers are store
    for image in wallfiles:
        hexobj.append(colorz(image))
    return hexobj

def get_hexvalues(hexobjects, hexlist = []):
    for i in range(len(hexobjects)):
        for x in hexobjects[i]:
            hexlist.append(x)
    return hexlist

def setwallpaper(img):
    # set the wallpaper in order 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 1, img, 1)

def sendcolr(clrin32):
    # send 32 bit color to arduino 
    color1 = clrin32[0]
    color2 = clrin32[1]
    color3 = clrin32[2]

    #print ((str(color1) + ',' + str(color2) + ',' + str(color3)))
    text = (str(color1) + ',' + str(color2) + ',' + str(color3)+ '\n').encode()
    print(text)
    ser.write(text)

    #print(color1 + color2 + color3)
    

def get_clr32bit(rgbtuple):
    R = rgbtuple[0]
    G = rgbtuple[1]
    B = rgbtuple[2]
    clr32 = (R << 24) | (G << 16) | (B << 8)
    return clr32

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


imgfile = read_wallpaper()
hexobjlist = getwallcolor(imgfile)
hexclrlist = get_hexvalues(hexobjlist)

rgb = []

while True:
    clr_index = 0
    clr_chunks = chunks(hexclrlist, 3)
    for file in imgfile:
        clr_chunk = next(clr_chunks)
        for clr in clr_chunk:
            val = tuple(int(clr.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))                    
            color32bit = get_clr32bit(val)
            rgb.append(color32bit)
        sendcolr(rgb)
        setwallpaper(file)
        
        
        rgb.clear()
        time.sleep(3)