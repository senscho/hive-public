#!/usr/bin/env python3
"""Square face-crop avatar from cached official art.
usage: make_avatar.py <src.png> <out_dir> [size=512]
Writes <out_dir>/avatar.png (latest) + avatar-vN.png (never overwritten).
Face bbox: lbpcascade_animeface (OpenCV) if available, else heuristic:
top of the non-transparent bbox, horizontally centered on the opaque pixels of the top band."""
import sys,os,glob
from PIL import Image
import numpy as np
CASCADE='/workspace/<franchise>-assets/lbpcascade_animeface.xml'
def detect(img):
    try:
        import cv2
        if not os.path.exists(CASCADE): return None
        g=cv2.cvtColor(np.array(img.convert('RGB')),cv2.COLOR_RGB2GRAY); g=cv2.equalizeHist(g)
        m=max(48,min(img.size)//25)
        f=cv2.CascadeClassifier(CASCADE).detectMultiScale(g,1.1,5,minSize=(m,m))
        if len(f)==0: return None
        x,y,w,h=sorted(f,key=lambda r:(r[1],-r[2]))[0]  # topmost face
        return x,y,w,h
    except Exception: return None
def heuristic(img):
    a=np.array(img.split()[-1]) if img.mode=='RGBA' else np.full(img.size[::-1],255,np.uint8)
    ys,xs=np.where(a>16); top,bot=ys.min(),ys.max(); H=bot-top
    band=a[top:top+max(1,int(H*.08))]; bx=np.where(band.max(0)>16)[0]
    cx=int(bx.mean()) if len(bx) else img.width//2
    s=int(H*.11); return cx-s//2,top+int(H*.04),s,s
def main(src,out,size=512):
    img=Image.open(src).convert('RGBA'); r=detect(img); how='animeface'
    if r is None: r=heuristic(img); how='heuristic'
    x,y,w,h=map(int,r); cx,cy=x+w/2,y+h/2; s=int(max(w,h)*1.9)   # face + hair/shoulders margin
    top=max(0,int(cy-s*0.45)); box=(int(cx-s/2),top,int(cx+s/2),top+s)
    bg=Image.new('RGBA',img.size,(255,255,255,255)); bg.alpha_composite(img)
    crop=bg.crop(box).convert('RGB').resize((size,size),Image.LANCZOS)
    os.makedirs(out,exist_ok=True); n=len(glob.glob(f'{out}/avatar-v*.png'))+1
    crop.save(f'{out}/avatar-v{n}.png'); crop.save(f'{out}/avatar.png')
    print(f'{out}/avatar-v{n}.png',how,box)
if __name__=='__main__': main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 512)
