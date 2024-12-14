import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import(
    BLUR, CONTOUR, DETAIL,EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS,
    FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask
)

app= QApplication([])
win=QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")
lb_image=QLabel("Картинка")
btn_dir=QPushButton("Папка")
lw_files=QListWidget()
 
btn_left=QPushButton("Вліво")
btn_right=QPushButton("Вправо")
btn_flip=QPushButton("Відзеркалити")
btn_sharp=QPushButton("Різкість")
btn_bw=QPushButton("Ч/Б")
 
btn_blr=QPushButton("Розмиття")
btn_contur=QPushButton("Контур")
btn_detail=QPushButton("Деталізація")
btn_Edge=QPushButton("Зріз кутів")
btn_emb=QPushButton("EMBOS")
 
btn_find=QPushButton("Find edges")
btn_smooth=QPushButton("Smooth")
btn_smooth_plus=QPushButton("Smooth more")
btn_sharpen=QPushButton("Sharpen")
btn_gaus=QPushButton("GaussianBlur")
btn_unsh=QPushButton("UnsharpMask")

row=QHBoxLayout()
col1=QVBoxLayout()
col2=QVBoxLayout()
col1.addWidget(btn_dir) 
col1.addWidget(lw_files)
col2.addWidget(lb_image,95)

row_tools=QVBoxLayout()
row_tools1=QHBoxLayout()
row_tools2=QHBoxLayout()
row_tools3=QHBoxLayout()

row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_flip)
row_tools1.addWidget(btn_sharp)
row_tools1.addWidget(btn_bw)

row_tools2.addWidget(btn_blr)
row_tools2.addWidget(btn_contur)
row_tools2.addWidget(btn_detail)
row_tools2.addWidget(btn_Edge)
row_tools2.addWidget(btn_emb)

row_tools3.addWidget(btn_find)
row_tools3.addWidget(btn_smooth)
row_tools3.addWidget(btn_smooth_plus)
row_tools3.addWidget(btn_sharpen)
row_tools3.addWidget(btn_gaus)
row_tools3.addWidget(btn_unsh)

row_tools.addLayout(row_tools1)
row_tools.addLayout(row_tools2)
row_tools.addLayout(row_tools3)

col2.addLayout(row_tools)

row.addLayout(col1,20)
row.addLayout(col2,80)
 
win.setLayout(row)
win.show()
workdir = ''
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 
def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
 
def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
 
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)
 
btn_dir.clicked.connect(showFilenamesList)
 
class ImageProcessor():
    def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified/"
 
    def loadImage(self,filename):
       self.filename = filename
       fullname = os.path.join(workdir, filename)
       self.image = Image.open(fullname)
 
    def do_bw(self):
        self.image=self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
 
    def saveImage(self):
       path = os.path.join(workdir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       fullname = os.path.join(path, self.filename)
       self.image.save(fullname)
 
    def showImage(self, path):
       lb_image.hide()
       pixmapimage = QPixmap(path)
       w, h = lb_image.width(), lb_image.height()
       pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
       lb_image.setPixmap(pixmapimage)
       lb_image.show()
 
    def do_left(self):
        self.image=self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
 
    def do_right(self):
        self.image=self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
 
    def do_flip(self):
        self.image=self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
 
    def do_sharpen(self):
        self.image=self.image.filter(SHARPEN)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_blr(self):
        self.image=self.image.filter(BLUR)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_contur(self):
        self.image=self.image.filter(CONTOUR)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
    
    def detailed(self):
        self.image=self.image.filter(DETAIL)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_edge(self):
        self.image=self.image.filter(EDGE_ENHANCE)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
    
    def do_emb(self):
        self.image=self.image.filter(EMBOSS)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

    def find_edges(self):
        self.image=self.image.filter(FIND_EDGES)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_smooth(self):
        self.image=self.image.filter(SMOOTH)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
    
    def do_more_smooth(self):
        self.image=self.image.filter(SMOOTH_MORE)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_gaussianblur(self):
        self.image=self.image.filter(GaussianBlur)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)
    
    def do_unsharp(self):
        self.image=self.image.filter(UnsharpMask)
        self.saveImage()
        image_path=os.path.join(workdir,self.save_dir,self.filename)
        self.showImage(image_path)

def showChosenImage():
   if lw_files.currentRow() >= 0:
       filename = lw_files.currentItem().text()
       workimage.loadImage(filename)
       workimage.showImage(os.path.join(workdir, workimage.filename))
 
workimage=ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)

btn_left.clicked.connect(workimage.do_left) 
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)
btn_bw.clicked.connect(workimage.do_bw)
btn_sharp.clicked.connect(workimage.do_sharpen)

btn_blr.clicked.connect(workimage.do_blr)
btn_contur.clicked.connect(workimage.do_contur)
btn_detail.clicked.connect(workimage.detailed)
btn_Edge.clicked.connect(workimage.do_edge)

btn_emb.clicked.connect(workimage.do_emb)
btn_find.clicked.connect(workimage.find_edges)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_smooth_plus.clicked.connect(workimage.do_more_smooth)
btn_gaus.clicked.connect(workimage.do_gaussianblur)
btn_unsh.clicked.connect(workimage.do_unsharp)


all_buttons = [btn_dir,btn_left,btn_right,btn_flip,btn_sharp,btn_bw,btn_blr,btn_contur,btn_detail,btn_Edge,btn_emb,btn_find,btn_smooth,btn_smooth_plus,btn_sharpen,btn_gaus,btn_unsh
             
]
for i in all_buttons:
    i.setStyleSheet("""
    font-family: Arial Black;
    background-image: url(green.png);
    background-position: center;
    background-repeat: no-repeat;
    border:5px solid #70D19F;
    border-radius: 8px
    """)
    
win.setStyleSheet("""
background-image: url(back.jpg);
background-position: center;
background-repeat: no-repeat
""")

app.exec()
