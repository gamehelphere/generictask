# -*- coding: UTF-8 -*-
#
# Author: Ryan Baclit
# Email: gamehelphere@gmail.com
#
# generated by wxGlade 0.9.6 on Sun Jul  5 17:28:04 2020
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

from Dialog_Add_Edit_Task import Dialog_Add_Edit_Task

class Dialog_About(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialog_About.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.button_close = wx.Button(self, wx.ID_ANY, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.button_close_click, self.button_close)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dialog_About.__set_properties
        self.SetTitle("dialog")
        self.Hide()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialog_About.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        label_credits = wx.StaticText(self, wx.ID_ANY, "Written by Ryan Baclit.\n\nEmail: gamehelphere@gmail.com", style=wx.ALIGN_CENTER)
        sizer_2.Add(label_credits, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 36)
        sizer_2.Add(self.button_close, 18, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 12)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def button_close_click(self, event):  # wxGlade: Dialog_About.<event_handler>
        #print("Event handler 'button_close_click' not implemented!")
        #event.Skip()

        self.Close(True)

# end of class Dialog_About
