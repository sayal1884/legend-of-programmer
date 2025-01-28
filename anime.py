from random import randrange
from math import *
class animatingRandom():
    def __init__(self,fenetre,canvas,long,larg,color):
        self.longuer,self.largeur,self.fenetre=long,larg,fenetre
        self.color,self.chooseColor=color,[]
        self.num=int(self.longuer/2)
        self.canvas,self.speedTable,self.cube,self.startColor=canvas,[],[],[]
        self.counter,self.choice=[],['blue','red','green','yellow','purple','multi','multiDark']
        self.colorTable=[["#000","#001","#002","#003","#004","#005","#006","#007","#008","#009","#00a","#00b","#00c","#00d","#00e","#00f","#11f",
             "#22f","#33f","#44f","#55f","#66f","#77f","#88f"
             ,"#99f","#aaf","#bbf","#ccf","#ddf","#eef","#fff"],["#000","#100","#200","#300","#400","#500","#600","#700","#800","#900"
             ,"#a00","#b00","#c00","#d00","#e00","#f00","#f11","#f22","#f33","#f44","#f55","#f66","#f77","#f88"
             ,"#f99","#faa","#fbb","#fcc","#fdd","#fee","#fff"],["#000","#010","#020","#030","#040","#050","#060","#070","#080","#090"
             ,"#0a0","#0b0","#0c0","#0d0","#0e0","#0f0","#1f1","#2f2","#3f3","#4f4","#5f5","#6f6","#7f7","#8f8"
             ,"#9f9","#afa","#bfb","#cfc","#dfd","#efe","#fff"],["#000","#110","#220","#330","#440","#550","#660","#770","#880","#990"
             ,"#aa0","#bb0","#cc0","#dd0","#ee0","#ff0","#ff1","#ff2","#ff3","#ff4","#ff5","#ff6","#ff7","#ff8"
             ,"#ff9","#ffa","#ffb","#ffc","#ffd","#ffe","#fff"],["#000","#101","#202","#303","#404","#505","#606","#707","#808","#909"
             ,"#a0a","#b0b","#c0c","#d0d","#e0e","#f0f","#f1f","#f2f","#f3f","#f4f","#f5f","#f6f","#f7f","#f8f"
             ,"#f9f","#faf","#fbf","#fcf","#fdf","#fef","#fff"],["#f9f","#faf","#fbf","#fcf","#fdf","#fef","#fff","#ff9","#ffa","#ffb","#ffc","#ffd","#ffe","#fff",
            "#9f9","#afa","#bfb","#cfc","#dfd","#efe","#fff","#f99","#faa","#fbb","#fcc","#fdd","#fee","#fff"
             ,"#99f","#aaf","#bbf","#ccf","#ddf","#eef","#fff"],["#00f","#11f","#22f","#33f","#44f","#55f","#66f","#77f","#88f","#f00",
            "#f11","#f22","#f33","#f44","#f55","#f66","#f77","#f88","#f99","#0f0","#1f1","#2f2","#3f3","#4f4","#5f5","#6f6","#7f7","#8f8"
             ,"#9f9","#ff0","#ff1","#ff2","#ff3","#ff4","#ff5","#ff6","#ff7","#ff8","#ff9","#f0f","#f1f","#f2f","#f3f","#f4f","#f5f","#f6f","#f7f","#f8f"
             ,"#f9f"]]
        for i in range(len(self.choice)):
            if self.color==self.choice[i]:
                self.chooseColor=self.colorTable[i]
                break
            else:
                self.chooseColor=self.colorTable[0]
        self.cubeDraw()
        self.footFillAnime()
        self.footAnime()
    def cubeDraw(self):
        self.startx,self.starty=int(self.largeur*0.01),int(self.largeur*0.01)
        self.spacex,self.spacey=int(self.largeur*0.01),int(self.largeur*0.01)
        self.speedTable=[]
        for i in range(5):
            self.num=randrange(20,40)
            for j in range(self.num):
                self.o=randrange(2)
                if self.o==0:
                    self.cube.append(self.canvas.create_rectangle(self.spacex,self.spacey,self.startx+self.spacex,
                                                                  self.starty+self.spacey,fill="white",outline=""))
                else:
                    self.cube.append(self.canvas.create_oval(self.spacex,self.spacey,self.startx+self.spacex,
                                                             self.starty+self.spacey,fill="white",outline=""))
                self.spacex=self.startx+self.spacex+int(self.longuer*0.3)
                self.counter.append(randrange(30))
                self.speedTable.append(randrange(1,10))
            self.spacey=self.starty+self.spacey+int(self.largeur*0.03)
            self.spacex=int(self.largeur*0.002)
    def footFillAnime(self):
        self.filling=self.chooseColor
        for i in range(len(self.speedTable)):
            self.canvas.itemconfigure(self.cube[i],fill=self.filling[self.counter[i]])
            if self.counter[i]<len(self.filling):
                self.counter[i]+=1
            if self.counter[i]==int(len(self.filling)-1):
                self.counter[i]=0
        self.fenetre.after(1000,self.footFillAnime)
    def footAnime(self):
        try:
            for i in range(len(self.speedTable)):
                self.liste=self.canvas.coords(self.cube[i])
                self.num+=10
                if self.liste[1]>int(self.largeur):
                    self.canvas.coords(self.cube[i],self.liste[0],self.liste[1]-int(self.largeur),
                                       self.liste[0]+int(self.largeur*0.01),self.liste[3]-int(self.largeur))
                else:
                    self.canvas.coords(self.cube[i],self.liste[0]+int(math.sin(self.num)*10),
                                      self.liste[1]+self.speedTable[i],self.liste[2]+int(math.sin(self.num)*10),self.liste[3]+self.speedTable[i])
        except:
            pass
        self.fenetre.after(50,self.footAnime)
