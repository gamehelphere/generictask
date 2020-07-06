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


class Frame_Tasklist(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame_Tasklist.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((859, 409))
        
        # Menu Bar
        self.frame_tasklist_menubar = wx.MenuBar()
        self.menuitem_action_attribute = wx.Menu()
        self.frame_tasklist_menubar.menuitem_addtask_attribute = self.menuitem_action_attribute.Append(wx.ID_ANY, "Add Task", "Add a task.")
        self.Bind(wx.EVT_MENU, self.menuitem_addtask_click, id=self.frame_tasklist_menubar.menuitem_addtask_attribute.GetId())
        self.frame_tasklist_menubar.menuitem_changetask_attribute = self.menuitem_action_attribute.Append(wx.ID_ANY, "Change Task", "Make a change in your highlighted task.")
        self.Bind(wx.EVT_MENU, self.menuitem_changetask_click, id=self.frame_tasklist_menubar.menuitem_changetask_attribute.GetId())
        self.frame_tasklist_menubar.menuitem_removetask_attribute = self.menuitem_action_attribute.Append(wx.ID_ANY, "Remove Task", "Remove a highlighted task. Do it after consideration!")
        self.Bind(wx.EVT_MENU, self.menuitem_removetask_click, id=self.frame_tasklist_menubar.menuitem_removetask_attribute.GetId())
        self.frame_tasklist_menubar.menuitem_exit_attribute = self.menuitem_action_attribute.Append(wx.ID_ANY, "Exit", "Exit and go back to main menu.")
        self.Bind(wx.EVT_MENU, self.menuitem_exit_click, id=self.frame_tasklist_menubar.menuitem_exit_attribute.GetId())
        self.frame_tasklist_menubar.Append(self.menuitem_action_attribute, "Actions")
        self.menuitem_help_attribute = wx.Menu()
        self.frame_tasklist_menubar.Append(self.menuitem_help_attribute, "Help")
        self.SetMenuBar(self.frame_tasklist_menubar)
        # Menu Bar end
        self.list_ctrl_tasks = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_SORT_ASCENDING | wx.LC_SORT_DESCENDING | wx.LC_VRULES)
        self.button_add = wx.Button(self, wx.ID_ANY, "Add Task")
        self.button_change = wx.Button(self, wx.ID_ANY, "Change Task")
        self.button_remove = wx.Button(self, wx.ID_ANY, "Remove Task")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.button_add_click, self.button_add)
        self.Bind(wx.EVT_BUTTON, self.button_change_task, self.button_change)
        self.Bind(wx.EVT_BUTTON, self.button_remove_task, self.button_remove)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Frame_Tasklist.__set_properties
        self.SetTitle("Task Management")
        self.Hide()
        self.list_ctrl_tasks.AppendColumn("Task ID", format=wx.LIST_FORMAT_LEFT, width=133)
        self.list_ctrl_tasks.AppendColumn("Task Description", format=wx.LIST_FORMAT_LEFT, width=582)
        self.list_ctrl_tasks.AppendColumn("Status", format=wx.LIST_FORMAT_LEFT, width=140)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame_Tasklist.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.list_ctrl_tasks, 5, wx.EXPAND, 0)
        sizer_4.Add(self.button_add, 1, wx.ALL, 10)
        sizer_4.Add(self.button_change, 1, wx.ALL, 10)
        sizer_4.Add(self.button_remove, 1, wx.ALL, 10)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        self.Centre()
        # end wxGlade

    def menuitem_action_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_action_click' not implemented!")
        event.Skip()

    def menuitem_addtask_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_addtask_click' not implemented!")
        event.Skip()

    def menuitem_changetask_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_changetask_click' not implemented!")
        event.Skip()

    def menuitem_removetask_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_removetask_click' not implemented!")
        event.Skip()

    def menuitem_exit_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_exit_click' not implemented!")
        event.Skip()

    def menuitem_help_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_help_click' not implemented!")
        event.Skip()

    def button_add_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'button_add_click' not implemented!")
        event.Skip()

    def button_change_task(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'button_change_task' not implemented!")
        event.Skip()

    def button_remove_task(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'button_remove_task' not implemented!")
        event.Skip()

# end of class Frame_Tasklist
