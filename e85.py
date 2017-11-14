from itertools import count

def num_rects(w,h):
    return (w*(w+1)*h*(h+1))/4

def answer():
    for i in count(1):
        for j in count(i):
            n = num_rects(i,j)
            if n > 2000000:
                break
            if abs(n - 2000000) is 2:
                return i * j

if __name__ == '__main__':
    print answer()
