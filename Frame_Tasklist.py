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

"""

Must Do:

1. Save and load data from SQLite database. = No, I used a text file. Done!
2. Maybe a text file would be better because an SQL database might be too much for this app. = Yes!
3. I have to add a hidden or squished column in the ListCtrl for the dates. I think both
date created and date done must be added, but hidden.

"""

from Dialog_Add_Edit_Task import Dialog_Add_Edit_Task

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

        self.__init_custom()

    """
    Instead of putting too much extra code in the constructor, I made a method to call my own code.
    This will be called by the constructor.
    """

    def __init_custom(self):
        
        self.dialog_add_edit_task = Dialog_Add_Edit_Task(self)

    """
    Setter method to get an instance of Frame_Main. The Frame_Tasklist instance will use it to
    get back to the main frame, Frame_Main.
    """

    def set_Frame_Main(self, givenFrameMain):
        
        self.frame_main = givenFrameMain

    def __set_properties(self):
        # begin wxGlade: Frame_Tasklist.__set_properties
        self.SetTitle("Task Management")
        self.Hide()
        self.list_ctrl_tasks.AppendColumn("Task ID", format=wx.LIST_FORMAT_LEFT, width=1)
        self.list_ctrl_tasks.AppendColumn("Task Description", format=wx.LIST_FORMAT_LEFT, width=782)
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
        
        self.dialog_add_edit_task.set_operation("Add new task entry")
        self.dialog_add_edit_task.ShowModal()
        self.add_entry()

    def menuitem_changetask_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        
        self.dialog_add_edit_task.set_operation("Change task entry")
        self.dialog_add_edit_task.ShowModal()

    def menuitem_removetask_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_removetask_click' not implemented!")
        event.Skip()

    def menuitem_exit_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        #print("Event handler 'menuitem_exit_click' not implemented!")
        #event.Skip()

        self.frame_main.Show(True)
        self.Hide()

    def menuitem_help_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        print("Event handler 'menuitem_help_click' not implemented!")
        event.Skip()

    def button_add_click(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        
        self.dialog_add_edit_task.set_operation("Add new task entry")
        self.dialog_add_edit_task.ShowModal()
        self.add_entry()
        

    def button_change_task(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        
        self.dialog_add_edit_task.set_operation("Change task entry")
        self.dialog_add_edit_task.ShowModal()

    def button_remove_task(self, event):  # wxGlade: Frame_Tasklist.<event_handler>
        
        self.remove_task()


    """
    Main logic to remove a task. Putting it here will make the button_remove_task method cleaner.
    """

    def remove_task(self):
        
        focusedItem = self.list_ctrl_tasks.GetFocusedItem()
        print("Ang napili ay " + str(focusedItem))
        if(focusedItem != -1):
            if(self.list_ctrl_tasks.IsSelected(focusedItem)):
                print("Focused!")
                dialog_inform_remove = wx.MessageDialog(self, "Are you sure you want to remove this entry?", "Warning", wx.YES|wx.NO|wx.ICON_WARNING)
                result = dialog_inform_remove.ShowModal()   
                if result == wx.ID_YES:
                    
                    """
                    Finally remove selected entry. No turning back at this point!
                    """
                    
                    self.list_ctrl_tasks.DeleteItem(focusedItem)
                    
                    dialog_inform_remove_final = wx.MessageDialog(self, "Entry removed successfully.", "Information", wx.OK_DEFAULT|wx.ICON_INFORMATION)
                    dialog_inform_remove_final.ShowModal()   
                    dialog_inform_remove_final.Destroy()                     
                
                dialog_inform_remove.Destroy()
                 
            else:
                print("Non-focused.")
                print("Please select an item to remove.")
                dialog_inform_remove = wx.MessageDialog(self, "No entry selected to remove.", "Information", wx.OK|wx.CENTRE|wx.ICON_QUESTION)
                dialog_inform_remove.ShowModal()       
                dialog_inform_remove.Destroy()         
        else:
            print("Please select an item to remove.")
                        
            dialog_inform_remove = wx.MessageDialog(self, "No entry selected to remove.", "Information", wx.OK|wx.CENTRE|wx.ICON_QUESTION)
            dialog_inform_remove.ShowModal()
            
            """
            Dialog boxes must be removed from running memory to save system memory. It might not be
            useful for systems with lots of memory, but can be in older systems.
            """            
            
            dialog_inform_remove.Destory()        

    """
    The routine to add the data in the List widget. The code might become big later and putting
    them in a method will be wise.
    """

    def add_entry(self):
        
        """
        File operations underway! A flat or text file is enough for this application because an SQLite
        DB is too much.
        
        The algorithm to replace these lines is
        
        1. Retrieve all data from the ListCtrl and put it in a nested list.
        2. Add the new data from Dialog_Add_Edit_Task in the nested list.
        3. Overwrite the save file if existing or make one in the same directory.
        4. Save the contents of the nested list in the file.
        5. Clear the current contents of the ListCtrl.
        6. Load the text file and put the contents in the ListCtrl.
        
        It may appear that the algorithm is wasting cycles and a database would be better, but
        I still believe a flat file is enough for this small program. :)
        
        totalEntries = self.list_ctrl_tasks.GetItemCount() + 1
        if(totalEntries > 0):
            totalEntries = totalEntries - 1
        
        strTotalEntries = str(totalEntries)
        
        self.list_ctrl_tasks.InsertItem(totalEntries, strTotalEntries)
        
        # Put a row using SetItem() for the remaining columns.
        
        # For the task description.
        
        self.list_ctrl_tasks.SetItem(totalEntries, 1, self.dialog_add_edit_task.text_ctrl_taskdescription.GetLineText(0))
        
        # For the status.
        
        self.list_ctrl_tasks.SetItem(totalEntries, 2, "On-going.")
        
        """

        """
        New add entry algorithm with saving in a text file.
        """
        
        saveFile = open('generictask.savefile', 'w')
        
        """
        Save the existing entries in the ListCtrl.
        """

        for counter in range(self.list_ctrl_tasks.GetItemCount()):
            currentItem = self.list_ctrl_tasks.GetItem(counter, 1)
            taskDescription = currentItem.GetText()
            currentItem = self.list_ctrl_tasks.GetItem(counter, 2)
            status = currentItem.GetText()
            newEntry = '0{-9}' + taskDescription + '{-9}' + status + '\n'
            saveFile.write(newEntry)
            
        # Write the new entry in the file.
        
        taskDescription = self.dialog_add_edit_task.text_ctrl_taskdescription.GetLineText(0)
        status = 'On-going'
        newEntry = '0{-9}' + taskDescription + '{-9}' + status + '\n'
        saveFile.write(newEntry)
        saveFile.close()
        
        totalEntries = self.list_ctrl_tasks.GetItemCount()
        strTotalEntries = str(totalEntries)
        
        self.list_ctrl_tasks.InsertItem(totalEntries, strTotalEntries)
        
        # Put a row using SetItem() for the remaining columns.
        
        # For the task description.
        
        self.list_ctrl_tasks.SetItem(totalEntries, 1, taskDescription)
        
        # For the status.
        
        self.list_ctrl_tasks.SetItem(totalEntries, 2, "On-going")
        
# end of class Frame_Tasklist
