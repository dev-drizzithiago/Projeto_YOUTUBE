import wx

class Youtube_v4:
    def __init__(self):
        self.app = wx.App()
        self.janela_principal = wx.Frame(None, title='Youtube_V4', size=(400, 200))
        self.janela_principal.Show()

        self.app.MainLoop()


iniciando_obj = Youtube_v4()
