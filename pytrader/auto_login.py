from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/Kiwoom/KiwoomFlash2/khministarter.exe")

title = "번개 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('암호')

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('공인인증서암호')

btn_ctrl = dlg.Button0
btn_ctrl.Click()

while os.system("taskkill /im khmini.exe") is not 0:
    time.sleep(10)