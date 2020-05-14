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

ser = serial.Serial("COM3", 9600, timeout = 1)

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

def getwallcolor(wallfiles):
    # get the color of all the wallpapers are store
    clrlist = [] 
    for image in wallfiles:
        clrlist.append(colorz(image))
    return clrlist

def setwallpaper(img):
    # set the wallpaper in order 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 1, img, 1)

def sendclr(clrin32):
    # send 32 bit color to arduino 
    ser.write(clrin32)
    

def clr32bit(rgbtuple):
    R = rgbtuple[0]
    G = rgbtuple[1]
    B = rgbtuple[2]
    clr32 = (R << 24) | (G << 16) | (B << 8)
    return clr32

read_wallpaper()



  

