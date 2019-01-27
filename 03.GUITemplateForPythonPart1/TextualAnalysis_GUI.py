#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates a front-end GUI for AnalyseThis.py
@author: matta_idlecoder@protonmail.com
"""
from tkinter import Tk, Frame, StringVar, IntVar
from tkinter import NORMAL, DISABLED, RAISED, END
from tkinter import Button, Radiobutton, Checkbutton
from tkinter import Toplevel, Entry, Label
import tkinter.constants, tkinter.filedialog
import tkinter.messagebox
import os
 
from AnalyseThis import analyse_this
 
 
class PythonGUI(Frame):
    """The object space for creating your dashboard and launching your app
   """
    def __init__(self, root):
        """This is where you define & initialise all your GUI variables
        """
        Frame.__init__(self, root)
        self.master = root
 
        self.std_button_opts = {'wraplength':"6c", 'relief':RAISED, 'bd':4, 'pady':5}
 
 
        """ Define the default file options for opening files:
        """
        self.file_opt = {}
        self.file_opt['defaultextension'] = '.txt'
        self.file_opt['filetypes'] = [('text files', '.txt')]
        self.file_opt['initialdir'] = '.'
        self.file_opt['parent'] = root
 
        self.text_name = 'None chosen'
        self.text_path_and_name = None
        self.save_path_and_name = None
 
        self.dict_path_and_name = './EnglishDictionary.txt'
        self.textstatus = StringVar()
        self.textstatus.set('Choose a text file to analyse')
 
        self.dictstatus = StringVar()
        self.dictstatus.set('Change the dictionary')
 
        self.StartTrigButtonName = StringVar()
        self.StopTrigButtonName = StringVar()
        self.StartTriggerDisp = StringVar()
        self.StopTriggerDisp = StringVar()
 
        self.StartTrigger = StringVar()
        self.StopTrigger = StringVar()
 
        self.SortByAlpha = IntVar()
        self.ListContractions = IntVar()
        self.IgnoreAndListPropers = IntVar()
        self.SplitCompoundsAndList = IntVar()
        self.spellcheck = IntVar()
 
        self.SortByAlpha.set(1)
        self.ListContractions.set(1)
        self.IgnoreAndListPropers.set(1)
        self.SplitCompoundsAndList.set(1)
        self.spellcheck.set(1)
 
        self.reset_all_start_trigger_vars()
        self.reset_all_stop_trigger_vars()
 
        self.YourAppDashboard()
        return
 
 
    def YourAppDashboard(self):
        """The function that creates your dashboard and all its widgets
        """
        std_pos_opts = {'fill':tkinter.constants.BOTH, 'padx':10}
 
        BlankLine = ' ' * 80
 
        Button(self, textvariable=self.textstatus, font=('Helvetica', 16),
               command=self.GetNameOfTextToAnalyse,
               **self.std_button_opts).pack(pady=20, **std_pos_opts)
 
        Button(self, textvariable=self.StartTrigButtonName,
               command=self.GetStartTrig, **self.std_button_opts).pack(pady=5,
               **std_pos_opts)
 
        Button(self, textvariable=self.StopTrigButtonName,
               command=self.GetStopTrig, **self.std_button_opts).pack(pady=5,
               **std_pos_opts)
 
        Label(self, text=BlankLine).pack()
 
        Checkbutton(self, text="List proper nouns separately",
                    variable=self.IgnoreAndListPropers).pack(**std_pos_opts)
 
        Checkbutton(self, text='List contractions used',
                    variable=self.ListContractions).pack(**std_pos_opts)
 
        Checkbutton(self, text='List hyphenated compounds\nwords separately',
                    variable=self.SplitCompoundsAndList).pack(**std_pos_opts)
 
        Label(self, text=BlankLine).pack()
 
        Checkbutton(self, text='Do a spell check', variable=self.spellcheck,
                    command=self.onSpellCheck).pack(**std_pos_opts)
 
        self.SelectDictButton = Button(self, text=self.dictstatus,
               textvariable=self.dictstatus, command=self.GetNameOfDictToUse,
               state=NORMAL, **self.std_button_opts)
 
        self.SelectDictButton.pack(**std_pos_opts)
 
        Label(self, text=BlankLine).pack()
 
        Radiobutton(self, text='Sort word frequency analysis\nalphabetically by word',
                    variable=self.SortByAlpha, value=1).\
                    pack(**std_pos_opts)
 
        Radiobutton(self, text='Sort word frequency analysis\nby word frequencies',
                    variable=self.SortByAlpha, value=0).\
                    pack(**std_pos_opts)
 
        Button(self, text='Analyse', command=self.analyse_text, relief=RAISED,
               bd=4, padx=10, pady=5, font=('Helvetica', 16)).pack(padx=10, pady=10)
 
        Button(self, text='Quit', command=self.quit, relief=RAISED,
               bd=4, padx=10, pady=5, font=('Helvetica', 16)).pack(padx=5, pady=10)
        return
 
 
    def GetNameOfTextToAnalyse(self):
        """Returns a filename for your own code to open elsewhere
        """
        if self.text_path_and_name: # a text has been chosen before
            self.file_opt['initialdir'], old_text_name = os.path.split(self.text_path_and_name)
        else:
            old_text_name = self.text_name
            self.file_opt['initialdir'] = '.'
 
        OldTextFilePath = self.text_path_and_name
 
        self.file_opt['title'] = 'Choose a text file to analyse:'
        self.file_opt['initialfile'] = ''
 
        self.text_path_and_name = tkinter.filedialog.askopenfilename(**self.file_opt)
        if self.text_path_and_name:  # if it's not '':
            text_path, self.text_name = os.path.split(self.text_path_and_name)
            self.reset_all_start_trigger_vars()
            self.reset_all_stop_trigger_vars()
        else:
            self.text_path_and_name = OldTextFilePath
            self.text_name = old_text_name
 
        self.textstatus.set('TEXT: ' + self.text_name)
        return
 
 
    def save_as_file(self, result):
        """ Saves the result of your program to a file
        """
        if self.save_path_and_name:
            self.file_opt['initialdir'], save_name = os.path.split(self.save_path_and_name)
 
        OldSaveFilePath = self.save_path_and_name
 
        if "." in self.text_name:
            basename, suffix = self.text_name.split(".")
        else:
            basename = self.text_name
 
        self.file_opt['title'] = "Save results to:"
        self.file_opt['initialfile'] = basename + '.Analysis.txt'
 
        self.save_path_and_name = tkinter.filedialog.asksaveasfilename(**self.file_opt)
        if self.save_path_and_name:  # if it's not '':
            file = open(self.save_path_and_name, 'w')
            file.write(result)
            file.close
            self.file_opt['initialdir'], save_name = os.path.split(self.save_path_and_name)
        else:
            self.save_path_and_name = OldSaveFilePath
        return
 
 
    def GetNameOfDictToUse(self):
        """Called when the user wants to select another dictionary file to use
        """
        OldDictPath = self.dict_path_and_name
        self.file_opt['initialdir'], old_dict_name = os.path.split(OldDictPath)
 
        self.file_opt['title'] = 'Choose a dictionary to use:'
        self.file_opt['initialfile'] = ''
 
        self.dict_path_and_name = tkinter.filedialog.askopenfilename(**self.file_opt)
        if self.dict_path_and_name:
            dict_path, new_dict_name = os.path.split(self.dict_path_and_name)
        else:
            self.dict_path_and_name = OldDictPath
            new_dict_name = old_dict_name
 
        self.dictstatus.set('Dictionary chosen: ' + new_dict_name)
        return
 
 
    def GetStartTrig(self):
        """Opens Entry dialog box to paste start trigger text into
        """
        self.StartTrigWin = Toplevel(self)
        root.grab_release()
        self.StartTrigWin.grab_set()
 
        geom_string = "+{}+{}".format(w-120, h+90)
        self.StartTrigWin.geometry(geom_string)
 
        self.StartTrigWin.title('Set Your Start Trigger')
 
        Instruction = "\nCut and paste a suitable START text trigger from your "
        Instruction += "text file into the space below. Don't worry about "
        Instruction += "putting it in quotation marks. The analysis will only "
        Instruction += "begin AFTER this text string has been found. It need"
        Instruction += " not be long - or unique - but it must be the first "
        Instruction += "time it occurs in the text file, and identify the point "
        Instruction += "after which the actual literary work begins (after the"
        Instruction += " publisher's preamble, forewords, etc):"
 
        Label(self.StartTrigWin, text=Instruction, wraplength="11c").pack(pady=5)
 
        TriggerEntry = Entry(self.StartTrigWin, textvariable=self.StartTriggerDisp,
                             width=80, justify='center')
        TriggerEntry.pack(pady=5)
        TriggerEntry.focus_set()
        TriggerEntry.select_range(0, END)
 
        button_1_title = "START analysing my text file only after finding the "
        button_1_title += "above text trigger."
        Button(self.StartTrigWin, text=button_1_title,
               command=self.onStartButton1,
               **self.std_button_opts).pack(pady=5)
 
        button_2_title = "Don't worry about using a start trigger. Start "
        button_2_title += "analysing my text file from the BEGINNING."
        Button(self.StartTrigWin, text=button_2_title,
               command=self.onStartButton2,
               **self.std_button_opts).pack(pady=5)
        return
 
 
    def onStartButton1(self):
        """This is called when the user wants to save the pasted start trigger
        """
        if (self.StartTriggerDisp.get()[:3] == '===')  or \
            (len(self.StartTriggerDisp.get()) == 0):
            self.reset_all_start_trigger_vars()
        else:
            self.StartTrigger.set(self.StartTriggerDisp.get())
            self.StartTrigButtonName.set('START trigger is SET')
 
        self.StartTrigWin.destroy()
        return
 
 
    def onStartButton2(self):
        """Called when the user decides not to save the pasted start trigger
        """
        self.reset_all_start_trigger_vars()
        self.StartTrigWin.destroy()
        return
 
 
    def reset_all_start_trigger_vars(self):
        """Resets all variables related to the start triggers
        """
        self.StartTrigButtonName.set('No start trigger is set: analyse from the BEGINNING')
        self.StartTriggerDisp.set('=== COPY & PASTE YOUR START TRIGGER TEXT HERE ===')
        self.StartTrigger.set("")
        return
 
 
    def GetStopTrig(self):
        """Opens an Entry dialog box to paste the stop trigger text into
        """
        self.StopTrigWin = Toplevel(self)
        root.grab_release()
        self.StopTrigWin.grab_set()
 
        geom_string = "+{}+{}".format(w-120, h+150)
        self.StopTrigWin.geometry(geom_string)
 
        self.StopTrigWin.title('Set Your Stop Trigger')
 
        Instruction = "\nCut and paste a suitable STOP text trigger from your "
        Instruction += "text file into the space below. The analysis will stop "
        Instruction += "when this text is found. It need not be long, but it "
        Instruction += "must be the first time it occurs in the text file, and "
        Instruction += "identify the end of the actual literary work, before "
        Instruction += "the index, glossary, etc. It will not be part of the "
        Instruction += "analysis. Don't worry about putting it in quotation marks:"
 
        Label(self.StopTrigWin, text=Instruction, wraplength="11c").pack(pady=5)
 
        TriggerEntry = Entry(self.StopTrigWin,
                                  textvariable=self.StopTriggerDisp,
                                  width=80, justify='center')
        TriggerEntry.pack(pady=5)
        TriggerEntry.focus_set()
        TriggerEntry.select_range(0, END)
 
        button_1_title = "STOP analysing my text file when the the above STOP "
        button_1_title += "text trigger is found."
        Button(self.StopTrigWin, text=button_1_title,
               command=self.onStopButton1, **self.std_button_opts).pack(pady=5)
 
        button_2_title = "Don't worry about using a stop trigger. Analyse my"
        button_2_title += "text file all the way to the END."
        Button(self.StopTrigWin, text=button_2_title,
               command=self.onStopButton2,
               **self.std_button_opts).pack(pady=5)
        return
 
 
    def onStopButton1(self):
        """This is called when the user wants to save the pasted stop trigger
        """
        if (self.StopTriggerDisp.get()[:3] == '===') or \
            (len(self.StopTriggerDisp.get()) == 0):
            self.reset_all_stop_trigger_vars()
        else:
            self.StopTrigger.set(self.StopTriggerDisp.get())
            self.StopTrigButtonName.set('STOP trigger is SET')
 
        self.StopTrigWin.destroy()
        return
 
 
    def onStopButton2(self):
        """Called when the user decides not to save the pasted stop trigger
        """
        self.reset_all_stop_trigger_vars()
        self.StopTrigWin.destroy()
        return
 
 
    def reset_all_stop_trigger_vars(self):
        """Resets all variables related to the stop triggers
        """
        self.StopTrigButtonName.set('No stop trigger is set: analyse all the way to the END')
        self.StopTriggerDisp.set('=== COPY & PASTE YOUR STOP TRIGGER TEXT HERE ===')
        self.StopTrigger.set("")
        return
 
 
    def onSpellCheck(self):
        """Enables/disables dictionary selector button
        """
        if self.spellcheck.get():
            self.SelectDictButton.config(state=NORMAL)
        else:
            self.SelectDictButton.config(state=DISABLED)
        return
 
 
    def analyse_text(self):
        """A simple wrapper to pass your dashboard-set variables to your logic
        """
        result = ''
 
        if self.text_name == 'None chosen':
            tkinter.messagebox.showinfo(title='Error: no text file chosen.   ',
                message="Please choose a text to analyse.", icon='error')
 
        else:
            result = analyse_this(self.text_path_and_name,
                        self.dict_path_and_name,
                        SortByAlpha=self.SortByAlpha.get(),
                        StartTrigger=self.StartTrigger.get(),
                        StopTrigger=self.StopTrigger.get(),
                        CheckingSpelling=self.spellcheck.get(),
                        SplitAndListCompounds=self.SplitCompoundsAndList.get(),
                        IgnoreNListProperNouns=self.IgnoreAndListPropers.get(),
                        ListingContractions=self.ListContractions.get(),
                        ListingAdverbs=False,
                        ListingGerunds=False)
 
            self.save_as_file(result)
        return
 
 
if __name__=='__main__':
    root = Tk()
 
    HalfScreenWidth = int(root.winfo_screenwidth()/2)
    HalfScreenHeight = int(root.winfo_screenheight()/2)
 
    w = HalfScreenWidth - 200
    h = HalfScreenHeight - 350
    # Centre window:
    geom_string = "+{}+{}".format(w, h)
 
    root.geometry(geom_string)
    root.title('Dashboard')
    root.lift()
    PythonGUI(root).pack()
 
    root.mainloop()

