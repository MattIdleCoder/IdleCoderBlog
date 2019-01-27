#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This GUI program will present the user with a simple front end dashboard for
the Python command line program Markov.py to select the files it will use to 
build its Markov word chains. It will also ask the user to define the order of 
the Markov chains to use, and the size of the output paragraph to create, 
saving the results in a file name of the user's choice.
 
@author: matta_idlecoder@protonmail.com
"""
from tkinter import Tk, Frame, StringVar, IntVar
from tkinter import RAISED, END, E, W, CENTER, LEFT, RIGHT
from tkinter import Button, NORMAL, DISABLED
from tkinter import Toplevel, Entry, Label
import tkinter.constants, tkinter.filedialog
import tkinter.messagebox, tkinter.font
import os
import platform
 
from Markov import create_markov_text_from
 
 
def Cardinal(integer):
    """Converts an integer from 1-4 into a cardinal text string
    """
    if integer == 1:
        return 'one'
    elif integer == 2:
        return 'two'
    elif integer == 3:
        return 'three'
    elif integer == 4:
        return 'four'
    elif integer == 5:
        return 'five'
    elif integer == 6:
        return 'six'
    elif integer >= 7:
        return str(integer)
 
 
class PythonGUI_2(Frame):
    """The object space for creating your dashboard and launching your app
    """
    def __init__(self, root):
        """This is where you define & initialise all your GUI variables
        """
        Frame.__init__(self, root)
        self.master = root
 
        self.NormalFont = ('Helvetica', 14)
        self.FancyFont = ('Caladea', 15)
 
        self.std_button_opts = {'wraplength':"6c", 'relief':RAISED, 'bd':4,
                                'padx':10, 'pady':10}
 
        self.file_opt = {}
        self.file_opt['defaultextension'] = '.txt'
        self.file_opt['filetypes'] = [('text files', '.txt')]
        self.file_opt['initialdir'] = '.'
        self.file_opt['parent'] = root
 
        self.save_path_and_name = None
        self.path_list = []
 
        self.fileSelector = StringVar()
        self.FileCountButton = StringVar()
        self.fileSelector.set('Select files')
        self.FileCountButton.set('No files selected')
 
        self.FirstWordsButtonName = StringVar()
        self.FirstWordsDisp = StringVar()
        self.FirstWordsString = StringVar()
 
        self.OrderButtonName = StringVar()
        self.ParaLenButtonName = StringVar()
 
        self.MarkovOrder = IntVar()
        self.ParaLength = IntVar()
 
        self.MarkovOrder.set(2)
        self.ParaLength.set(200)
 
        self.OrderButtonName.set('Markov Order will be {:d}'.format(self.MarkovOrder.get()))
        self.ParaLenButtonName.set('Paragraph:{} words long'.format(self.ParaLength.get()))
 
        self.reset_first_words()
 
        self.YourAppDashboard()
        return
 
 
    def YourAppDashboard(self):
        """The function that creates your dashboard and all its widgets
        """
 
        std_pack_opts = {'padx':10, 'pady':10}
 
        BlankLine = ' ' * 80
 
        Label(self, text="\nMarkov Random Text Generator", font=('MS Gothic', 
                                                                 16)).pack()
        Label(self, text=BlankLine).pack()
 
        self.ListFilesButton = Button(self, textvariable=self.FileCountButton,
                                font=self.NormalFont, command=self.ListFiles,
                                state=DISABLED, **self.std_button_opts)
        self.ListFilesButton.pack(**std_pack_opts)
 
        Button(self, textvariable=self.fileSelector, command=self.GetFileList,
                               font=self.FancyFont,
                               **self.std_button_opts).pack(**std_pack_opts)
 
        Label(self, text=BlankLine).pack()
 
        Button(self, textvariable=self.FirstWordsButtonName,
                                command=self.GetFirstWords,
                                font=self.NormalFont,
                                **self.std_button_opts).pack(**std_pack_opts)
 
        self.OrderButton = Button(self, textvariable=self.OrderButtonName,
                                cursor='plus', font=self.NormalFont,
                                command=lambda:
                                self.UpdateNumberButton(Parent='self',
                                Variable='self.MarkovOrder',
                                ButtonName='self.OrderButtonName',
                                Font=self.NormalFont,
                                ButtonFormat='.set("Markov Order will be {:d}".format(NewValue))',
                                Title='Order',
                                Instruction='\nEnter the Markov order\nyou want to use:',
                                Advice='   Number should be between {:d} and {:d}.   ',
                                Currency='',
                                Minimum = 1, Maximum = 4),
                                **self.std_button_opts)
        self.OrderButton.pack(**std_pack_opts)
 
        self.ParaLenButton = Button(self, textvariable=self.ParaLenButtonName,
                                cursor='plus', font=self.NormalFont,
                                command=lambda:
                                self.UpdateNumberButton(Parent='self',
                                Variable='self.ParaLength',
                                ButtonName='self.ParaLenButtonName',
                                Font=self.NormalFont,
                                ButtonFormat='.set("Paragraph: {:d} words long".format(NewValue))',
                                Title='Length',
                                Instruction='\nEnter the length of paragraph\nyou want to create:',
                                Advice='   Number should be between {:d} and {:d}.   ',
                                Currency='',
                                Minimum = 100, Maximum = 1000),
                                **self.std_button_opts)
        self.ParaLenButton.pack(**std_pack_opts)
 
        Label(self, text=BlankLine).pack()
 
        Button(self, text='Create Markov Text >>>', command=self.run_markov,
                                font=self.FancyFont,
                                **self.std_button_opts).pack(**std_pack_opts)
 
        Label(self, text=BlankLine).pack()
 
        Button(self, text='Quit', command=self.quit, font=self.NormalFont,
                                **self.std_button_opts).pack(**std_pack_opts)
        return
 
 
 
    def onAdviceOKButton(self, parent):
        """Kills the parent window when OK is clicked
        """
        self.InfoWindow.grab_release()
        eval(parent + '.grab_set()')
        self.InfoWindow.destroy()
 
 
    def InfoBox(self, Parent='root', Title='', Font=('Helvetica', 12),
                Text='Missing text'):
        """General utility for getting user confirmation on a status
        """
        self.InfoWindow = Toplevel(self)
        eval(Parent + '.grab_release()')
        self.InfoWindow.grab_set()
        geom_string = "+{}+{}".format(w-25, h+120)
        self.InfoWindow.geometry(geom_string)
        self.InfoWindow.title(Title)
 
        Label(self.InfoWindow, text=Text, width=30, font=Font,
              wraplength=200).pack(padx=10)
 
        Button(self.InfoWindow, text='OK', justify=CENTER, font=Font,
               padx=15, pady=5, command=lambda:
               self.onAdviceOKButton(Parent)).pack(pady=10)
        return
 
 
    def ListFiles(self, parent='root', MaxShow=10):
        """List the files selected by the user
        """
        NameList, FileCount = [], 0
        NumFiles = len(self.path_list)
 
        if NumFiles > MaxShow:
            if NumFiles==(MaxShow+1):
                MaxShow -=1
            FilesLeft = NumFiles - MaxShow
 
        for path in self.path_list:
            Folder, FileName = os.path.split(path)
            NameList.append(FileName)
            FileCount += 1
            if FileCount == MaxShow:
                if NumFiles > MaxShow:
                    NameList.append("   Plus {} more...".format(Cardinal(FilesLeft)))
                break
 
        FileList = "\n"
        FileList += "\n\n".join(NameList)
        FileList += "\n"
 
        self.InfoBox(Parent=parent, Title="Files Chosen:", Text=FileList,
                     Font=self.NormalFont)
        return
 
 
    def reset_first_words(self):
        """Resets all variables related to the opening words in the paragraph
        """
        self.FirstWordsButtonName.set('No opening words are set: choose a group at random')
        self.FirstWordsDisp.set('=== COPY & PASTE YOUR OPENING WORDS HERE ===')
        self.FirstWordsString.set("")
        return
 
 
    def onStartButton1(self):
        """This is called when the user wants to save the pasted opening words
        """
        if (self.FirstWordsDisp.get()[:3] == '===')  or \
            (len(self.FirstWordsDisp.get()) == 0):
            self.reset_first_words()
        else:
            """Newline forces button text to 2 lines, which maintains the
            button shape when the text gets longer when the words are shown:
            """
            self.FirstWordsString.set(self.FirstWordsDisp.get())
            self.FirstWordsButtonName.set('Opening words will be: "{}"...'.
                                          format(self.FirstWordsDisp.get()))
 
        self.FirstWordsWin.destroy()
        return
 
 
    def onStartButton2(self):
        """Called when the user decides not to save the pasted opening words
        """
        self.reset_first_words()
        self.FirstWordsWin.destroy()
        return
 
 
    def GetFirstWords(self):
        """Opens Entry dialog box for user to paste their opening words into
        """
        self.FirstWordsWin = Toplevel(self)
        root.grab_release()
        self.FirstWordsWin.grab_set()
 
        geom_string = "+{}+{}".format(w-120, h+90)
        self.FirstWordsWin.geometry(geom_string)
 
        self.FirstWordsWin.title('Pick your opening words')
 
        Instruction = "\nType or copy & paste some opening words from one of your "
        Instruction += "chosen text files into the space below. The random "
        Instruction += "Markov text will begin with these words. "
        Instruction += "Don't worry about putting them in quotation marks:"
 
        Label(self.FirstWordsWin, text=Instruction, font=self.NormalFont,
              wraplength="11c").pack(pady=5)
 
        FirstWordsEntry = Entry(self.FirstWordsWin, font=self.NormalFont,
                             textvariable=self.FirstWordsDisp,
                             width=80, justify='center')
        FirstWordsEntry.pack(pady=5)
        FirstWordsEntry.focus_set()
        FirstWordsEntry.select_range(0, END)
 
        button_1_title = "START my Markov paragraph with the above words"
        Button(self.FirstWordsWin, text=button_1_title, font=self.NormalFont,
               padx=5, pady=5, command=self.onStartButton1).pack(pady=5)
 
        button_2_title = "Don't worry about the opening words. Start my Markov "
        button_2_title += "nonsense text with a randomly selected sequence of "
        button_2_title += "words from one of my text files."
 
        Button(self.FirstWordsWin, text=button_2_title, font=self.NormalFont,
               command=self.onStartButton2, **self.std_button_opts).pack(pady=5)
        return
 
 
    def ValidateInt(self, new_text):
        '''Checks every char UpdateNumberButton() gets is part of a valid int
        '''
        if not new_text:
            return True
        try:
            entered_number = int(new_text)
            self.UpdateButton.config(state=NORMAL)
            return True
        except ValueError:
            return False
 
 
    def onUpdateNumberButton(self, parent, minimum, maximum, variable,
                             button_name, button_format):
        """Checks the value entered is correct. Updates variable and button name
        """
        NewValue = int(self.NewNumEntry.get())
 
        if ((maximum is not False) and (minimum <= NewValue <= maximum)) or \
            ((maximum is False) and (minimum <= NewValue)):
 
            eval(variable + '.set({})'.format(NewValue))
            eval(button_name + button_format)
 
            self.NewNumberEntryWin.grab_release()
            eval(parent + '.grab_set()')
            self.NewNumberEntryWin.destroy()
            return
 
        else:
            self.NewNumEntry.bell()
            self.UpdateButton.config(state=DISABLED)
            self.NewNumEntry.delete(0, END)
            return
 
 
    def UpdateNumberButton(self, Parent='root', Variable='self.DollarAmount',
                    ButtonName='self.NoButtonName', Font=('Helvetica', 11),
                    ButtonFormat='.set("${:,.0f}".format(NewValue))',
                    Title='Unknown Update',
                    Instruction='Check your code: window needs an instruction',
                    Minimum=0, Maximum=1, Width=9,
                    Advice='   Figure should be between ${:0,.0f} and ${:0,.0f}.   ',
                    Currency='          $', Suffix=''):
        """Opens a child Entry window to ask for the new number
        """
        self.NewNumberEntryWin = Toplevel(self)
        eval(Parent + '.grab_release()')
        self.NewNumberEntryWin.grab_set()
 
        geom_string = "+{}+{}".format(w-25, h+300)
        self.NewNumberEntryWin.geometry(geom_string)
 
        self.NewNumberEntryWin.title(Title)
 
        r=0; c=0
        self.NewCashInstruction = Label(self.NewNumberEntryWin, text=Instruction, font=Font)
        self.NewCashInstruction.grid(row=r, column=c, columnspan=3, padx=10)
 
        r+=1; c=0
        Label(self.NewNumberEntryWin, text=Currency, justify=RIGHT, font=Font).grid(
                                row=r, column=c, sticky=E)
 
        c+=1
        vcmd = self.NewNumberEntryWin.register(self.ValidateInt)
        self.NewNumEntry = Entry(self.NewNumberEntryWin, validate="key",
                                justify=CENTER, validatecommand=(vcmd, '%P'),
                                width=Width, font=Font)
        self.NewNumEntry.grid(row=r, column=c, pady=5)
        self.NewNumEntry.focus_set()
 
        c+=1
        Label(self.NewNumberEntryWin, text=Suffix, justify=LEFT, font=Font).grid(row=r,
                                column=c, sticky=W)
 
        c+=1
        self.UpdateButton = Button(self.NewNumberEntryWin, text='Update', font=Font,
                                justify=LEFT, state=DISABLED, width=6,
                                command=lambda:
                                    self.onUpdateNumberButton(Parent, Minimum,
                                    Maximum, Variable, ButtonName, ButtonFormat))
        self.UpdateButton.grid(row=r, column=c, padx=5, pady=5)
 
        r+=1; c=0
        if not Maximum:
            self.NewNumAdvice = Label(self.NewNumberEntryWin, text=Advice.format(
                                Minimum), font=Font)
        else:
            self.NewNumAdvice = Label(self.NewNumberEntryWin, text=Advice.format(
                                Minimum, Maximum), font=Font)
        self.NewNumAdvice.grid(row=r, column=c, pady=5, columnspan=4)
        return
 
 
    def GetFileList(self):
        """Returns a list of path names for your own code to open elsewhere
        """
        if self.path_list != []:
            # a set of files have been chosen before. Go to the same place:
            self.file_opt['initialdir'], an_old_text_name = os.path.split(self.path_list[0])
        else:
            old_path_list = self.path_list
            self.file_opt['initialdir'] = '.'
        old_path_list = self.path_list
 
        Key = 'CTRL'if platform.mac_ver()[0] == '' else 'Command'
 
        self.file_opt['title'] = 'Use SHIFT-click and {}-click to pick multiple text files:'.format(Key)
 
        self.file_opt['initialfile'] = '*.txt'
 
        self.path_list = list(tkinter.filedialog.askopenfilenames(**self.file_opt))
 
        if self.path_list != []:
            path_list_copy = self.path_list.copy()
            for index, path in enumerate(path_list_copy):
                if "*.txt" in path:
                    del self.path_list[index]
                    break
            num_files_chosen = len(self.path_list)
            verb = 'Add' if num_files_chosen == 1 else 'Change'
            plural = 's' if num_files_chosen > 1 else ''
            self.fileSelector.set('{} files'.format(verb))
            self.reset_first_words()
            number = Cardinal(num_files_chosen)
            self.FileCountButton.set('{} file{} selected'.format(number.capitalize(), plural))
        else:
            self.path_list = old_path_list
 
        if self.path_list != []:
            self.ListFilesButton.config(state=NORMAL)
        return
 
 
    def save_as_file(self, result):
        """ Saves the result of your program to a file
        """
        if self.save_path_and_name:
            self.file_opt['initialdir'], save_name = os.path.split(self.save_path_and_name)
 
        OldSaveFilePath = self.save_path_and_name
        self.file_opt['title'] = "Save results to:"
        self.file_opt['initialfile'] = 'Markov_Result.txt'
 
        self.save_path_and_name = tkinter.filedialog.asksaveasfilename(**self.file_opt)
        if self.save_path_and_name:
            file = open(self.save_path_and_name, 'w')
            file.write(result)
            file.close
            self.file_opt['initialdir'], save_name = os.path.split(self.save_path_and_name)
        else:
            self.save_path_and_name = OldSaveFilePath
        return
 
 
    def run_markov(self):
        """A simple wrapper to pass your dashboard-set variables to your logic
        """
        result = ''
        FirstWords = self.FirstWordsString.get()
 
        if self.path_list == []:
            tkinter.messagebox.showinfo(title='No text files chosen   ',
                message="Please choose some texts to\nturn into meaningless gibberish.",
                icon='error')
 
        elif FirstWords != '' and (len(FirstWords.split()) != self.MarkovOrder.get()):
            tkinter.messagebox.showinfo(title='Markov Error   ',
                message="The number of opening words\nmust equal the Markov order.",
                icon='error')
 
        else:
            result, error  = create_markov_text_from(self.path_list,
                                    markov_order=self.MarkovOrder.get(),
                                    word_len=self.ParaLength.get(),
                                    starting_words=self.FirstWordsString.get())
            if error != 'OK':
                self.InfoBox(Parent='root', Title="Error", Text=error, Font=self.NormalFont)
                return
            else:
                self.save_as_file(result)
        return
 
 
 
 
if __name__=='__main__':
    root = Tk()
 
    HalfScreenWidth = int(root.winfo_screenwidth()/2)
    HalfScreenHeight = int(root.winfo_screenheight()/2)
 
    w = HalfScreenWidth - 200
    h = HalfScreenHeight - 350
    geom_string = "+{}+{}".format(w, h)
 
    root.geometry(geom_string)
    root.title('Dashboard')
    root.lift()
    PythonGUI_2(root).pack()
 
    root.mainloop()

