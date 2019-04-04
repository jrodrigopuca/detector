from ui05 import *
import sys
import cv2 
import numpy as np
import datetime
import matplotlib.pyplot as plt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # pass
    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.BtnInput.clicked.connect(self.pedirVideo)

    def cantFrames(self, video):
        # Traer cantidad manualmente
        cant=0
        success, frame = video.read()
        while success:
            cant+=1
            success, frame= video.read()
        return cant
    
    def detectar(self, metodo, imagen,seg):
        rgb= cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    
        # Capturo los puntos en donde posiblemente se encuentre la persona
        rects, weights = metodo.detectMultiScale(rgb,winStride=(16, 16),padding=(32, 32))

        # Dibujo rectángulo
        for i, (x, y, w, h) in enumerate(rects):
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),10)  
            fuente=cv2.FONT_HERSHEY_SIMPLEX
            peso=weights[i]
            if (weights[i] > 0):
                self.Lst.addItem(f'[INFO] Segundo {seg}: Encontró algo!')
            y2 = x - 15 if x - 15 > 15 else x + 15
            cv2.putText(imagen, str(peso), (h, y2), fuente, 0.75, (0, 255, 0),2)
        return imagen


    def pedirVideo(self):
        archivo, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Video", "","(*.mp4;)" )

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )

        if archivo:
            video= cv2.VideoCapture(archivo)
            fps=video.get(cv2.CAP_PROP_FPS)
            codec =0x00000021 #cv2.VideoWriter_fourcc(*'MPEG')
            size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            nuevoVideo= cv2.VideoWriter('resultado.mp4',codec,fps,size)

            i=0
            seg=0
            
            cantidad=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            print("cantidad", cantidad)

            success, frame = video.read()
            while success:
                i+=1
                print("frame",i)
                self.Bar.setValue(int(i*100/cantidad))
                if (i%fps==0):
                    seg+=1
                frame=self.detectar(hog, frame,seg)
                nuevoVideo.write(frame)
                success, frame= video.read()
            video.release()
            nuevoVideo.release()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()