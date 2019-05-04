from detector import *

diy = Detector("../videos/tecnica.mp4")
#diy.detectarHOG("../result/resultadoHOG.mp4")
diy.detectarCSC("../result/resultadoCSC.mp4")
eventos = diy.traerEventos()
print(eventos)

