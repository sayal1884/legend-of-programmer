from tkinter import*
from random import randrange
from math import sin,pi,cos,sqrt,asin
import random
import math,anime
import os,PIL,sqlite3
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
class dualGame():
    def __init__(self,canvas,width,height,posX=0):
       self.canvas,self.width,self.height=canvas,width,height
       self.ind,self.posX=30,posX
       self.selectQuest,self.radioVar,self.numQuestion=[],StringVar(),StringVar()
       self.radio,self.label,self.lab,self.allQuest=[],[],StringVar(),[]
       self.img,self.variable,self.quest,imageQuest=[],[],[],[]
       self.player1Move,self.player2Move=10,10
       self.count,self.scoreJ1,self.scoreJ2=0,0,0
       self.winner=None
       self.countRand,self.lionPassCoords,self.tablePowerUp=0,[],[]
       self.lionCoords=None
       self.playerFlag,self.number,self.displaceNum=True,0,0
       self.displaceFlag,self.obstacle,self.obsCoordsMonster=True,[],[(23,6)]
       self.obsCoordsLion=[(23,9),(23,12),(20,12)]
       self.obsTag=['monster','lion','water','chess','cup','fire','fly','exp']
       self.powerUp=['exp','exp','exp','exp','fly','fly','fly','fly']
       random.shuffle(self.powerUp)
       random.shuffle(self.powerUp)
       self.xnum,self.ynum=25,15
       self.pas=int(self.width/self.xnum)-int(self.width/self.xnum*0.15)
       self.monsterAlpha=[]
       self.pionImage,self.pionImg,self.pionPhoto=['games/acter/christal.png','games/acter/alice.png'],[],[]
       self.tableItem=['games/item/akom.png', 'games/item/garden tree (1).png', 'games/item/garden tree (2).png',
                       'games/item/Olivo.png', 'games/item/tropical palm.png']
       self.count,self.posx,self.posy=-self.pas*2,self.pas,-self.pas*2
       self.obsImage,self.obsImg,self.obsPhoto=['games/item/akom.png', 'games/acter/cup.png', 'games/acter/fire.png',
                                                     'games/acter/fly.png', 'games/acter/lion.png', 'games/acter/monstre.png',
                                                     'games/acter/water.png','games/acter/exp.png'],[],[]
       self.alphaImage,self.alphaImg,self.alphaPhoto=['games/acter/tigreGateAlpha.png','games/acter/lionGateAlpha.png'],[],[]
       self.table=["cytology","cardiology","gut","endocrinology","immunology",
           "pathology","enzymology","nervous","physiology","respiratory","genetic",
           "sensitiviy","locomotion","laboratory","urinar"]
       self.itemCoords=[(3,11),(8,10),(15,5),(17,12),(19,4),(11,5)]
       self.item=[]
       self.fond9=PIL.Image.open(self.tableItem[randrange(len(self.tableItem)-1)])
       self.xsize,self.ysize=self.fond9.size
       self.fond9=self.fond9.resize((int(self.height*0.2*(self.xsize/self.ysize)),int(self.height*0.2)),PIL.Image.LANCZOS)
       self.affiche9=ImageTk.PhotoImage(self.fond9)
       self.fond8=PIL.Image.open(random.choice(['games/ancient.png', 'games/desert.jpg', 'games/cascade.jpg', 'games/snk.jpg', 'games/japan.jpg', 'games/bord.jpg']))
       self.fond8=self.fond8.resize((int(self.width),int(self.height)),PIL.Image.LANCZOS)
       self.affiche8=ImageTk.PhotoImage(self.fond8)
       self.fond7=PIL.Image.open('games/bas.png')
       self.fond7=self.fond7.resize((int(self.width*0.3),int(self.height*0.3)),PIL.Image.LANCZOS)
       self.affiche7=ImageTk.PhotoImage(self.fond7)
       self.fond6=PIL.Image.open('games/acter/alice.png')
       self.fond6=self.fond6.resize((int(self.width*0.05),int(self.height*0.1)),PIL.Image.LANCZOS)
       self.affiche6=ImageTk.PhotoImage(self.fond6)
       self.fond5=PIL.Image.open('games/acter/christal.png')
       self.fond5=self.fond5.resize((int(self.width*0.05),int(self.height*0.1)),PIL.Image.LANCZOS)
       self.affiche5=ImageTk.PhotoImage(self.fond5)
       self.fond4=PIL.Image.open('games/acter/play.png')
       self.fond4=self.fond4.resize((int(self.width*0.05),int(self.height*0.1)),PIL.Image.LANCZOS)
       self.affiche4=ImageTk.PhotoImage(self.fond4)
       self.fond3=PIL.Image.open('games/acter/scarab.png')
       self.fond3=self.fond3.resize((int(self.width*0.15),int(self.height*0.05)),PIL.Image.LANCZOS)
       self.affiche3=ImageTk.PhotoImage(self.fond3)
       self.fond2=PIL.Image.open('games/acter/liline.png')
       self.xsize,self.ysize=self.fond2.size
       self.fond2=self.fond2.resize((int(self.height*2*(self.xsize/self.ysize)),int(self.height*2)),PIL.Image.LANCZOS)
       self.affiche2=ImageTk.PhotoImage(self.fond2)
       self.fond1=PIL.Image.open('games/acter/asuka.png')
       self.xsize,self.ysize=self.fond1.size
       self.fond1=self.fond1.resize((int(self.height*2*(self.xsize/self.ysize)),int(self.height*2)),PIL.Image.LANCZOS)
       self.affiche1=ImageTk.PhotoImage(self.fond1)
       self.fond0=PIL.Image.open('games/acter/cup1.png')
       self.affiche0=ImageTk.PhotoImage(self.fond0)
       for i in range(len(self.obsImage)):
           self.obsImg.append(PIL.Image.open(self.obsImage[i]))
           self.obsImg[i]=self.obsImg[i].resize((self.pas,self.pas),PIL.Image.LANCZOS)
           self.obsPhoto.append(ImageTk.PhotoImage(self.obsImg[i]))
       for i in range(len(self.alphaImage)):
           self.alphaImg.append(PIL.Image.open(self.alphaImage[i]))
           self.alphaImg[i]=self.alphaImg[i].resize((int(self.width*0.4),int(self.height*0.85)),PIL.Image.LANCZOS)
           self.alphaPhoto.append(ImageTk.PhotoImage(self.alphaImg[i]))
       for i in range(len(self.pionImage)):
           self.pionImg.append(PIL.Image.open(self.pionImage[i]))
           self.pionImg[i]=self.pionImg[i].resize((self.pas,self.pas),PIL.Image.LANCZOS)
           self.pionPhoto.append(ImageTk.PhotoImage(self.pionImg[i]))
       self.tableCube,self.tableWay,self.tablePower=[],[(1,4),(1,8),(2,4),(2,5),(2,6),(2,7),(2,8),(3,6),(4,6),(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
                                                        (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 6),(7, 12), (8, 12), (9, 12), (10, 12), (11, 12),
                                                        (12, 12), (13, 12), (14, 12),(7, 6), (8, 6), (9, 6),(6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3),
                                                        (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3),(9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)
                                                        ,(6, 1), (7, 1), (8, 1), (9, 1), (10, 1),(10, 9), (11, 9), (12, 9), (13, 9),(14, 7), (14, 8),
                                                        (14, 9),(14, 10), (14, 11),(10,2),(10, 7), (11, 7), (12, 7), (13, 7),(13, 4),(13, 5),(13, 6),(15, 9),
                                                        (16, 9),(17, 9),(17, 2), (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8),(18, 6), (19, 6), (20, 6),
                                                        (21, 6), (22, 6), (23, 6),(21, 2), (21, 3), (21, 4), (21, 5),(18, 2), (19, 2), (20, 2),
                                                        (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12),(20,13),(21,13),(22,13),(23,13),(-5,13),(12,-5),(13,20)], [(5,1),
                                                        (6,11),(9,9),(12,12),(13,5),(21,2),(17,8),(8,3)]
       self.tableRoyal=[(23,13),(23,12),(23,11),(23,10),(23,9),(23,8),(23,7),(23,6),(22,13),(21,13),(20,13),(19,13),(19,12),(19,11),(19,10),(19,9)]
       for i in range(self.ynum):
          for j in range(self.xnum):
             self.tableCube.append(self.canvas.create_rectangle(self.posx,self.posy,self.posx+self.pas,self.posy+self.pas,outline=""))
             self.posx+=self.pas
          self.posx,self.posy=-self.pas*2,self.posy+self.pas
       self.count,self.posx,self.posy=0,self.pas,self.pas
       #self.pion1=self.canvas.create_oval(self.posx*21,self.posy*6,self.posx*21+self.pas,(self.posy*6)+self.pas,fill='blue',stipple='@kunimitsu.xbm',outline="",tag='player1')
       #self.pion2=self.canvas.create_oval(self.posx*1,self.posy*8,self.posx+self.pas,(self.posy*8)+self.pas,fill="yellow",outline="",tag='player2')
       self.menu=Canvas(self.canvas,width=int(self.width*0.195),height=int(self.height*1.01),relief="ridge",bg='#5f5',bd=5)
       self.wind=self.canvas.create_window(int(self.width*0.9),int(self.height*0.285),window=self.menu)
       self.frame=Frame(self.canvas, width=int(self.width*0.190),height=int(self.height*0.46),relief="ridge",bg='#5f5',bd=5)
       self.frame1=Frame(self.menu,width=int(self.width*0.190),height=int(self.height*0.15),relief='raised',bd=5)
       self.frame2=Frame(self.menu,width=int(self.width*0.190),height=int(self.height*0.15),relief='raised',bd=5)
       self.tableRadio,self.tableVar=[],[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
       self.quests=Text(self.frame,font=("arial",12),width=int(self.width*0.190*0.13),height=int(self.height*0.46*0.028),relief='raised',bd=5)
       self.quests.grid(column=0,row=0)
       self.helpB = Button(self.menu, text = 'à propos....', command = self.helpPlay ,overrelief="sunken", fg = '#55ffaa', bg = '#111133')
       for i in range(4):
           self.tableRadio.append(Radiobutton(self.frame,variable=self.tableVar[1],relief="ridge",
                                          overrelief='sunken',bg='white',anchor='w'))
           self.tableRadio[i].grid(column=0,row=i+1,sticky='nswe')
       self.submit=Button(self.frame,text='valider',image=self.affiche3,overrelief="sunken")
       self.labPlayer1=Label(self.frame1,text="Joueur 1",image=self.affiche5)
       self.submitPlayer1=Button(self.frame1,text='jouer',command=self.player1,image=self.affiche4,overrelief="sunken")
       self.ScorePlayer1=Canvas(self.frame1,width=int(self.width*0.05),height=int(self.height*0.1),relief="ridge",bd=2)
       self.labPlayer1.grid(column=0,row=0,sticky='nswe')
       self.submitPlayer1.grid(column=1,row=0,sticky='nswe')
       self.ScorePlayer1.grid(column=2,row=0,sticky='nswe')
       self.labPlayer2=Label(self.frame2,text="Joueur 2",image=self.affiche6)
       self.submitPlayer2=Button(self.frame2,text='jouer',command=None,image=self.affiche4,overrelief="sunken")
       self.ScorePlayer2=Canvas(self.frame2,width=int(self.width*0.05),height=int(self.height*0.1),relief="ridge",bd=2)
       self.labPlayer2.grid(column=0,row=0,sticky='nswe')
       self.submitPlayer2.grid(column=1,row=0,sticky='nswe')
       self.ScorePlayer2.grid(column=2,row=0,sticky='nswe')
       self.screen=Canvas(self.menu,width=int(self.width*0.2),height=int(self.height*0.2),relief="ridge",bd=5)
       self.screenT=Canvas(self.canvas,width=int(self.width*0.4),height=int(self.height*0.4),relief="ridge",bd=5)
       self.screen.create_image(int(self.width*0.2*0.5),int(self.height*0.2*0.5),image=self.affiche7)
       self.screenT.create_image(int(self.width*0.4*0.5),int(self.height*0.4*0.5),image=self.affiche8)
       self.play1S=self.ScorePlayer1.create_text(int(self.width*0.05*0.5),int(self.height*0.08*0.5),text=self.tableVar[2].get())
       self.play2S=self.ScorePlayer2.create_text(int(self.width*0.05*0.5),int(self.height*0.08*0.5),text=self.tableVar[3].get())
       self.show=self.screen.create_text(int(self.width*0.2*0.5),int(self.height*0.2*0.5),text=self.tableVar[4].get())
       self.showT=self.screenT.create_text(int(self.width*0.395*0.5),int(self.height*0.395*0.5),text='Bienvenue sur le \n grand Défi de Python')
       self.screenT.itemconfig(self.showT, font=('papyrus',28,'bold', 'italic','underline'),fill='black', justify ='center')
       self.showT2=self.screenT.create_text(int(self.width*0.4*0.5),int(self.height*0.4*0.5),text='Bienvenue sur le \n grand Défi de Python')
       self.screenT.itemconfig(self.showT2, font=('papyrus',28,'bold', 'italic','underline'),fill='#ffff00', justify ='center')
       self.menu.grid_propagate(1)
       self.winner1Coords,self.winner2Coords,self.cupCoords,self.speed=[],[],90,[]
       self.submit.grid(column=0,row=6,pady=5)
       self.screen.pack(pady=5)
       self.frame1.pack(pady=2)
       self.frame2.pack(pady=2)
       self.helpB.pack(pady=2)
       self.canvas.focus_set()
       self.wayDraw()
       self.royalPath()
       self.monster()
       self.drawPion()
       self.drawPowerUp()
       self.window = self.canvas.create_window(self.width/2, self.height/2, window = self.screenT)
       self.canvas.after(5000, self.starter)
       self.canvas.bind('<Key>',self.displacePlayer1)
       self.loaderQuest()
    def helpPlay(self):
        with open('games/legend of programmer.txt', 'rb') as file:
            self.ins= file.read()
        self.ins = self.ins.decode('utf8')
        self.f = Frame(self.canvas,relief='ridge',bd=5, bg = '#111133')
        self.info=Text(self.f,font=("arial",12),width=int(self.width*0.190*0.4),height=int(self.height*0.46*0.05))
        self.canvas.itemconfig(self.window, window = self.f)
        self.scroll = Scrollbar(self.f, command = self.info.yview, orient ='vertical', highlightbackground = '#111133', bg = '#55ffaa')
        self.info.config(yscrollcommand= self.scroll.set, fg = '#55ffaa', bg = '#111133', font=('papyrus',12))
        self.quitB = Button(self.f, text = 'fermer', command = self.close,overrelief="sunken", bg = '#55ffaa', fg = '#111133')
        self.info.grid(column = 0, row = 0)
        self.quitB.grid(column = 0, row = 1)
        self.scroll.grid(column = 1, row = 0, rowspan = 2, sticky ='ns')
        self.info.insert('end', self.ins)
        self.info.config(state ='disabled')
        self.canvas.coords(self.window, self.width/2.5, self.height/2)
    def close(self):
        self.canvas.itemconfig(self.window, window = self.frame)
        self.canvas.coords(self.window, -500, -500)
    def victoryAnim(self):
        self.cupCoords=self.canvas.coords(self.cupWin)
        self.canvas.delete(self.window)
        if self.cupCoords[1]>self.height*0.5:
            self.canvas.coords(self.cupWin,self.cupCoords[0],self.cupCoords[1]-5)
        elif self.winner==True:
            self.winner2Coords=[self.width,self.height]
            self.winner1Coords=self.canvas.coords(self.winner1)
            if self.winner1Coords[0]<self.width*0.3:
                self.canvas.coords(self.winner1,self.winner1Coords[0]+5,self.winner1Coords[1])
        else:
            self.winner1Coords=[self.width,self.height]
            self.winner2Coords=self.canvas.coords(self.winner2)
            if self.winner2Coords[0]<self.width*0.4:
                self.canvas.coords(self.winner2,self.winner2Coords[0]+5,self.winner2Coords[1])
        if self.cupCoords[1]>self.height*0.5:
            self.canvas.after(25,self.victoryAnim)
        elif self.winner1Coords[0]<self.width*0.3 or self.winner2Coords[0]<self.width*0.4:
            self.canvas.after(25,self.victoryAnim)
        else:
            pass
            #anime.animatingRandom(self.canvas,self.canvas,int(self.width*0.2),int(self.height*0.99),'multiDark')
    def starter(self):
        self.tableVar[4].set('Joueur 1, Appuyez \n sur votre Bouton rouge \n pour Commencer')
        self.screen.itemconfig(self.show, font=('gabriola',15,'bold'),fill='Yellow',text=self.tableVar[4].get(), justify ='center')
        self.frame1.config(bg="blue")
        self.frame2.config(bg="gray")
        self.ScorePlayer2.config(bg="white")
        self.ScorePlayer1.config(bg="blue")
        self.canvas.itemconfig(self.window, window = self.frame)
        self.canvas.coords(self.window, -500, -500)
    def loaderQuest(self):
        self.eltClass=self.table[randrange(len(self.table))]
        self.dataImg=sqlite3.connect('games/queryData.db')
        self.cur=self.dataImg.cursor()
        self.cur.execute('''create table if not exists qcmData(category TEXT,question TEXT,response TEXT) ''')
        try:
            self.request="select * from qcmData where category='{}'".format('python')
            self.cur.execute(self.request)
            self.data=list(self.cur)
            for j in self.data:
                self.allQuest.append(j)
        except:
            print('___________ table not complete _________________')
        self.a,self.selected,self.b=0,[], 0
        while self.a<len(self.allQuest)-1:
            self.b=randrange(len(self.allQuest))
            if self.b not in self.selected:
                self.selectQuest.append(self.allQuest[self.b])
                self.selected.append(self.b)
            else:
                while self.b in self.selected:
                    self.b=randrange(len(self.allQuest))
                    if self.b not in self.selected:
                        break
                self.selectQuest.append(self.allQuest[self.b])
                self.selected.append(self.b)
            self.a+=1
        random.shuffle(self.selectQuest)
        for i in range(30):
            self.quest.append([])
            self.quest[i].append(self.selectQuest[i][1])
            self.quest[i].append([])
            for j in range(3):
                self.quest[i][1].append(self.selectQuest[randrange(len(self.selectQuest))][2])
            self.quest[i][1].append(self.selectQuest[i][2])
            random.shuffle(self.quest[i][1])
            self.quest[i].append(self.selectQuest[i][2])
        self.dataImg.commit()
        self.dataImg.close()
    def assign(self):
        self.quests.config(state="normal",bg="#ddd")
        self.quests.delete('0.0','end')
        self.quests.config(state="disabled",bg="#ddd")
        self.answerAffiche(self.number)
        self.canvas.coords(self.window, -500, -500)
        self.canvas.focus_set()
        for i in range(4):
            self.tableRadio[i].config(value='',text='')
        if self.number==29:
            self.number=0
        else:
            self.number+=1
        if self.playerFlag==True:
            self.submitPlayer2.config(command=self.player2)
            self.submit.config(command=lambda : None)
            self.frame2.config(bg="blue")
            self.frame1.config(bg="white")
            self.ScorePlayer1.config(bg="white")
            self.ScorePlayer2.config(bg="blue")
        else:
            self.submitPlayer1.config(command=self.player1)
            self.submit.config(command=lambda : None)
            self.frame1.config(bg="blue")
            self.frame2.config(bg="gray")
            self.ScorePlayer2.config(bg="white")
            self.ScorePlayer1.config(bg="blue")
        self.canvas.focus_set()
    def questSubmit1(self,num):
        self.num,self.first,self.second=num,0,0
        for i in range(4):
            if self.tableVar[1].get()==self.quest[self.num][1][i]:
                self.first=i
        for i in range(4):
            if self.quest[self.num][2]==self.quest[self.num][1][i]:
                self.second=i
        return (self.first,self.second)
    def answerAffiche(self,num):
        self.num,self.imgPhoto=num,[]
        self.countRand=0
        self.elt=self.questSubmit1(self.num)
        if self.elt[0]==self.elt[1]:
            if self.playerFlag==True:
                self.scoreJ1+=2
                self.tableVar[4].set('Correct')
                self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='yellow',text=self.tableVar[4].get())
                self.tableVar[2].set(self.scoreJ1)
                self.ScorePlayer1.itemconfig(self.play1S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[2].get())
                self.canvas.after(1500,self.randomer)
            else:
                self.tableVar[4].set('Correct')
                self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='yellow',text=self.tableVar[4].get())
                self.scoreJ2+=2
                self.tableVar[3].set(self.scoreJ2)
                self.ScorePlayer2.itemconfig(self.play2S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[3].get())
                self.canvas.after(1500,self.randomer)
        else:
            if self.playerFlag==True:
                self.tableVar[4].set('Incorrect')
                self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='red',text=self.tableVar[4].get())
                self.scoreJ1+=0
                self.tableVar[2].set(self.scoreJ1)
                self.ScorePlayer1.itemconfig(self.play1S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[2].get())
                self.displaceFlag=False
                self.player1Move=0
            else:
                self.tableVar[4].set('Incorrect')
                self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='red',text=self.tableVar[4].get())
                self.scoreJ2+=0
                self.tableVar[3].set(self.scoreJ2)
                self.ScorePlayer2.itemconfig(self.play2S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[3].get())
                self.displaceFlag=False
                self.player2Move=0
    def answerAffiche1(self,num):
        self.num,self.imgPhoto=num,[]
        self.countRand=0
        self.elt=self.questSubmit1(self.num)
        if self.elt[0]==self.elt[1]:
            self.scoreJ1+=2
            self.tableVar[4].set('Correct')
            self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='yellow',text=self.tableVar[4].get())
            self.tableVar[2].set(self.scoreJ1)
            self.ScorePlayer1.itemconfig(self.play1S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[2].get())
            self.canvas.coords(self.pion1,self.lionCoords)
            self.player1Move=0
            self.player2Move=0
        else:
            self.tableVar[4].set('Incorrect')
            self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='red',text=self.tableVar[4].get())
            self.scoreJ1+=0
            self.tableVar[2].set(self.scoreJ1)
            self.ScorePlayer1.itemconfig(self.play1S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[2].get())
            self.displaceFlag=False
            self.player1Move=0
    def answerAffiche2(self,num):
        self.num,self.imgPhoto=num,[]
        self.countRand=0
        self.elt=self.questSubmit1(self.num)
        if self.elt[0]==self.elt[1]:
            self.scoreJ1+=2
            self.tableVar[4].set('Correct')
            self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='yellow',text=self.tableVar[4].get())
            self.tableVar[2].set(self.scoreJ2)
            self.ScorePlayer2.itemconfig(self.play2S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[2].get())
            self.canvas.coords(self.pion2,self.lionCoords)
            self.player2Move=0
            self.player1Move=0
        else:
            self.tableVar[4].set('Incorrect')
            self.screen.itemconfig(self.show,font=('papyrus',30,'bold'),fill='red',text=self.tableVar[4].get())
            self.scoreJ2+=0
            self.tableVar[2].set(self.scoreJ2)
            self.ScorePlayer2.itemconfig(self.play2S,font=('gabriola',35,'bold'),fill='Yellow',text=self.tableVar[2].get())
            self.displaceFlag=False
            self.player2Move=0
    def assign1(self):
        self.quests.config(state="normal",bg="#ddd")
        self.quests.delete('0.0','end')
        self.quests.config(state="disabled",bg="#ddd")
        self.answerAffiche1(self.number)
        self.canvas.coords(self.window, -500, -500)
        for i in range(4):
            self.tableRadio[i].config(value='',text='')
        if self.number==29:
            self.number=0
        else:
            self.number+=1
        self.submitPlayer2.config(command=self.player2)
        self.submit.config(command=lambda : None)
        self.canvas.focus_set()
    def assign2(self):
        self.quests.config(state="normal",bg="#ddd")
        self.quests.delete('0.0','end')
        self.quests.config(state="disabled",bg="#ddd")
        self.answerAffiche2(self.number)
        self.canvas.coords(self.window, -500, -500)
        for i in range(4):
            self.tableRadio[i].config(value='',text='')
        if self.number==29:
            self.number=0
        else:
            self.number+=1
        self.submitPlayer1.config(command=self.player1)
        self.submit.config(command=lambda : None)
        self.canvas.focus_set()
    def submitActive(self):
        self.submit.config(command=self.assign)
    def submitActive1(self):
        self.submit.config(command=self.assign1)
    def submitActive2(self):
        self.submit.config(command=self.assign2)
    def randomer(self):
        self.displaceNum=randrange(1,7)
        self.player1Move=0
        self.player2Move=0
        self.tableVar[4].set(str(self.displaceNum))
        self.screen.itemconfig(self.show,font=('algerian',30,'bold'),fill='yellow',text=self.tableVar[4].get())
        if self.countRand<20:
            self.canvas.after(100,self.randomer)
            self.countRand+=1
    def player1(self):
        self.playerFlag=True
        self.displaceFlag=True
        self.canvas.coords(self.window, self.width/2, self.height/2)
        self.quests.config(state="normal",bg="#afa")
        self.quests.delete('0.0','end')
        self.quests.config(font=('arial',16),fg='blue')
        self.quests.insert('0.0',self.quest[self.count][0])
        for i in range(4):
            self.t = ''
            if len(self.quest[self.count][1][i]) >50:
                self.tt = list(self.quest[self.count][1][i])
                for j in range(len(self.tt)):
                    self.t = self.t + self.tt[j]
                    if j%50 ==0 and j!=0:
                        self.t = self.t + '\n'
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.t)
            else:
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.quest[self.count][1][i])
        self.quests.config(state="disabled")
        if self.count==29:
            self.count=0
        else:
            self.count+=1
        self.submitPlayer2.config(command=lambda : None)
        self.submitPlayer1.config(command=lambda : None)
        for i in range(4):
            self.tableRadio[i].config(command=self.submitActive)
    def player2(self):
        self.playerFlag=False
        self.displaceFlag=False
        self.canvas.coords(self.window, self.width/2, self.height/2)
        self.quests.config(state="normal",bg="#aaf")
        self.quests.config(font=('arial',16),fg='blue')
        self.quests.delete('0.0','end')
        self.quests.insert('0.0',self.quest[self.count][0])
        for i in range(4):
            self.t = ''
            if len(self.quest[self.count][1][i]) >50:
                self.tt = list(self.quest[self.count][1][i])
                for j in range(len(self.tt)):
                    self.t = self.t + self.tt[j]
                    if j%50 ==0 and j!=0:
                        self.t = self.t + '\n'
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.t)
            else:
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.quest[self.count][1][i])
        self.quests.config(state="disabled")
        if self.count==29:
            self.count=0
        else:
            self.count+=1
        self.submitPlayer1.config(command=lambda : None)
        self.submitPlayer2.config(command=lambda : None)
        for i in range(4):
            self.tableRadio[i].config(command=self.submitActive)
    def royalPath(self):
        for i in range(len(self.tableRoyal)):
          self.elt=self.canvas.find_closest(self.posx*self.tableRoyal[i][0],self.posy*self.tableRoyal[i][1])
          try:
              self.canvas.itemconfig(self.elt,fill='#fda',outline="black",tag='royal')
          except:
              pass
    def monster(self):
        for i in range(len(self.obsCoordsMonster)):
          self.obstacle.append(self.canvas.create_image(self.posx*self.obsCoordsMonster[i][0]-int(self.pas/2),self.posy*self.obsCoordsMonster[i][1]+int(self.pas/2),
                                                        image=self.obsPhoto[5],tag=self.obsTag[0]))
        for i in range(len(self.obsCoordsLion)):
          self.obstacle.append(self.canvas.create_image(self.posx*self.obsCoordsLion[i][0]-int(self.pas/2),self.posy*self.obsCoordsLion[i][1]+int(self.pas/2),
                                                        image=self.obsPhoto[4],tag=self.obsTag[1]))
          self.lionPassCoords.append(0)
    def tigerDraw(self):
        self.monsterAlpha.append(self.canvas.create_image(int(self.width*0.3),int(self.height*0.5),image=self.alphaPhoto[0]))
        self.canvas.after(1500,self.deleteMonster)
    def lionDraw1(self):
        self.monsterAlpha.append(self.canvas.create_image(int(self.width*0.6),int(self.height*0.5),image=self.alphaPhoto[1]))
        self.canvas.after(1500,self.deleteMonster)
        self.canvas.after(2000,self.passLion1)
    def lionDraw2(self):
        self.monsterAlpha.append(self.canvas.create_image(int(self.width*0.6),int(self.height*0.5),image=self.alphaPhoto[1]))
        self.canvas.after(1500,self.deleteMonster)
        self.canvas.after(2000,self.passLion2)
    def deleteMonster(self):
        for i in range(len(self.monsterAlpha)):
            self.canvas.delete(self.monsterAlpha[i])
    def passLion1(self):
        self.playerFlag=True
        self.displaceFlag=True
        self.canvas.coords(self.window, self.width/2, self.height/2)
        self.quests.config(state="normal",bg="#fcc")
        self.quests.delete('0.0','end')
        self.quests.insert('0.0',self.quest[self.count][0])
        for i in range(4):
            self.t = ''
            if len(self.quest[self.count][1][i]) >50:
                self.tt = list(self.quest[self.count][1][i])
                for j in range(len(self.tt)):
                    self.t = self.t + self.tt[j]
                    if j%50 ==0 and j!=0:
                        self.t = self.t + '\n'
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.t)
            else:
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.quest[self.count][1][i])
        self.quests.config(state="disabled")
        if self.count==29:
            self.count=0
        else:
            self.count+=1
        self.submitPlayer2.config(command=lambda : None)
        self.submitPlayer1.config(command=lambda : None)
        for i in range(4):
            self.tableRadio[i].config(command=self.submitActive1)
    def passLion2(self):
        self.playerFlag=False
        self.displaceFlag=False
        self.canvas.coords(self.window, self.width/2, self.height/2)
        self.quests.config(state="normal",bg="#fcc")
        self.quests.delete('0.0','end')
        self.quests.insert('0.0',self.quest[self.count][0])
        for i in range(4):
            self.t = ''
            if len(self.quest[self.count][1][i]) >50:
                self.tt = list(self.quest[self.count][1][i])
                for j in range(len(self.tt)):
                    self.t = self.t + self.tt[j]
                    if j%50 ==0 and j!=0:
                        self.t = self.t + '\n'
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.t)
            else:
                self.tableRadio[i].config(value=self.quest[self.count][1][i],text=self.quest[self.count][1][i])
        self.quests.config(state="disabled")
        if self.count==29:
            self.count=0
        else:
            self.count+=1
        self.submitPlayer2.config(command=lambda : None)
        self.submitPlayer1.config(command=lambda : None)
        for i in range(4):
            self.tableRadio[i].config(command=self.submitActive2)
    def wayDraw(self):
       for i in range(len(self.tableWay)):
          self.elt=self.canvas.find_closest(self.posx*self.tableWay[i][0],self.posy*self.tableWay[i][1])
          self.canvas.itemconfig(self.elt,fill='white',outline="black",tag='way', stipple='gray75')
       self.back=self.canvas.create_image(int(self.width/2),int(self.height/2),image=self.affiche8)
       self.cupWin=self.canvas.create_image(int(self.width*0.5),int(self.height*1.5),image=self.affiche0)
       self.winner1=self.canvas.create_image(int(self.width*(-0.3)),int(self.height),image=self.affiche1)
       self.winner2=self.canvas.create_image(int(self.width*(-0.3)),int(self.height),image=self.affiche2)
       self.canvas.tag_lower(self.back)
       for i in range(len(self.itemCoords)):
            self.item.append(self.canvas.create_image(self.posx*self.itemCoords[i][0]+int(self.pas/2),
                                                      self.posy*self.itemCoords[i][1]+int(self.pas/2),image=self.affiche9,tag='way'))
            self.canvas.tag_raise(self.item[i],self.back)
    def drawPion(self):
       self.pion1=self.canvas.create_image(self.posx*1+int(self.pas/2),self.posy*4+int(self.pas/2),image=self.pionPhoto[0],tag='player1')
       self.pion2=self.canvas.create_image(self.posx*1+int(self.pas/2),self.posy*8+int(self.pas/2),image=self.pionPhoto[1],tag='player2')
       self.cup=self.canvas.create_image(self.posx*19+int(self.pas/2),self.posy*9+int(self.pas/2),image=self.obsPhoto[1],tag='cup')
    def drawPowerUp(self):
        for i in range(len(self.powerUp)):
            if self.powerUp[i]=='exp':
                self.tablePowerUp.append(self.canvas.create_image(self.posx*self.tablePower[i][0]+int(self.pas/2),
                                                                  self.posy*self.tablePower[i][1]+int(self.pas/2),image=self.obsPhoto[-1],tag='exp'))
            else:
                self.tablePowerUp.append(self.canvas.create_image(self.posx*self.tablePower[i][0]+int(self.pas/2),
                                                                  self.posy*self.tablePower[i][1]+int(self.pas/2),image=self.obsPhoto[3],tag='fly'))
    def displacePlayer1(self,event):
       self.key=event.keysym
       if self.displaceFlag==True and self.player1Move<self.displaceNum:
           self.coordPlayer1=self.canvas.coords(self.pion1)
           self.touche=['z','q','s','d']
           self.midX,self.midY=0,0
           self.action=[(self.coordPlayer1[0],self.coordPlayer1[1]-self.pas),
                        (self.coordPlayer1[0]-self.pas,self.coordPlayer1[1]),
                        (self.coordPlayer1[0],self.coordPlayer1[1]+self.pas),
                        (self.coordPlayer1[0]+self.pas,self.coordPlayer1[1])]
           for i in range(len(self.touche)):
              if self.key==self.touche[i]:
                 self.midX,self.midY=int(self.action[i][0]),int(self.action[i][1])
           self.dir=[(self.coordPlayer1[0],self.coordPlayer1[1]-self.pas),(self.coordPlayer1[0]-self.pas,self.coordPlayer1[1]),
                     (self.coordPlayer1[0],self.coordPlayer1[1]+self.pas),(self.coordPlayer1[0]+self.pas,self.coordPlayer1[1])]
           for i in range(len(self.touche)):
              if self.key==self.touche[i]:
                 self.next=self.canvas.find_closest(self.dir[i][0],self.dir[i][1])
                 self.tag=self.canvas.itemcget(self.next,'tag')
                 self.firstag=self.tag.split(' ')[0]
                 if self.firstag=='way'  or self.firstag=='player2':
                    self.canvas.coords(self.pion1,self.action[i])
                 elif self.firstag=='exp':
                    self.rand=randrange(6,11,2)
                    self.canvas.coords(self.pion1,self.action[i])
                    self.canvas.delete(self.next)
                    self.tableVar[4].set('bravo Joueur 1 !\n vous avez obtenu \n {} points'.format(str(self.rand)))
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                    self.tableVar[2].set(self.scoreJ1+self.rand)
                    self.scoreJ1+=self.rand
                    self.ScorePlayer1.itemconfig(self.play1S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[2].get())
                 elif self.firstag=='cup':
                    self.canvas.coords(self.pion1,self.action[i])
                    self.canvas.delete(self.next)
                    self.tableVar[4].set('bravo Joueur 1 !\n vous avez gagné')
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                    self.winner=True
                    self.victoryAnim()
                 elif self.firstag=='fly':
                    self.rand=randrange(8,13,2)
                    self.canvas.coords(self.pion1,self.action[i])
                    self.canvas.delete(self.next)
                    self.tableVar[4].set('bravo Joueur 1 !\n vous avez obtenu \n {} mouvements'.format(str(self.rand)))
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                    self.displaceNum+=self.rand
                 elif self.firstag=='royal' or self.firstag=='monster' and self.scoreJ1>=32:
                    self.canvas.coords(self.pion1,self.action[i])
                 elif self.firstag=='royal' or self.firstag=='monster' and self.scoreJ1<32:
                    self.tigerDraw()
                    self.player1Move=self.displaceNum-1
                    self.tableVar[4].set('tigre : Il vous faut \n plus de 32 points pour \n entrer dans cette Zone')
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                 elif self.firstag=='lion':
                    self.player1Move=self.displaceNum
                    self.lionCoords=self.canvas.coords(self.next)
                    self.lionDraw1()
                    self.tableVar[4].set('Lion : Tenez vous tranquille \n et repondez-moi pour \n pouvoir continuer !')
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='red',text=self.tableVar[4].get())
           if self.player1Move==self.displaceNum-1:
               self.submitPlayer2.config(command=self.player2)
               self.submitPlayer1.config(command=lambda : None)
               self.displaceFlag=False
               self.displaceNum=0
           elif self.key in self.touche:
               self.player1Move+=1
       elif self.displaceFlag==False and self.player2Move<self.displaceNum:
           self.coordPlayer1=self.canvas.coords(self.pion2)
           self.touche=['Up','Left','Down','Right']
           self.action=[(self.coordPlayer1[0],self.coordPlayer1[1]-self.pas),
                        (self.coordPlayer1[0]-self.pas,self.coordPlayer1[1]),
                        (self.coordPlayer1[0],self.coordPlayer1[1]+self.pas),
                        (self.coordPlayer1[0]+self.pas,self.coordPlayer1[1])]
           for i in range(len(self.touche)):
              if self.key==self.touche[i]:
                 self.midX,self.midY=int(self.action[i][0]),int(self.action[i][1])
           self.dir=[(self.coordPlayer1[0],self.coordPlayer1[1]-self.pas),(self.coordPlayer1[0]-self.pas,self.coordPlayer1[1]),
                     (self.coordPlayer1[0],self.coordPlayer1[1]+self.pas),(self.coordPlayer1[0]+self.pas,self.coordPlayer1[1])]
           for i in range(len(self.touche)):
              if self.key==self.touche[i]:
                 self.next=self.canvas.find_closest(self.dir[i][0],self.dir[i][1])
                 self.tag=self.canvas.itemcget(self.next,'tag')
                 self.firstag=self.tag.split(' ')[0]
                 if self.firstag=='way' or self.firstag=='player1':
                    self.canvas.coords(self.pion2,self.action[i])
                 elif self.firstag=='royal' or self.firstag=='monster' and self.scoreJ2>=32:
                    self.canvas.coords(self.pion2,self.action[i])
                 elif self.firstag=='exp':
                    self.rand=randrange(6,11,2)
                    self.canvas.coords(self.pion2,self.action[i])
                    self.canvas.delete(self.next)
                    self.tableVar[4].set('bravo Joueur 2 !\n vous avez obtenu \n {} points'.format(str(self.rand)))
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                    self.tableVar[3].set(self.scoreJ2+self.rand)
                    self.scoreJ2+=self.rand
                    self.ScorePlayer2.itemconfig(self.play2S,font=('gabriola',35,'bold'),fill='green',text=self.tableVar[3].get())
                 elif self.firstag=='cup':
                    self.canvas.coords(self.pion2,self.action[i])
                    self.canvas.delete(self.next)
                    self.tableVar[4].set('bravo Joueur 2 !\n vous avez gagné')
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                    self.winner=False
                    self.victoryAnim()
                 elif self.firstag=='fly':
                    self.rand=randrange(8,13,2)
                    self.canvas.coords(self.pion2,self.action[i])
                    self.canvas.delete(self.next)
                    self.tableVar[4].set('bravo Joueur 2 !\n vous avez obtenu \n {} mouvements'.format(str(self.rand)))
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='yellow',text=self.tableVar[4].get())
                    self.displaceNum+=self.rand
                 elif self.firstag=='royal' or self.firstag=='monster' and self.scoreJ2<32:
                    self.tigerDraw()
                    self.player2Move=self.displaceNum-1
                    self.tableVar[4].set('tigre : Il vous faut \n plus de 32 points pour \n entrer dans cette Zone')
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='red',text=self.tableVar[4].get())
                 elif self.firstag=='lion':
                    self.player2Move=self.displaceNum
                    self.lionCoords=self.canvas.coords(self.next)
                    self.lionDraw2()
                    self.tableVar[4].set('Lion : Tenez vous tranquille \n et repondez-moi pour \n pouvoir continuer !')
                    self.screen.itemconfig(self.show,font=('gabriola',12,'bold'),fill='red',text=self.tableVar[4].get())
           if self.player2Move==self.displaceNum-1:
               self.submitPlayer1.config(command=self.player1)
               self.submitPlayer2.config(command=lambda : None)
               self.displaceNum=0
               self.displaceFlag=True
           elif self.key in self.touche:
               self.player2Move+=1
if __name__=='__main__':
    fen=Tk()
    fen['bg'] = '#111133'
    fen.title('legend of Programmer')
    fen.iconbitmap('games/legendProgrammer.ico')
    titre = Label(fen, text = 'Legend of programmer version 1.0', font = ('papyrus', 20, 'bold', 'italic'),bg ='#8f8', fg ='#448')
    titre.pack(side ='top', fill ='x', pady = 2)
    can=Canvas(fen,width=1000,height=500,bg='#115')
    dualGame(can,1000,500)
    can.pack(side='top', pady = 5)
    consigne = Label(fen, text = 'developper par Python Lite Fr, whatapps : +237694539239, Yaounde                (c) 2024', font = ('cambria', 14, 'bold', 'italic'),
                     bg ='#55ffaa', fg ='#111133')
    consigne.pack(side ='bottom', fill ='x', pady = 2)
    fen.mainloop()
