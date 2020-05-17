#! env python
# -*- coding: utf-8 -*-

import os
import sys
import wx
from MyProject1MyFrame1 import MyProject1MyFrame1

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyProject1MyFrame1(None)
    frame.Show(True)
    app.MainLoop()