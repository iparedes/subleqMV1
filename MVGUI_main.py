import wx
import gettext
from MVGUI import MVGUIFrame
from MV import MV

class MyFrame(MVGUIFrame):
    def __init__(self, *args, **kwds):
        MVGUIFrame.__init__(self,*args,**kwds)
        self.M=None


    def on_button_step(self, event):  # wxGlade: MVGUIFrame.<event_handler>
        self.M.step()
        self.RefreshInst()
        self.RefreshMem()
        event.Skip()



    def RefreshMem(self):
        self.list_ctrl_1.DeleteAllItems()
        i=0
        maxmem=len(self.M.mem)
        # Showing 3 columns
        remainder=maxmem % 3
        while (i<maxmem-remainder):
            item=[]
            item.append("{:02x}".format(i))
            memo=self.M.mem_get_raw(i)+" "+self.M.mem_get_raw(i+1)+" "+self.M.mem_get_raw(i+2)
            item.append(memo)
            vals="{:02x}".format(self.M.mem_get(i))+" "+"{:02x}".format(self.M.mem_get(i+1))+" "+"{:02x}".format(self.M.mem_get(i+2))
            item.append(vals)
            self.list_ctrl_1.Append(item)
            i+=3
        if (remainder>0):
            item=[]
            memo=""
            vals=""
            item.append("{:02x}".format(i))
            for j in range(0,remainder):
                vals+=self.M.mem_get_raw(i+j)+" "
                memo+="{:02x}".format(self.M.mem_get(i+j))+" "
            item.append(memo)
            item.append(vals)
            self.list_ctrl_1.Append(item)

    def RefreshInst(self):
        i=self.M.PC
        item="{:02x}".format(self.M.mem_get(i))+" "+"{:02x}".format(self.M.mem_get(i+1))+" "+"{:02x}".format(self.M.mem_get(i+2))
        self.text_ctrl_inst.ChangeValue(item)
        item="{:02x}".format(i)
        self.text_ctrl_addr.ChangeValue(item)



class MyApp(wx.App):

    def __init__(self, *args, **kwds):
        wx.App.__init__(self,*args,**kwds)
        self.M=None


    def SetM(self,M):
        self.frame.M=M
        self.frame.RefreshMem()
        self.frame.RefreshInst()


    def OnInit(self):
        self.frame=MyFrame(None, wx.ID_ANY,"")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__=="__main__":
    gettext.install("app") # replace with the appropriate catalog name


    J=MV()
    J.load(0,3,4,6)
    J.load(3,7,7,7)
    J.load(6,3,4,0)

    app = MyApp(0)
    app.SetM(J)
    app.MainLoop()
