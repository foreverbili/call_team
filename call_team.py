# -*-coding:cp936-*-

import webbrowser
import os
import sys
from PyQt4 import QtGui,QtCore
import subprocess
import time
import re
reload(sys)

from PyQt4.QtWebKit import *  
from PyQt4.QtNetwork import *
from PyQt4.QtCore import *  
from PyQt4.QtGui import * 
sys.setdefaultencoding('cp936')





class Example(QtGui.QWidget):

    def __init__(self):
        super(Example,self).__init__()

        self.initUI()

    def initUI(self):

        
        self.resize(500,510)
        self.setWindowTitle(u'��������')
        self.center()

        #qbtn=QtGui.QPushButton(u'ծ��',self)
        #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #qbtn.resize(qbtn.sizeHint())
        
#       hbox = QtGui.QHBoxLayout()
#        hbox.addStretch(1)
#        hbox.addWidget(qbtn)

#        vbox = QtGui.QVBoxLayout()
#        vbox.addStretch(1)
#        vbox.addLayout(hbox)

#        self.setLayout(vbox)


        si=subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        eve1 = QtGui.QLabel(u'<font color=red><b>ٻŮ����</b></font> ', self)
        eve1.move(200, 135)
        eve1.setFont(QtGui.QFont("Roman times", 11))
        def Eve1():
           webbrowser.open_new_tab("http://km.netease.com/operation_site/content_widescreen?article_id=210045") 
        btn=QtGui.QPushButton(u'ٻŮ���κϷ�',self)
        btn.resize(btn.sizeHint())
        btn.move(20,165)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve1)
        def Eve2():
           webbrowser.open_new_tab("https://115.238.119.230/ywtools/showviewcode") 
        btn=QtGui.QPushButton(u'��������',self)
        btn.resize(btn.sizeHint())
        btn.move(140,165)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve2)
        def Eve3():
           webbrowser.open_new_tab("http://km.netease.com/operation_site/content_widescreen?article_id=231644")
        btn=QtGui.QPushButton(u'���������',self)
        btn.resize(btn.sizeHint())
        btn.move(260,165)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve3)
        def Eve4():
           webbrowser.open_new_tab("http://xqn.netease.com/forum-11-1.html")
        btn=QtGui.QPushButton(u'�ٷ�����',self)
        btn.resize(btn.sizeHint())
        btn.move(380,165)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve4)
        def Eve5():
           webbrowser.open_new_tab("http://its.og.163.gz/main/issue/view.do?id=2355966")
        btn=QtGui.QPushButton(u'�·��ռ�',self)
        btn.resize(btn.sizeHint())
        btn.move(20,195)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve5)
        def Eve6():
           webbrowser.open_new_tab("http://its.og.163.gz/main/issue/view.do?id=2240074")
        btn=QtGui.QPushButton(u'���鷴��',self)
        btn.resize(btn.sizeHint())
        btn.move(140,195)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve6)
        def Eve7():
           subprocess.Popen(r'"X:\h����\c���ù���\�����¹ⱦ��\Ghost_launcher.exe"')
        btn=QtGui.QPushButton(u'�¹ⱦ��',self)
        btn.resize(btn.sizeHint())
        btn.move(260,195)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve7)
        def Eve8():
           webbrowser.open_new_tab("http://xqn.163.com/news/2017/04/28/12347_685757.html")
        btn=QtGui.QPushButton(u'���ʹ�ʾ',self)
        btn.resize(btn.sizeHint())
        btn.move(380,195)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve8)
        def Eve9():
           subprocess.Popen(r'"X:\���оٱ�����4.0\jbgj3.0.exe"')
        btn=QtGui.QPushButton(u'�ٱ�����',self)
        btn.resize(btn.sizeHint())
        btn.move(20,225)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve9)
        def Eve10():
           subprocess.Popen(r'"X:\g�ռǱ�\һ��ͬ�������������.exe"')
        btn=QtGui.QPushButton(u'��Ϸ�����ռ�',self)
        btn.resize(btn.sizeHint())
        btn.move(140,225)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Eve10)
        
        
        eve2 = QtGui.QLabel(u'<font color=red><b>���й���</b></font> ', self)
        eve2.move(200, 10)
        eve2.setFont(QtGui.QFont("Roman times", 11))
        def Fve1():
           webbrowser.open_new_tab("http://ogoss.gameyw.netease.com/cs/login.jsp") 
        btn=QtGui.QPushButton(u'OGҳ��',self)
        btn.resize(btn.sizeHint())
        btn.move(20,40)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve1)
        def Fve2():
           webbrowser.open_new_tab("http://web.95163.call/") 
        btn=QtGui.QPushButton(u'����ҳ��',self)
        btn.resize(btn.sizeHint())
        btn.move(140,40)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve2)
        def Fve3():
           subprocess.Popen(r'"C:\Pidgin\pidgin.exe"')
        btn=QtGui.QPushButton(u'Pidgin',self)
        btn.resize(btn.sizeHint())
        btn.move(260,40)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve3)
        def Fve4():
           subprocess.Popen(r'"C:\Program Files (x86)\CounterPath\X-Lite\x-lite.exe"')
        btn=QtGui.QPushButton(u'X-Lite',self)
        btn.resize(btn.sizeHint())
        btn.move(380,40)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve4)
        def Fve5():
           os.system(r'"X:\h����\s����������Ϣ.xlsx"') 
        btn=QtGui.QPushButton(u'���ж���',self)
        btn.resize(btn.sizeHint())
        btn.move(20,70)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve5)
        def Fve6():
           webbrowser.open_new_tab("http://qc.gameyw.netease.com/hzdhzj/index.php") 
        btn=QtGui.QPushButton(u'�ʼ�ƽ̨',self)
        btn.resize(btn.sizeHint())
        btn.move(140,70)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve6)
        
        self.news=News()
        btn=QtGui.QPushButton(u'���о���',self)
        btn.setStyleSheet(" font-size:15px;color: rgb(225, 0, 0)")
        btn.resize(btn.sizeHint())
        btn.move(260,70)
        self.connect(btn, QtCore.SIGNAL("clicked()"), self.news.show)
        
        def Fve8():
           os.system(r'"X:\h����\J���ű����顱�ƻ�\���ű����顱�ڶ���.xlsx"')
        btn=QtGui.QPushButton(u'�ű�����',self)
        btn.resize(btn.sizeHint())
        btn.move(380,70)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve8)
        def Fve9():
           os.system(r'"X:\h����\J���ű����顱�ƻ�\���ò�Ʒ��ϵ��V2.xlsx"')
        btn=QtGui.QPushButton(u'������ϵ��',self)
        btn.resize(btn.sizeHint())
        btn.move(20,100)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Fve9)

        self.hello=Record()           
        btn=QtGui.QPushButton(u'���ɼ�¼',self)
        btn.resize(btn.sizeHint())
        btn.move(140,100)
        self.connect(btn, QtCore.SIGNAL("clicked()"), self.hello.show)

        self.hello1=Record1()           
        btn=QtGui.QPushButton(u'����¼��',self)
        btn.resize(btn.sizeHint())
        btn.move(260,100)
        self.connect(btn, QtCore.SIGNAL("clicked()"), self.hello1.show)




        eve3 = QtGui.QLabel(u'<font color=blue><b>ٻŮ����</b></font> ', self)
        eve3.move(200, 260)
        eve3.setFont(QtGui.QFont("Roman times", 11))
        def Gve1():
           webbrowser.open_new_tab("http://qnm.netease.com/thread-28544-1-1.html") 
        btn=QtGui.QPushButton(u'�Ϸ���ѯ',self)        
        btn.resize(btn.sizeHint())
        btn.move(20,290)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve1)
        def Gve2():
           webbrowser.open_new_tab("https://s3.cn-north-1.amazonaws.com.cn/l10-public/serverlists/online-with-date.html") 
        btn=QtGui.QPushButton(u'�������б�',self)
        btn.resize(btn.sizeHint())
        btn.move(140,290)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve2)
        def Gve3():
           webbrowser.open_new_tab("http://qnm.163.com/news/update/") 
        btn=QtGui.QPushButton(u'�ٷ�����',self)
        btn.resize(btn.sizeHint())
        btn.move(260,290)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve3)
        def Gve4():
           webbrowser.open_new_tab("http://mgdc.gameyw.netease.com/mcs/main.action")
        btn=QtGui.QPushButton(u'��������',self)
        btn.resize(btn.sizeHint())
        btn.move(380,290)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve4)
        def Gve5():
           subprocess.Popen(r'"X:\h����\c���ù���\Mobile_Launcher1.11�汾\mobile_launcher.exe"') 
        btn=QtGui.QPushButton(u'�����¹�',self)
        btn.resize(btn.sizeHint())
        btn.move(20,320)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve5)
        def Gve6():
           webbrowser.open_new_tab("http://qnm.netease.com/forum.php?mod=forumdisplay&fid=74&page=1")
        btn=QtGui.QPushButton(u'��ֵδ����',self)
        btn.resize(btn.sizeHint())
        btn.move(140,320)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve6)
        def Gve7():
           os.system(r'"X:\sy\sylc.xlsx"') 
        btn=QtGui.QPushButton(u'����������',self)
        btn.resize(btn.sizeHint())
        btn.move(260,320)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve7)
        def Gve8():
           subprocess.Popen(r'"E:\netease\qnsy.exe"') 
        btn=QtGui.QPushButton(u'ٻŮ����',self)
        btn.resize(btn.sizeHint())
        btn.move(380,320)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve8)        
        def Gve9():
           webbrowser.open_new_tab("https://qnm.netease.com/forum-87-1.html") 
        btn=QtGui.QPushButton(u'L10������',self)
        btn.resize(btn.sizeHint())
        btn.move(20,350)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve9)
        def Gve10():
           webbrowser.open_new_tab("http://qnm.163.com/news/update/2017/04/25/20682_685450.html") 
        btn=QtGui.QPushButton(u'���ʹ�ʾ',self)
        btn.resize(btn.sizeHint())
        btn.move(140,350)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve10)
        
        eve4 = QtGui.QLabel(u'<font color=blue><b>������Ϸ</b></font> ', self)
        eve4.move(200, 385)
        eve4.setFont(QtGui.QFont("Roman times", 11))
        def Gve1():
           webbrowser.open_new_tab("http://h35admin.x.netease.com:8892/serverinfo") 
        btn=QtGui.QPushButton(u'H35��������',self)
        btn.resize(btn.sizeHint())
        btn.move(20,415)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve1)
        def Gve2():
           webbrowser.open_new_tab("https://land.16163.com/forum-1653-1.html") 
        btn=QtGui.QPushButton(u'H35������',self)
        btn.resize(btn.sizeHint())
        btn.move(140,415)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve2)
        def Gve3():
           webbrowser.open_new_tab("http://land.163.com/2017/04/25/25294_685434.html") 
        btn=QtGui.QPushButton(u'H35����',self)
        btn.resize(btn.sizeHint())
        btn.move(260,415)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve3)
        def Gve4():
           webbrowser.open_new_tab("http://clx.16163.com/forum-1695-1.html") 
        btn=QtGui.QPushButton(u'�����㹫��',self)
        btn.resize(btn.sizeHint())
        btn.move(380,415)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve4)       
        def Gve5():
           os.system(r'"X:\h����\S����\c������\�������б�2018.1.xlsx"')  
        btn=QtGui.QPushButton(u'�����������',self)
        btn.resize(btn.sizeHint())
        btn.move(20,445)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve5)
        def Gve6():
           subprocess.Popen(r'"X:\h����\S����\c������\���������°�2018.1.exe"')  
        btn=QtGui.QPushButton(u'�����㹤��',self)
        btn.resize(btn.sizeHint())
        btn.move(140,445)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve6)
        def Gve7():
           webbrowser.open_new_tab("http://t2.16163.com/forum-1270-1.html") 
        btn=QtGui.QPushButton(u'�ս��߹���',self)
        btn.resize(btn.sizeHint())
        btn.move(260,445)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve7)    

        def Gve8():
           webbrowser.open_new_tab("http://t2.163.com/news/update/2018/01/24/23100_737354.html") 
        btn=QtGui.QPushButton(u'�ս��߼���',self)
        btn.resize(btn.sizeHint())
        btn.move(380,445)
        self.connect(btn, QtCore.SIGNAL("clicked()"), Gve8) 

        
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
#���Ͼ��ǹ�����������Ϳ��������Ĺ���


class Record(QtGui.QWidget):
     def __init__(self, parent = None):
          super( Record, self ).__init__(parent)
          self.setWindowTitle( u"��¼¼��" )
          self.resize( 250, 180 )
          gridlayout = QtGui.QGridLayout()
          Input = QtGui.QPushButton( u"��¼¼��" )
          Search = QtGui.QPushButton( u"�鿴��¼" )
          Quit = QtGui.QPushButton( u"�˳�" )

          gridlayout.addWidget( Input, 1, 0, 1, 2 )
          gridlayout.addWidget( Search, 2, 0, 1, 2 )
          gridlayout.addWidget( Quit, 3, 0, 1, 2 )
          self.setLayout( gridlayout )
        
          self.connect(Input,QtCore.SIGNAL("clicked()"),self.Input)
          self.connect(Search,QtCore.SIGNAL("clicked()"),self.Search)
          self.connect(Quit,QtCore.SIGNAL("clicked()"),self.Quit)

     def Input(self):
          InputW=In()
          I=InputW.exec_()
     def Quit(self):
          self.close()
     def Search(self):
          os.system(r'"X:\h����\c���ù���\a����¼��\����¼��.txt"')          

class In(QtGui.QDialog):
     def __init__(self):
                         super(In,self).__init__()
                         self.setWindowTitle(u"��¼��Ϣ")
                         self.resize( 200, 150 )
                         self.gridlayout=QtGui.QGridLayout()
                         self.gridlayout.setSpacing(10)

                         self.Id=QtGui.QLabel(u"������ţ�                                     ")       
                         self.Name=QtGui.QLabel(u"����������                                     ")



                         self.textId=QtGui.QLineEdit()
                         self.textPsw=QtGui.QLineEdit()
                         self.textName=QtGui.QLineEdit()


                         self.okButton=QtGui.QPushButton(u"����")
                         self.cancalButton=QtGui.QPushButton(u"�˳�")

                         self.gridlayout.addWidget( self.Id , 0, 0)
                         self.gridlayout.addWidget( self.textId , 1, 0)
                         self.gridlayout.addWidget( self.Name , 2, 0 )
                         self.gridlayout.addWidget( self.textName , 3, 0 , 1, 10)

                         self.gridlayout.addWidget( self.okButton , 4, 1 )
                         self.gridlayout.addWidget( self.cancalButton , 4, 2 )


                         self.connect( self.okButton, QtCore.SIGNAL( 'clicked()' ), self.OnOk )
                         self.connect( self.cancalButton, QtCore.SIGNAL( 'clicked()' ), self.OnCancel )

                         self.setLayout( self.gridlayout )


     def OnOk( self ):
                         a=self.textId.text()
                         c=self.textName.text()

        
                         with open(r'X:\h����\c���ù���\a����¼��\����¼��.txt',"r") as fp:

                             fp=open(r"X:\h����\c���ù���\a����¼��\����¼��.txt","a")
                             s=a+'  ,  '+c+'  ,  '+time.strftime("%Y/%m/%d")+'\n======================================================'+'\n'
                             fp.write(s)
                             fp.close()
                             QtGui.QMessageBox.about(self,u'About',u'��¼')
            
                         self.done( 1 )
     def OnCancel( self ):
                         self.done( 0 )

                        
class Record1(QtGui.QWidget):
     def __init__(self, parent = None):
          super( Record1, self ).__init__(parent)
          self.setWindowTitle( u"��¼¼��" )
          self.resize( 250, 180 )
          gridlayout = QtGui.QGridLayout()
          Input = QtGui.QPushButton( u"��¼¼��" )
          Search = QtGui.QPushButton( u"�鿴��¼" )
          Quit = QtGui.QPushButton( u"�˳�" )

          gridlayout.addWidget( Input, 1, 0, 1, 2 )
          gridlayout.addWidget( Search, 2, 0, 1, 2 )
          gridlayout.addWidget( Quit, 3, 0, 1, 2 )
          self.setLayout( gridlayout )
        
          self.connect(Input,QtCore.SIGNAL("clicked()"),self.Input)
          self.connect(Search,QtCore.SIGNAL("clicked()"),self.Search)
          self.connect(Quit,QtCore.SIGNAL("clicked()"),self.Quit)

     def Input(self):
          InputW=In1()
          I=InputW.exec_()
     def Quit(self):
          self.close()
     def Search(self):
          os.system(r'"X:\h����\c���ù���\a����¼��\����¼��.txt"')   


class In1(QtGui.QDialog):
     def __init__(self):
                         super(In1,self).__init__()
                         self.setWindowTitle(u"��¼��Ϣ")
                         self.resize( 200, 180 )
                         self.gridlayout=QtGui.QGridLayout()
                         self.gridlayout.setSpacing(10)

                         self.Id=QtGui.QLabel(u"������ţ�                                     ")
                         self.Psw=QtGui.QLabel(u"�ύ��Ա��                                     ")        
                         self.Name=QtGui.QLabel(u"����������                                     ")



                         self.textId=QtGui.QLineEdit()
                         self.textPsw=QtGui.QLineEdit()
                         self.textName=QtGui.QLineEdit()


                         self.okButton=QtGui.QPushButton(u"����")
                         self.cancalButton=QtGui.QPushButton(u"�˳�")

                         self.gridlayout.addWidget( self.Id , 0, 0)
                         self.gridlayout.addWidget( self.textId , 1, 0)
                         self.gridlayout.addWidget( self.Psw , 2, 0 )
                         self.gridlayout.addWidget( self.textPsw , 3, 0 )
                         self.gridlayout.addWidget( self.Name , 4, 0 )
                         self.gridlayout.addWidget( self.textName , 5, 0 , 1, 10)

                         self.gridlayout.addWidget( self.okButton , 6, 1 )
                         self.gridlayout.addWidget( self.cancalButton , 6, 2 )


                         self.connect( self.okButton, QtCore.SIGNAL( 'clicked()' ), self.OnOk )
                         self.connect( self.cancalButton, QtCore.SIGNAL( 'clicked()' ), self.OnCancel )

                         self.setLayout( self.gridlayout )


     def OnOk( self ):
                         a=self.textId.text()
                         b=self.textPsw.text()
                         c=self.textName.text()

        
                         with open(r'X:\h����\c���ù���\a����¼��\����¼��.txt',"r") as fp:

                             fp=open(r"X:\h����\c���ù���\a����¼��\����¼��.txt","a")
                             s=a+'  ,  '+b+'  ,  '+c+'  ,  '+time.strftime("%Y/%m/%d")+'\n======================================================'+'\n'
                             fp.write(s)
                             fp.close()
                             QtGui.QMessageBox.about(self,u'About',u'��¼')
            
                         self.done( 1 )
     def OnCancel( self ):
                         self.done( 0 )


class EmittingStream(QtCore.QObject):  
        textWritten = QtCore.pyqtSignal(str)  
        def write(self, text):  
            self.textWritten.emit(str(text)) 

class News(QtGui.QWidget):
     def __init__(self, parent = None):
          super( News, self ).__init__(parent)
          self.setWindowTitle( u"���о���" )
          self.resize(800, 500)
          gridlayout = QtGui.QGridLayout()            
          self.Input0 = QtGui.QPushButton( u"ٻŮ����" )
          self.Input1 = QtGui.QPushButton( u"ٻŮ����" )
          self.Input2 = QtGui.QPushButton( u"�ս���2" )
          self.Input3 = QtGui.QPushButton( u"������½" )
          self.Input4 = QtGui.QPushButton( u"����" )
          self.Input5 = QtGui.QPushButton( u"��ˮ��" )
          self.Input6 = QtGui.QPushButton( u"������" )
          self.Input7 = QtGui.QPushButton( u"������Ϸ" )
          self.Input8 = QtGui.QPushButton( u"�ʺ��ܱ�" )
          self.Input9 = QtGui.QPushButton( u"��������" )
          self.Search = QtGui.QPushButton( u"�鿴Ⱥ��(XXXX/XX/XX)" )
          self.Innote = QtGui.QPushButton( u"��¼Ⱥ��" )
          
          self.liEdit = QtGui.QLineEdit()
          self.txEdit = QtGui.QTextEdit()

          gridlayout.addWidget( self.liEdit, 0, 0,1,0  )
          gridlayout.addWidget( self.Input0, 1, 0  )
          gridlayout.addWidget( self.Input1, 1, 1 )
          gridlayout.addWidget( self.Input2, 1, 2 )
          gridlayout.addWidget( self.Input3, 1, 3 )
          gridlayout.addWidget( self.Input4, 1, 4 )
          gridlayout.addWidget( self.Input5, 2, 0 )
          gridlayout.addWidget( self.Input6, 2, 1 )
          gridlayout.addWidget( self.Input7, 2, 2 )
          gridlayout.addWidget( self.Input8, 2, 3 )
          gridlayout.addWidget( self.Input9, 2, 4 )
          
          gridlayout.addWidget( self.Search, 6,4 )
          gridlayout.addWidget( self.Innote, 6,0 )
          gridlayout.addWidget( self.txEdit, 4, 0 ,2,0)
          
          self.setLayout(gridlayout)
#�����￪ʼ¼��
          self.aa=Instr()
          self.connect(self.Innote, QtCore.SIGNAL("clicked()"), self.aa.show)
          
          self.connect(self.Search, QtCore.SIGNAL("clicked()"), self.reread)
          
          
          self.connect(self.Input0, QtCore.SIGNAL('clicked()'), self.aaButton)
          self.connect(self.Input1, QtCore.SIGNAL('clicked()'), self.bbButton)
          self.connect(self.Input2, QtCore.SIGNAL('clicked()'), self.ccButton)
          self.connect(self.Input3, QtCore.SIGNAL('clicked()'), self.ddButton)
          self.connect(self.Input4, QtCore.SIGNAL('clicked()'), self.eeButton)
          self.connect(self.Input5, QtCore.SIGNAL('clicked()'), self.ffButton)
          self.connect(self.Input6, QtCore.SIGNAL('clicked()'), self.ggButton)
          self.connect(self.Input7, QtCore.SIGNAL('clicked()'), self.hhButton)
          self.connect(self.Input8, QtCore.SIGNAL('clicked()'), self.iiButton)
          self.connect(self.Input9, QtCore.SIGNAL('clicked()'), self.jjButton)


          sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
          

          self.txEdit.clear()
          yestd=time.strftime('%Y/%m/%d', time.localtime(time.time()-86400))
          yystd=time.strftime('%Y/%m/%d', time.localtime(time.time()-172800))
          QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))

          print yystd+'Ⱥ����\n'
          tx1=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'ٻŮ����:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'ٻŮ����:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\�ս���2.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'�ս���2:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������½.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������½:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\����.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'����:'+'\n********************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\��ˮ��.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'��ˮ��:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������Ϸ.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������Ϸ:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\�ʺ��ܱ�.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'�ʺ��ܱ�:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()


          tx1=open(r'X:\h����\c���ù���\Ⱥ��\��������.txt')
          tx_1=tx1.read()
          pattern=re.compile(yystd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'��������:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()          


          print yestd+'Ⱥ����\n'
          tx1=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'ٻŮ����:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'ٻŮ����:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\�ս���2.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'�ս���2:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������½.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������½:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\����.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'����:'+'\n********************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\��ˮ��.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'��ˮ��:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������Ϸ.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������Ϸ:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\�ʺ��ܱ�.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'�ʺ��ܱ�:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()


          tx1=open(r'X:\h����\c���ù���\Ⱥ��\��������.txt')
          tx_1=tx1.read()
          pattern=re.compile(yestd+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'��������:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(255,0,0); QTextEdit {color:green}")          
          
#�����ǰ����ڲ�ѯ����
     def reread(self):
          QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
          self.txEdit.clear()
          
          tim = str(self.liEdit.text())
          print tim+'\n'
          tx1=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'ٻŮ����:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()
          

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'ٻŮ����:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\�ս���2.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'�ս���2:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������½.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������½:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\����.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'����:'+'\n********************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\��ˮ��.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'��ˮ��:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\������Ϸ.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'������Ϸ:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\�ʺ��ܱ�.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'�ʺ��ܱ�:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close()

          tx1=open(r'X:\h����\c���ù���\Ⱥ��\��������.txt')
          tx_1=tx1.read()
          pattern=re.compile(tim+'~��\n([\s\S]*?)\n---------------')
          ltx1=pattern.findall(tx_1)
          if ltx1:
              print u'��������:'+'\n*******************'
              for i in ltx1:
                  print i+'\n'+'---------------------------------------------------'
              print ' '
          tx1.close() 
                  





#��������������     
     def aaButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt') 
         all_tx=data.read()

         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
             if keywords in i:
                 print i+'\n'+'---------------------------------------------------'
                 self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
                 
                 
         data.close()
         
     def bbButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def ccButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\�ս���2.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()


     def ddButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\������½.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def eeButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\����.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def ffButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\��ˮ��.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def ggButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\������.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def hhButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\������Ϸ.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def iiButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\�ʺ��ܱ�.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

     def jjButton(self):
         self.txEdit.clear()
         keywords = str(self.liEdit.text())
         QTextCodec.setCodecForCStrings(QTextCodec.codecForName("cp936"))
         data=open(r'X:\h����\c���ù���\Ⱥ��\��������.txt') 
         all_tx=data.read()
         
         pattern1=re.compile('~~([\s\S]*?)\n-------')
         pattern2=re.compile('.*'+keywords+'.*')
         alltext=pattern1.findall(all_tx)

         for i in alltext:
                 if pattern2.findall(i):
                     print i+'\n'+'---------------------------------------------------'
                     self.txEdit.setStyleSheet("font-family:Microsoft YaHei;font-size:18px;color: rgb(0,0,139)")
         data.close()

         

     def __del__(self):  
         sys.stdout = sys.__stdout__ 

     def normalOutputWritten(self, text):  
         cursor = self.txEdit.textCursor()  
         cursor.movePosition(QtGui.QTextCursor.End)  
         cursor.insertText(text)  
         self.txEdit.setTextCursor(cursor)  
         self.txEdit.ensureCursorVisible()         


#�������Ⱥ����¼����          
class Instr(QtGui.QWidget):
     def __init__(self, parent = None):
          super( Instr, self ).__init__(parent)
          self.setWindowTitle( u"Ⱥ����¼" )
          self.resize( 500, 300 )
          gridlayout = QtGui.QGridLayout()

          self.sEdit = QtGui.QTextEdit()
          Input0 = QtGui.QPushButton( u"ٻŮ����" )
          Input1 = QtGui.QPushButton( u"ٻŮ����" )
          Input2 = QtGui.QPushButton( u"�ս���2" )
          Input3 = QtGui.QPushButton( u"������½" )
          Input4 = QtGui.QPushButton( u"����" )
          Input5 = QtGui.QPushButton( u"��ˮ��" )
          Input6 = QtGui.QPushButton( u"������" )
          Input7 = QtGui.QPushButton( u"������Ϸ" )
          Input8 = QtGui.QPushButton( u"�ʺ��ܱ�" )
          Input9 = QtGui.QPushButton( u"��������" )
          

          gridlayout.addWidget( self.sEdit, 0, 0,1,0 )
          gridlayout.addWidget( Input0, 1, 0  )
          gridlayout.addWidget( Input1, 1, 1 )
          gridlayout.addWidget( Input2, 1, 2 )
          gridlayout.addWidget( Input3, 1, 3 )
          gridlayout.addWidget( Input4, 1, 4 )
          gridlayout.addWidget( Input5, 2, 0 )
          gridlayout.addWidget( Input6, 2, 1 )
          gridlayout.addWidget( Input7, 2, 2 )
          gridlayout.addWidget( Input8, 2, 3 )
          gridlayout.addWidget( Input9, 2, 4 )

          self.setLayout( gridlayout )

          
          self.connect(Input0, QtCore.SIGNAL("clicked()"), self.Save1)
          self.connect(Input1, QtCore.SIGNAL("clicked()"), self.Save2)          
          self.connect(Input2, QtCore.SIGNAL("clicked()"), self.Save3)
          self.connect(Input3, QtCore.SIGNAL("clicked()"), self.Save4)
          self.connect(Input4, QtCore.SIGNAL("clicked()"), self.Save5)
          self.connect(Input5, QtCore.SIGNAL("clicked()"), self.Save6)
          self.connect(Input6, QtCore.SIGNAL("clicked()"), self.Save7)
          self.connect(Input7, QtCore.SIGNAL("clicked()"), self.Save8)
          self.connect(Input8, QtCore.SIGNAL("clicked()"), self.Save9)
          self.connect(Input9, QtCore.SIGNAL("clicked()"), self.Save10)




     def Save1(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
          
          self.sEdit.clear()  
          


     def Save2(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\ٻŮ����.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')

          self.sEdit.clear() 



     def Save3(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\�ս���2.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear() 


          
     def Save4(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\������½.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear() 


     def Save5(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\����.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear() 


          
     def Save6(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\��ˮ��.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear()

          
     def Save7(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\������.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear()

          
     def Save8(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\������Ϸ.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear() 


     def Save9(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\�ʺ��ܱ�.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
                 
          
     def Save10(self):
          a=self.sEdit.toPlainText()
          with open(r'X:\h����\c���ù���\Ⱥ��\��������.txt',"a") as fps:
                 b=a.split('\n***\n')
                 for i in b:
                     q='~~'+time.strftime("%Y/%m/%d")+u'~��\n'+i+'\n'+'--------------------------------------'+'\n'
                     fps.write(q)
                 fps.close()
                 QtGui.QMessageBox.about(self,u'About',u'��¼')
            
          self.sEdit.clear()


            
          self.sEdit.clear()





          

def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
    
