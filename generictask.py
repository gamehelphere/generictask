#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Author: Ryan Baclit
# Email: gamehelphere@gmail.com
#
# generated by wxGlade 0.9.6 on Sun Jul  5 17:28:04 2020
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
from Frame_Main import Frame_Main


class GenericTask(wx.App):
    def OnInit(self):
        self.frame_main = Frame_Main(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame_main)
        self.frame_main.Show()
        return True

# end of class GenericTask

if __name__ == "__main__":
    generictask = GenericTask(0)
    generictask.MainLoop()
