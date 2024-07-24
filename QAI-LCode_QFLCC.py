##################################################################################
# Quantum AI Lens Coding (QAI-LCode) and Classification (QFLCC) program as part of  
# the quantum field lens coding algorithm (QFLCA), program code and execution.
# Standard filename is: QAI-LCode_QFLCC.py
# Written in Python by P. B. Alipour, @ ECE Dept. University of Victoria, 
# Victoria BC, Canada. 
# ORCID: https://orcid.org/0000-0003-1037-018X Copyright © 2022--2024, ver. 1.0
#--------------------------/// Description ///-----------------------------------
# This QFLCC version of the QAI-LCode is basic. More revisions to come, as the 
# dataset grows on the number of trials on 1 or more QDF circuits occurs relative 
# to improvements of dataset representation of quantum and classical parameters 
# in observing a thermodynamic system based on Refs. [1-3,5] of the Data in Brief, 
# Elsevier J article.
##################################################################################
# Importing required library
import math, csv
import numpy as np
import importlib

import warnings  # As packages like 'pandas' develop, warning after compilation can be annoying until essential! 
warnings.filterwarnings("ignore") # Suppress incompatible/outdated floating point numpy errors.
import pandas as pd

import sys # This module provides signal interruption services, or access to the variables 
           # and functions that interact strongly with the interpreter.
import keyboard # For a specific command or key stroke as an interrupt signal coming from the keyboard by user.
import winsound # For system sound representing a state of event or algorithm step. 
#from playsound import playsound.

import colorama
import time   # To delay at certain checkpoints for viewing I/O data or calculation results
from time import sleep
import datetime  # For recording r/w file time entry 
import threading
from pathlib import Path  # For accessing and conduct operations on files/directories 
import os
import webbrowser # To load/view *.htm or *.html files.

import re  # For search and spot regular expressions in {text, metadata, binary,...} I/O files.
import subprocess # To record I/O terminal events.
from joblib import Parallel
import multiprocessing
import threading
from alive_progress import alive_bar # For live progressbar on active simulations and dataset analysis. 
from array import *
from multiprocessing.pool import ThreadPool
from random import random
from threading import Thread
import concurrent.futures, shutil # For copying I/O data files from other directories concurrently.
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style  # To print certain text in standard color for highlighting 
                                 # quantum points vs. classical points about the measurement dataset
import termplotlib as tpl # To draw plots on circuit results during/after experiment. 
from colored import fg, bg

import click
@click.group()
def cli():
    """Main entry point."""

@cli.command()
@click.option("-d", "--debug", help="Include debug output.")
def build(debug):
    """- Build production assets."""

#-------------------------------------------------------------------------------------------------
# Colored foreground (fg) and background (bg) Classes for sectioning and highlighting the code 
# according to a specific QF-LCC algorithm step, checkpoint, computer operation, error, or HALT. 
#-------------------------------------------------------------------------------------------------
class fg:
        black='\033[30m'
        silver="\033[0;38;5;7m"
        red='\033[31m'
        green='\033[32m'
        orange='\033[40m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
      
        """- Colored foreground (fg) class for sectioning and highlighting the 
        QF-LCC algorithm step, checkpoint, computer operation, error, or HALT."""

class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
        """- Colored background (bg) class for sectioning and highlighting the 
        QF-LCC algorithm step, checkpoint, computer operation, error, or HALT."""

import random  # To generate random numbers.
class ExitMyProgram(Exception):
    """- Exception used to exit program."""
 
def QFLCC_program():
    while True:
        if random.randint(1, 1000) == 500:
            raise ExitMyProgram
        """- QFLCC program steps prior are more complicated than shown here. This is to 
        end the current QFLCC program step engaged by the user."""

def main_exit():
    ###################################################
    # Run the ending of the current QFLCC program step 
    # and catch the ExitMyProgram exception.
    ###################################################
    global entry_stage, sim_state # Any exit entry of the program is reset back to 0. 
      
    try:
        QFLCC_program()
    except ExitMyProgram:
         print(fg.yellow+Back.RED+"The program is terminated manually!")
         # Log the exit of the program. 
         entry_stage = -1 # This value resets entry to 0 via its
                          # default increment += 1. 
         entry_stage += 1
         file_ = open('shell_output.txt', 'a')
         now = datetime.datetime.now() # Date the I/O file entry 
         subprocess.run("echo {}- Checkpoint logged on {} for all programs: \
///-PROGRAM TERMINATED--///".format(entry_stage, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_)
         raise SystemExit      
        
#---------------------------------------------------------------------------------------------------
# The thread launches an invoked code function by the user, while the main thread (program 
# application) continues. Once the user input, the user may want to ask the thread printing to stop.
#---------------------------------------------------------------------------------------------------
numcores = 32 # How many cores on your device to process QF-LCA data...
max_workers=numcores/8 # Depending on your classical or quantum device, assign workers/threads/nodes 
# as many as necessary via +,/,* to the numcores available on the device running this program. 
__space__ = None
filesFlag = 0 # File state/flag is 0 in case of dataset files are not present 
              # and to be copied to the current directory.

def site_doc():
#############################################################
# To load and read QFLCA project documentation website. 
#############################################################
    global site_dir, site_name
    site_file = ["index.html", "about.html", "QAI-LCode_QFLCC-reference.html",
             "QDF-game-reference.html"] # This html file is stored in the same site folder to read.
    site_dir = "site" # This site folder contains project's documentation html files to read.
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) # Play sound.
    if site_name == "home-site":
         webbrowser.open_new_tab(os.path.join(site_dir, site_file[0]))
    elif  site_name == "about-site":
          webbrowser.open_new_tab(os.path.join(site_dir, site_file[1]))
    elif  site_name == "qflcc-site":
          webbrowser.open_new_tab(os.path.join(site_dir, site_file[2]))
    elif  site_name == "game-site":
          webbrowser.open_new_tab(os.path.join(site_dir, site_file[3]))

#### Volume Settings #### 
import pyautogui as p

def set_vol(new_volume):
#############################################################
# The volume function sets volume according to your OS. 
# This option is available as 'v' or 'volume' during program.
#############################################################
    p.press('volumedown', presses = 50) # Sets volume to zero.
    time.sleep(0.5) # Using time.sleep to space the presses. 
    x = math.floor(new_volume / 2) # Setting the amount of presses required.
    p.press('volumeup', presses = x) # Setting the volume.
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) # Sound test. 
    """- End of volume settings."""

dir_flag = 0 # Directory flag for dataset directory is built when set to 0. 
             # If set to 1 after installation, directory will be accessed in a safe mode 
             # (SM) environment, and not re-installed. 

def prompt():
###################################
# Prompting code for a user input #
###################################
    global __help__, promptIn, site_name, entry_stage # File state/flag is 0 or 1 
    # to see if dataset files are present and to be copied to the current directory.
    global dir_flag # Directory flag for dataset directory access in safe mode when set to 1.
    __help__ = 'h'

    while True:
        print(fg.lightgreen + "\r< ", end=""), sleep(1.1)
        print("\r> ", end=""+Fore.RESET), sleep(1.1)
        try:
             promptIn = str(input())
             # Respond to the user's choice or command.
             if promptIn == 'n' or promptIn == 'next':
                print("Next...\n")
                break
             elif promptIn == 'v' or promptIn == 'volume':
                vol = float(input("Input sound volume (° ͜ʖ ͡°)👂🕪  between [🔇 = 0 for muted,\
 and 🔊 = 100 for loudest]:"))
                set_vol(vol)
                prompt() # Restart.
                if vol < 0:
                       print(fg.red +"Out of range or wrong value entered! Readjusted to muted or 0!")
                       prompt() # Restart.
                if vol > 100:
                       print(fg.red +"Out of range or wrong value entered! Readjusted to maximum or 100!")
                       prompt() # Restart.
                break
             elif promptIn == 'b' or promptIn == 'begin' or promptIn == 'r' or promptIn == 'restart':
                  print('Restarting program...☝(° ͜ʖ ͡°)☝')
                  subprocess.run(["python", "QAI-LCode_QFLCC.py"])  # Restart program.
                  break
             elif promptIn == 'cls' or promptIn == 'clear':
                  os.system('cls') # Clear screen.
             elif promptIn == 'website' or promptIn == 'site' or promptIn == 'about' or promptIn == 'web': 
                  site_name = "about-site" # This html file is stored in the same site folder to read.
                  site_doc() # Load website.
             elif (promptIn == 'dir' or promptIn 
                   == 'sm dir') and (dir_flag == 1): # Active only in safe mode directory environment when set to 1. 
                  safeMode_dir() # Run safe mode directory environment during simulation and dataset anlysis.
                  dir_flag == 0 # Reset flag until next time requested by the user to access dataset files.
                  break
             elif (promptIn == 'dir' or promptIn == 'sm dir') and (dir_flag == 0):
                      print(f"🚫 This command is supported only in the QFLCA's Safe Mode (SM:>>) environment!\
 \n\x1B[4m-Enter 'dir' at the dataset analysis & simulation stage after QFLCC directory installation!\x1B[0m" 
 + fg.lightgreen)     
                      continue
             elif promptIn == __help__ or promptIn == 'help':
                  userHelp()  # Show help.
                  continue
             elif promptIn == 'e' or promptIn == 'exit':
                  # Play Windows exit sound.
                  winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                  print('Exiting program...🖐 (° ͜ʖ ͡°)🖐  Goodbye!')
                  entry_stage = 0
                  main_exit() # Terminate program. 
             else:
                print('Input command or response. For help, enter \'h\'... ')
                continue
        except ValueError:
             main_exit()
             print("Invalid input. Please enter a response.")
'''
# The following part is an animated image shall be displayed on terminal!
'''

wid=[] # Register width value of an object like image during program run for later use.
hgt=[] # Register height value of an object like image during program run for later use.
chars=[]
spaces=[]
entry_stage=[] # This is defined to create checkpoints for certain steps of the program to log,
               # register or recall when e.g., called to revisit a function.
# This function is used for overwriting previously printed lines 
def clear_line(wid):
    global spaces
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for spaces in range(wid):
      print(LINE_UP, end=LINE_CLEAR)

# These packages are imported relevant to the intro-anim function next.
#-----------------------------------------------------------------------------------
import chafa  # This package is installed via e.g., "pip install chafa.py" command.
import random  # For returning random numbers. 
from chafa import *
from PIL import Image
from chafa.loader import Loader  # This also requires installing Wand and 
# ImageMagick .dll packages, 
# or visit https://chafapy.mage.black/usage/installation.html 
# and https://docs.wand-py.org/en/0.6.10/guide/install.html 
#-----------------------------------------------------------------------------------

def intro_anim():
     global chars
#######################################
# Calling this function will run 
# an animated intro image displayed 
# on terminal!
#######################################
     # Enable the following commented code lines if you switch to chafa.loader..
     # The active code lines use both chafa.loader and 
     # the Pillow (PIL) package definitions/functions. Only comment out when indicated..  
     #----------------------------------------------------------------------------------
     #FONT_HEIGHT = 12*6  #24 # Default value for image height >= image width.
     #FONT_WIDTH  = 26*2  #11 # Default value for image height >= image width.
     #FONT_RATIO = (FONT_WIDTH / FONT_HEIGHT) # A scalar ratio to keep dimensions fixed by product multiplication. 

     config = CanvasConfig()

     #config.height = 9 #60 # Default value for a square image.
     #config.width  = 160 #60 # Default value for a square image.

     # Set the canvas cell geometry.
     #config.cell_height = FONT_HEIGHT
     #config.cell_width  = FONT_WIDTH

     # Create a list of image objects 
     img_list=  ["./__img__/qdf-circuit-sprite/1D-circuit-00.png", #32-bit depth images
                 "./__img__/qdf-circuit-sprite/1D-circuit-a.png", "./__img__/qdf-circuit-sprite/1D-circuit-b.png",
                 "./__img__/qdf-circuit-sprite/1D-circuit-c.png", "./__img__/qdf-circuit-sprite/1D-circuit-d.png",
                 "./__img__/qdf-circuit-sprite/1D-circuit-d.png"] 
                
     # Loop through the gif image objects for a while.
     for j in range(0, 6):
      for img in img_list:
          print("\033[1A", end="\x1b[2K", flush= True), sleep(0.001)
          #image = Loader(img_list[j])   # Open image with chafa.loader or Loader.
          image = Image.open(img_list[j]) # Open image with PIL. Not used by Loader. 
          
          wid, hgt = image.size
          mode = image.mode  # Detect image mode on your system. 
     
          # When PIL package definitions are used. Comment out if using chafa.loader.
          if (img == "./__img__/1D-QDFcircuit-sprite/1D-circuit-02.png" or 
              img == "./__img__/1D-QDFcircuit-sprite/1D-circuit-03.png"):
               config.height = (hgt/8.8)   
               config.width  = wid/8.8  
          else:
            config.height = hgt/7.8
            config.width  = wid/6.6

          #config.height = (hgt/6.4) - 1
          #config.width  = wid/7.2  
          # Enable one of the switches to configure canvas to draw a high resolution image (for chafa.loader). 
          #--------------------------------------------------------------------------------------------------
          #config.pixel_mode = chafa.PixelMode.CHAFA_PIXEL_MODE_SIXELS  # To display a high resolution image
          #config.pixel_mode = chafa.PixelType.CHAFA_PIXEL_RGBA8_UNASSOCIATED  # To display according to 
          # terminal's output controls use config.pixel_mode = chafa.PixelMode.CHAFA_PIXEL_MODE_KITTY 
          # to display a high resolution image.
          #config.pixel_mode = chafa.PixelMode.CHAFA_PIXEL_MODE_KITTY 
          #config.pixel_mode = chafa.PixelMode.CHAFA_PIXEL_MODE_SYMBOLS  # To add symbols to image
          #config.pixel_mode = chafa.PixelType.CHAFA_PIXEL_BGRA8_UNASSOCIATED
          #-------------------------------------------------------------------------------------------------

          # Configure the ideal canvas geometry based on our FONT_RATIO, when using chafa.loader or PIL.
          #config.calc_canvas_geometry(  
          #image.width,
          #image.height,
          #FONT_RATIO
          #)
            
          # Set symbol map for visibility:
          # add 0's and 1's and quantum states to the map, relevant to the topic of this QFLCA program
          symbol_map = chafa.SymbolMap()
          symbol_map.add_by_range("a", "f")        
          
          bands  = len(image.getbands())  

          # Put image into correct format
          pixels = image.tobytes()
          canvas = Canvas(config)
               
          # Draw the intro image or graphics, when using chafa.loader. 
          '''canvas.draw_all_pixels(    
          image.pixel_type,
          image.get_pixels(),
          image.width, image.height,
          image.rowstride
               )'''
          
          # Draw the intro image or graphics, when loading image using PIL. 
          canvas.draw_all_pixels(    
          PixelType.CHAFA_PIXEL_RGBA8_PREMULTIPLIED, # Other example is .CHAFA_PIXEL_RGBA8_UNASSOCIATED, 
                                                     # given the image mode.
          pixels,
          image.width, image.height,
          image.width * bands
               )
          #--------------------------------------------
          #  Drawing Chars on Canvas.
          #--------------------------------------------
          QP_rand = random.random()  # Returns a random number between 0 and 1.
          CP_rand = random.randint(0, 1) # Returns a random number denoting the classical state.
          Int_rand= random.randint(0, 3) # Returns a random number denoting the quantum state.
                 
          for pixel in canvas[4,::10]:
               pixel.char = "1"

          for pixel in canvas[5,::10]:
               pixel.char = "0"

          #i = 0  # For drawing a sequence of chars or numbers on canvas. 
          #for pixel in canvas[:-3:-1, 3]:
          #     pixel.char = str(i)[0]
          #     i += 10

          print(canvas[3,55].char)
          canvas[3,55].char = "H" # Denotes the H gate in the partial QDF circuit.
          ## Superposition state is obtained by Hadamard gate (H) by 
          ## H|0〉=(|0〉+|1〉)/sqrt(2) and H|1〉=(|0〉-|1〉)/sqrt(2). 
          
          s = str(round(QP_rand, 2)) # Round the random value to two decimal points and convert to string. 
          c = 7 # Column cell number to draw a char.
          
          if img == "./__img__/1D-QDFcircuit-sprite/1D-circuit-05.png":
               s = "0.66"  # This is the expected P value >= 2/3 for a strong QDF prediction. 

          for r in s[0:3]: 
               canvas[c,55].char = "0"
               canvas[c,56].char = "."
               canvas[c,57].char = r # Draw the first three chars on canvas.
          
          canvas[3,82].char = "X"  # Denotes the X gate in the partial QDF circuit. 
          canvas[c,82].char = CP_rand
          
          #--------------------------------------------------------------------------------
          # The following is for terminal output and image info printouts per 
          # a cleared terminal line.
          #--------------------------------------------------------------------------------
          # clear_line(config.height) # Disable this if you want to see all frames in a sequenced list.  
          clear_line(config.width) # Disable this if you want to see all frames in a sequenced list.
          
          output = canvas.print()  # Default option.

          #--------------------------------------------------------------------------------
          # Write and Print images on the terminal.
          #--------------------------------------------------------------------------------    
          # Write picture
          print(output.decode(), Back.RESET), sleep(0.05)  # without decoding is raw data of the image.
   
          #if QP_rand > 0.5:   # Qubit P values printed in color for the corresponding circuit gates.
          #     print(fg.green + s, Back.RESET)
          #elif QP_rand <= 0.5 and img != "./__img__/1D-QDFcircuit-sprite/1D-circuit-05.png":
          #     print(fg.red + s, Back.RESET)
          #elif QP_rand <= 0.5 and QP_rand > 0.48: # Indicates P values approximating superposition. 
          #     print(fg.purple + s, Back.RESET)
          #elif img == "./__img__/1D-QDFcircuit-sprite/1D-circuit-05.png":
          #     print(fg.green + s, Back.RESET)

          # Print animated P's of gates in the 1D QDF circuit after logging all the animation frames. 
          file='intro-shell_output.txt' # The file to read/write from the terminal. 
          chars.append(s)
          chars = list(dict.fromkeys(chars)) # Removes duplicate values from recurring image frames. 
     
          with open(file, 'w') as file_to_write:
               # Write information about the original image sequence and final image frame.
               file_to_write.write(str(chars) + f"\n * Last animated step image: {img}" + 
                                 f"\n * Size: {wid} x {hgt} pixels" + f"\n * Mode: {mode}\n" 
                                 + str(datetime.datetime.now())) # date output entry to the file.
intro_anim(), sleep(0.05)  # Call this function to run the intro animation after a pause upon animated canvas drawing. 

def intro_anim_print():
#----------------------------------------------
# This function prints the intro_anim results 
# from its log file upon animation conclusion.
#----------------------------------------------
  with open("intro-shell_output.txt", "r") as input_file:
    for i in range(1):
         head = next(input_file).strip()
         print(fg.black+ bg.orange+"Animated P's of the QDF circuit, frame-by-frame = "+Back.RESET)
         print(fg.yellow, head)
    
    lines = input_file.readlines()[:-1]
    
    # Clean up the newlines in the lines of data. 
    lines = [line.rstrip('\n') for line in lines]
    
    # Split each line at the "," character.
    lines = [line.split(',') for line in lines]
    print(fg.lightgreen, lines, bg.green +fg.yellow + Back.RESET)
    print(bg.blue + Fore.BLACK + str(datetime.datetime.now()) + Back.RESET)
  input_file.close()
  
  print(bg.red+fg.yellow + 
        f"<<........ 1D QDF circuit animation as an update to the QFLCA-QFLCC v.1.0, has successfully concluded ........>>")
  print(f"<<........ Next... QFLCA Program's Prompt & Command Begins! ........>>", Back.RESET)
  print(Fore.LIGHTYELLOW_EX + f"======================================================================", Back.RESET)

intro_anim_print() 

#exit()  # enable this exit for a step-wise test
#breakpoint() # enable this or similar places for debugging... just in case! 

###################################
# Prompting step starts from here 
###################################
print(Back.LIGHTBLACK_EX + fg.lightgreen+ f"When this input signal, > or < switch appears: ")             
print("it means you can input a keyboard character then press [Enter], or input response, then \
press [Enter] to a program query. For more information, enter \'h\'...")

def userHelp():
     # Play Windows question sound and display recalled tips to the user.
     winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
     print('Input tips: \n-Enter \'n\' key for the \'next\' message or input. \n-Enter \'h\' or \'help\' \
to display these tips. \n-Enter a file number when an uploaded file list is displayed to view result. \
\n-Enter \'dir\' or \'sm dir\' at the dataset analysis & simulation stage after QFLCC directory installation.*\
\n*-This command is supported only in the QFLCA\'s Safe Mode (SM:>>) environment!\
\n-Enter \'site\' or \'web\' to view the \'website\' \'about\' this program or project. \
\n-Enter \'b\' or \'r\' to \'restart\' or \'begin\' program. \n-Enter \'v\' or \'volume\' for sound volume \
change during program. \n-Enter \'cls\' or \'clear\' to clear screen. \n-Enter \'e\' to \'exit\' the program.')

process = Thread(target = prompt)  # Invoke prompt() function by creating and executing threads
process.start()
#__space__ = input("Input something:")
#if input():
process.join() # Wait for the thread to terminate

if entry_stage == 0:  # This makes sure when main_exit is called, program exit is executed without bypassing it.
     main_exit()

"""- QFLCC code continues."""
#-------------------------------------------------------------------------------------------------
# Code Use and Copyright Information
#-------------------------------------------------------------------------------------------------
__ORCID__ = "ORCID: https://orcid.org/0000-0003-1037-018X"
__copyright__ = "Copyright © 2022--2024"
__license__ = "Creative Commons (CC BY-NC-ND)"
__author__ = "Philip B. Alipour"
__location__ = "@ ECE Dept. University of Victoria, Victoria BC, Canada"
__version__ = "ver. 1.0"
__description__ = "This QFLCC version of the QAI-LCode is basic. More revisions to come, as the \
dataset grows on the number of trials on 1 or more QDF circuits occurs relative to improvements \
of dataset representation of quantum and classical parameters in observing a thermodynamic system \
based on Refs. [1-3,5] of the Data in Brief, Elsevier J article."
print(Back.BLUE + fg.lightgreen + __description__, "\n") 
print(Back.RESET+"Copyright information in Python code:\n") 
print("\033[0m"+__license__ , __author__, __location__+',', fg.blue+"\x1B[4m"+__ORCID__+"\x1B[0m", 
      __copyright__, __version__, fg.pink+bg.lightgrey)
sleep(5)

##########################################
# Main dataset file directory installation 
# and listing steps starts here.  
##########################################
from tqdm import tqdm  # This is for progressbar display.

ibmq_f=0 # File flag set to 0 by default for IBMQ files if as not IN   
qi_f=0   # File flag set to 0 by default for QInspire files as not IN
dir_flag = 0 # Directory flag is set to 1 for dataset directory access in safe mode. 
           # Installing files is building the directory, so it is set to 0 here.  

print(os.getcwd())

ppath = Path(os.getcwd()).parent # This points to the parent path of current directory.
cpath = Path(os.getcwd())  # This is the current path.
print(ppath.absolute())
IBMQ_dir = os.path.join(ppath, 'IBMQ\\test\\')
QI_dir = os.path.join(ppath, 'QI\\test\\')
QI_files = os.listdir(QI_dir) # Fetching the list of all the files.
IBMQ_files = os.listdir(IBMQ_dir) # Fetching the list of all the files.
print('Importing IBMQ/QI data files: ', IBMQ_files, QI_files)  # Prints from e.g., C:/here/my_dir

pool = ThreadPoolExecutor(max_workers)

file_ = open('shell_output.txt', 'w+') 
subprocess.run("echo ///--- QFLCC Shell Log_file START ---///", shell=True, stdout=file_) 

now = datetime.datetime.now() # Date each I/O file entry.

try:
   # with MultithreadedCopier(max_threads=16) as copier: # this is to achieve e.g., ~35x speedup on a 32 core machine. 
   # with ThreadPool(4) as copier:
    with pool as executor:
            for file_name1 in QI_files:
             future = executor.submit(shutil.copy, QI_dir + file_name1, cpath)  # future = pool.submit(my_task, argument) 
                                                                                # does not block.
             qi_f=1
            for file_name1 in IBMQ_files:
                future = executor.submit(shutil.copy, IBMQ_dir+file_name1, cpath)
                ibmq_f=1
            value = future.result() # This one blocks.
            print(Back.RED + fg.black 
                  + f'Thread ---> <{value}> <--- got {future}. Maximum threads initiated: {int(max_workers)}')
            pool.shutdown()  

    print('All IBMQ/QI data files imported successfully!')
    #----------------------------------
    # File directory listing code
    #----------------------------------
except Exception as e:
    for i in tqdm(range(0, 10), ncols = 100, desc =Back.RESET+"Progress: "+Fore.RED): # Progress level of a copy operation. 
         time.sleep(.05)
    print('1 or more IBMQ/QI data files import failed!')
    qi_f=0
    ibmq_f=0
    print(e)

print(Back.RESET+'||||||||||||||||||||||||||||||||||||||') #, fileresult, sep="\n")
print(Fore.YELLOW + 'You may view any of the files listed below by clicking on the file or [Ctrl + Mouse_click] option:')

res = os.listdir()
fileresult = []

for (idx, st) in enumerate(res, 1):
    print(bg.green+'This is file # {} for {}'.format(idx, st.split('/')[-1]))
    time.sleep(.05)
    fileresult.append(st) 
    for i in tqdm(range(0, 1), ncols=100, desc =Back.RESET+f"Progress: {st}"+fg.lightcyan + Style.BRIGHT): # Progress level of copy operation.
     # For any error related to this line on colors, install this: pip install tqdm==4.59.
     time.sleep(.05)
     subprocess.run("echo {}- Checkpoint logged on {} for file # {} \
as {}".format(idx, now.strftime("%Y-%m-%d %H:%M:%S"), idx, fileresult[idx-1]), shell=True, stdout=file_)

#res=os.listdir().index() # Enable this line (with its print next) to have clickable files to load and view 
                          # on screen (not in terminal).

print(Style.RESET_ALL + fg.orange + bg.cyan +"||||||||||||||||||||||||||||||||||||||") 
#print(*res, '|||||||||||||||||||||||||||||||||||||||||', f'The current directory total listed files = {len(res)}', sep="\n") 
print('|||||||||||||||||||||||||||||||||||||||||', 
      f'The current directory total listed files = {len(res)}', sep="\n"), sleep(2) 
print("|||||||||||||||||||||||||||||||||||||||||"+Back.RESET)

#----------------------------------
# File directory listing code cont.
#----------------------------------
entries=[]

def file_reader():
#---------------------------------------------------------------
# File directory listing code cont. is by calling this function.
#---------------------------------------------------------------
 global entries, selected_path, selection
 while True:
  entries = []
  # Build a list of files and folders in the working directory.
  current_folder = Path.cwd()
  # If we're not already in the root, the first entry is the parent folder.
  if current_folder.parent != current_folder:
    entries.append(Path('..'))
  entries += current_folder.glob('*')
  # Print a numbered list of files and folders
  print(fg.cyan+f'Listing contents of {current_folder}')
  for i, path in enumerate(entries):
    print(f'{i}: {path.name}')
  # Get user input. Valid input is the word 'quit' or a number that corresponds
  # to an index in the list of files and folders
  print(fg.lightgreen + "Select a file # to see its contents in form of text before analysis, or enter \
\'n\' for next to analyze file contents:")
  print(fg.lightgreen + "\r< ", end=""), sleep(1.1)
  print("\r> ", end=""+Fore.RESET), sleep(1.1)
  user_input = input('') 
  if user_input == 'n' or user_input =='next':
    break
  elif user_input == '' or user_input =='h':
     userHelp() # Give user prompting tips.
     prompt() # Prompt user.
  elif user_input == 'v' or user_input == 'volume':
                vol = float(input("Input sound volume (° ͜ʖ ͡°)👂🕪  between [🔇 = 0 for muted,\
 and 🔊 = 100 for loudest]:"))
                set_vol(vol)
                file_reader() # Restart.
                if vol < 0:
                       print(fg.red +"Out of range or wrong value entered! Readjusted to muted or 0!")
                       file_reader() # Restart.
                if vol > 100:
                       print(fg.red +"Out of range or wrong value entered! Readjusted to maximum or 100!")
                       file_reader() # Restart.
  elif user_input == 'b' or user_input == 'begin' or user_input == 'r' or user_input == 'restart':
                  print('Restarting program...☝(° ͜ʖ ͡°)☝')
                  subprocess.run(["python", "QAI-LCode_QFLCC.py"])  # Restart program.
                  break
  elif user_input == 'cls' or user_input == 'clear':
                  os.system('cls') # Clear screen.
  elif user_input == 'e' or user_input == 'exit':
                  # Play Windows exit sound.
                  winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                  print('Exiting program...🖐 (° ͜ʖ ͡°)🖐  Goodbye!')
                  print(fg.yellow+Back.RED+"The program is terminated manually!"+Back.RESET)
                  sys.exit(1) # For abnormal termination, prefetch exception and force this exit. 
  try:
    selection = int(user_input) 
  except ValueError:
    print(fg.orange+'Invalid user input (please enter a number)'), sleep(1.1)
    continue
  if selection >= len(entries):
    print(fg.red+'Invalid user input (invalid number)'), sleep(2.1)
    continue
  # If the selected path is a folder, then change the working directory to
  # that folder.
  selected_path = Path(entries[selection])
  if selected_path.is_dir():
    os.chdir(selected_path)
    continue
  # Otherwise, try to read the file contents as if they are text. If this fails
  # print a warning message.
  try:
    file_contents = selected_path.read_text("UTF-8")
  except UnicodeDecodeError:
    print(Fore.LIGHTYELLOW_EX + f'{selected_path.name} is not a text or csv file'), sleep(2.1)
    continue
  # Otherwise print the file contents
  print(fg.black+bg.lightgrey + file_contents +Back.RESET)
  print(fg.lightgreen + "\r< ", end=""), sleep(1.1)
  print("\r> ", end=""+Fore.RESET), sleep(1.1)
  user_input = input('')

file_reader()

def filenum_call():
#----------------------------------
# This function takes in user's 
# file number request.
#----------------------------------
     global filenum, idx, entries, fileresult

     # Take file index value from user
     print(fg.orange +bg.cyan +"||||||||||||||||||||||||||||||||||||||") 
     print(f'The current directory total listed files = {len(entries)-1}', sep="\n") 
     print("|||||||||||||||||||||||||||||||||||||||||"+Back.RESET)
     filenum=input(fg.yellow+'Enter the relevant file # as {*.csv, *.txt, *.png} for analysis from the list: ')
     filenum=int(filenum)  # Typecast (convert) string datatype into integer.
     idx=filenum
     print("\n")
     print(Fore.GREEN + 'Selected file number is {} for {}'.format(idx, fileresult[idx-1]))
     
     if dir_flag == 1: # if Safe Mode is enabled then maintain a restricted yet error tolerant 
                       # safe mode environment for the user to select a dataset file form directory. 
        print(Back.LIGHTGREEN_EX + Fore.YELLOW + 
            "\033[1m<--- SAFE MODE DATASET ANALYSIS ENABLED --->\033[0m" + Back.RESET), sleep(2)
        print(f"{fg.lightgreen}Press any key to continue...")
        sys.stdout.write('SM:>>...')
        sys.stdout.flush()
        os.system("pause >nul")

filenum_call()

from pathlib import Path

def csv_analyzer():
#-------------------------------------
# Open the QFLCA "*.csv" for analysis. 
#-------------------------------------
   global pngfile

   with open(fileresult[idx-1], 'r') as x:
         pngfile=Path(f'{fileresult[idx - 1]}').stem
         sample_data = list(csv.reader(x, delimiter=","))
         print(Fore.RED + Back.YELLOW +
               f'Sample_data initiated... selected file for analysis from index value = 0 to {len(entries)-1} is: {idx}', sep="\n")
         print(Fore.CYAN + Back.RESET + '\033[1;4m' + '- User menu options are limited to Basic QFLCC program options.'+ '\033[0m')
         print(Fore.LIGHTCYAN_EX + '\033[1;4m' + '- Table data list:' + '\033[0m'+ Fore.RED + Back.CYAN + Fore.RED)
         subprocess.call([f'{pngfile}.png'], shell=True) # After stem from the selected csv filename, show the relevant 
                                                         # histogram and circuit with the csv file being analyzed.
         subprocess.call([f'{pngfile}_H.png'], shell=True) 
         sample_data = np.array(sample_data) # Import the P data into an array. 
         print(sample_data) 
         
         for row in sample_data:
                y=row[0]  # Store array's element value in y before converting csv left column data to a float value. 
                print(row[0] + Back.GREEN)
     ##############################################
# Getting the current work directory (cwd).
filesFlag = 0
thisdir = os.getcwd()
thisfile = fileresult[idx-1]

#---------------------------------------------------------------
# Standard group of file extensions that require a shared 
# operation for r/w analysis. 
# * This group can include more extension and tailored 
#   according to file_ext_call() and PAnalysis() functions. 
# * For more details, see file_ext_call() and PAnalysis() code.  
#---------------------------------------------------------------
ext0 = ('.docx','.txt') 
ext1 = ('.csv','.txt')
ext2 = ('.png','.jpg')
ext3 = ('.pdf','.exe')

# This will return a tuple of root and extension.
split_tup = os.path.splitext(thisfile)
print(split_tup)
 
# Extract the chosen filename and extension.
file_name = split_tup[0]
file_extension = split_tup[1]

def file_ext_call():
  #--------------------------------------------------------------------------
  # Call this function to setup and reconfigure r/w switches 
  # on the selected dataset file (extension based).
  # * See group of file extensions to operate r/w on prior to this function.
  #--------------------------------------------------------------------------
  global filesFlag
  ############################################################
  # Code reconfig options instead of the while loop:
  # r = root, d = directories, f = files
  # for r, d, f in os.walk(thisdir):
  #   for dirfile in f:
  #     if dirfile.endswith(ext0) and (file_extension=='.txt' 
  #        or file_extension=='.docx'):
  # ... as follows.
  ############################################################
  while filesFlag == 0:  # File state/flag is 1 in case of dataset files are present/copied in the current directory 
    #for item in range(1, 2):
     if (file_extension=='.txt' or file_extension=='.docx' or file_extension=='.bin') and filesFlag==0: 
          # print(os.path.join(r, dirfile))
          print(Fore.LIGHTYELLOW_EX + f'1- A {file_extension} file chosen to analyze:', thisfile)
          print('2- Temporarily read text file content available...')
          # print(os.path.join(r, dirfile))
          # csv_analyzer()
          file = open(thisfile, 'r', encoding='utf-8')
          content= file.read()
          print(fg.black+bg.lightgrey + content+ Back.RESET)
          print(Fore.LIGHTYELLOW_EX + 'Select another file for r-w analysis:...'), sleep(2.1)
          file_reader()
          print("Textual data to read...")
          filenum_call()
          filesFlag==0
          break
     elif (file_extension=='.png' or file_extension=='.jpg') and filesFlag==0:
          print(Fore.LIGHTYELLOW_EX + f'1- A {file_extension} file chosen to analyze:', thisfile)
          print('2- Temporarily image file content available...')
          # print(os.path.join(r, dirfile))
          pngfile=Path(f'{thisfile}').stem
          with open(thisfile, 'r') as x:
               subprocess.call(f'{pngfile}.png', shell=True)
               subprocess.call(f'{pngfile}.jpg', shell=True)
          file_reader()
          filenum_call()
          print("Image file to view...")
          filesFlag==0
          break
     elif file_extension=='.csv':
          print("*.csv being read for analysis...")
          csv_analyzer()
          filesFlag==1
          break
        
def __next__():
    while True:
         if keyboard.is_pressed("n"):
              print('Next...')
              sys.stdout.flush()
              break
         '''This flushed out the buffered keystrokes of character 'n' from memory 
            when key pressed by user continuously up to after reaching the 'Next...' 
            printout message displayed on screen...'''     

file_ext_call() # Call this function to setup and reconfigure r/w switches on 
                # the selected dataset file (file-extension based).  

print('Next data item...')
prompt()

def dataframe():
  global sample_data, df, df2, dfMin
  ####################################################################
  # Setting up the the first dataframe classification and analysis of
  # maximum and minimum P's on the selected file (dataset) by the user. 
  # This step is executed prior to a deeper analysis for QFLCA and QDF 
  # circuit's dataset.
  ####################################################################
  sample_data = np.genfromtxt(fileresult[idx-1], delimiter=',', skip_header=1) #, dtype=(None, str)) 
  #, skip_header=True) #, dtype=None) # Attributes to expand dataframe classification and analysis. 
  print("========================================================================")
  print (bg.orange + fg.black +"Min value element of Table: ", sample_data.min(axis=0)[1])
  
  df = pd.read_csv(fileresult[idx-1]) 
  print(df.iloc[0,0:3]) # Classified data from the dataframe df.
  print("========================================================================")
  print ("Max value element of Table: ", sample_data.max(axis=0)[1]) # Second csv column values are compared.
  df.max(axis=0)[1] # Will return max value of each column.
  
  # Using DataFrame.query() method...
  df2 = df.query('probability == probability.max()')
  print("Max P with its qubit/cbit list element:", df2)
  
  dfMin = df.query('probability == probability.min()')
  print("Min P with its qubit/cbit list element:", dfMin)
  
  for row in sample_data:
        if row[1] == sample_data.max(axis=0)[1]: #'0.67578125 from e.g., QFLCA_02 csv file':
              print(df2, row[1])

dataframe()

def PAnalysis():
#######################################
# P analysis of the selected dataset. #
#######################################
      global df2, df3
      if  (sample_data.max(axis=0)[1] < 0.5 and sample_data.max(axis=0)[1] > 0.2):  # Conditions to 
          # assign values to e.g., a weak classical min(∆P) = max(P) of a quantum outcome range (from 
          # the qubit dataset). Complement here is min(P) of the dataset if the user inputs for the opposition. 
           df2=df.loc[((df['probability'] < 0.5) & (df['probability'] > 0.27)), :].binary_string[:]
           df3=df.loc[((df['probability'] < 0.5) & (df['probability'] > 0.27)), :].probability[:] # Classify 
           # in the given included range of n:m
      elif (sample_data.max(axis=0)[1] < 1 and sample_data.max(axis=0)[1] >= 0.5):  # Conditions to assign values 
            # to e.g., a strong classical max(∆P) = min(P) of a quantum outcome range (from the qubit dataset). 
            # Complement here is max(P) of the dataset if the user inputs for the opposition.
           df2=df.loc[((df['probability'] < 1) & (df['probability'] >= 0.5)), :].binary_string[:]
           df3=df.loc[((df['probability'] < 1) & (df['probability'] >= 0.5)), :].probability[:]

def qdf_PAnalysis():
 global qdf, bitpair, df2bin, df3Mem, dfcomp, bitcomp # Main global variables to compute classical bit and qubit P's.
 if (sample_data.max(axis=0)[1] < 1):             
    PAnalysis() 
    print(Fore.GREEN + Back.RESET + 'Strong Prediction binary string is: ' + Fore.YELLOW,  
          df2.to_string(index=False, header=False) + Fore.GREEN + ', with a P value of' 
          + Fore.YELLOW, df3.to_string(index=False, header= False)) 
    df3Mem =df3.to_string(index=False, header= False)
    ### 
    df2bin= df2.to_string(index=False, header=False)
     
    qdf0=[df2bin[i:i+2] for i in range(math.floor(len(df2bin)/2)-1, math.ceil(len(df2bin)), 2)] # Use this formula 
    # to satisfy conditions of relevant outer binary string relative to central bit-pair according to Eq. (20) or 
    # Ref. [1] of the current Elsevier J. paper (given your/the QDF circuit design)...
    qdf1=[df2bin[i:i+2] for i in range(math.floor(len(df2bin)/2), math.ceil(len(df2bin)), 2)]
    qdf2=[df2bin[i:i+2] for i in range(math.floor(len(df2bin)/2)-1, math.ceil(len(df2bin)), math.floor(len(df2bin)/2))]
    
    qdf= qdf0 or qdf1 or qdf2 # Dynamic assignment of either df2bin range.

    if len(df2bin) <= 6 and qi_f == 1: # This if statement is designed to analyze QI dataset. One or more if statements 
         # needed to be added for IBMQ or different circuit/dataset configurations with their recorded binary strength 
         # lengths in their tables (their *.csv structure).
         print(Fore.GREEN + 'Paired qubit (left list element) relative to classical bit output (right list element): '
               + Fore.YELLOW, qdf0)
         qdf= qdf0  # Assign resultant value of qdf0 to qdf.  
    elif len(df2bin) > 6 and qi_f == 1: 
         print(Fore.GREEN + 'Paired qubit (left list element) relative to classical bit output (right list element): '
               + Fore.YELLOW, qdf1)
         qdf= qdf1  # Assign resultant value of qdf1 to qdf.
    else:  # Depending on QDF circuit design and configuration, more elif statements can be added to suit a bit-pair 
           # count and string foci as the one designed under IBMQ platform compared to QI (or QInspire) platform.    
         print(Fore.GREEN + 'Paired qubit (left list element) relative to classical bit output (right list element): '
               + Fore.YELLOW, qdf2) # Focus on the maximum from the middle qubit pair, if we put i+3, is to denote 
               # a pair + 1 qubit denoting up to three particles involved e.g. a photon Alice, Bob and the prize entangled. 
               # Iterate over a range of bins that are multiples of 2 (i.e. the size of the split substrings) for row in sample_data:
         qdf= qdf2  # Assign resultant value of qdf2 to qdf. 
  
    if dir_flag == 0:
         prompt() 
    else:  # Maintain a restricted yet error tolerant safe mode environment for the user to select a dataset file form directory. 
         print(Back.LIGHTGREEN_EX + Fore.YELLOW + 
             "\033[1m<--- SAFE MODE DATASET ANALYSIS CONTINUES --->\033[0m" + Back.RESET), sleep(2)
         print(f"{fg.lightgreen}Press any key to continue...")
         sys.stdout.write('SM:>>...')
         sys.stdout.flush()
         os.system("pause >nul")
    #########################################################################################
    # This part of the function prints the expected measurement output for different cases 
    # on qubit pairs. 
    #########################################################################################
    print(Fore.RED + f'\x1B[1;4mNotes:\033[0m\n' + Fore.CYAN + f'-* When shown in histograms generated from quantum circuit, \
the rightmost bit is for the measured qubit with the lowest index (q[0]). The leftmost bit is for the qubit with the highest index \
as the most significant qubit.\n-* Measurement focuses on QDF circuit bit pairs given the circuit configuration \
== focus on the maximum from the middle qubit pair in a list of measurement results. The program loop iterates over a range of \
bins that are multiples of 2 (i.e. the size of the split substrings) for row in sample_data...'+ Fore.YELLOW) 
    df2list = qdf0 or qdf1 or qdf2 
    qubit_print=''
    if '01' in df2list[:-1]: # Print the verdict on the one element prior last.
          print(fg.yellow+'{P_|01>b(01)} = 1 == ES')
          qubit_print='{P_|01>b(01)} = 1 == ES'
    if '00' in df2list[:-1]: 
          print(fg.yellow+'{P_|00>b(00)} = 0 == GS')
          qubit_print='{P_|00>b(00)} = 0 == GS'
    if '10' in df2list[:-1]:
          print(fg.yellow
                +f"{'{P_|10>b(10)} = 2 == ES within GS (QPT) or prize with lesser E value == some E loss or gain for Bob == uncertain or certain by swap gate when Eve reveals prize state':<40}")
          qubit_print=f"{'{P_|10>b(10)} = 2 == ES within GS (QPT) or prize with lesser E value == some E loss or gain for Bob == uncertain or certain by swap gate when Eve reveals prize state':<40}"
    if '11' in df2list[:-1]:
          print(fg.yellow+'{P_|11>b(11)} = 3 == superposition or prize state entangled with Alice or Bob')
          qubit_print='{P_|11>b(11)} = 3 == superposition or prize state entangled with Alice or Bob'
    if '0b' in df2list[:]: #or '1b' in df2list[:-1]:
          print(bg.orange + fg.lightgreen, qubit_print, Back.RESET + fg.lightgreen + "The binary string "+ Fore.YELLOW 
                + "\'..0b\' (classical bit)" + fg.lightgreen + " ends upon the least significant qubit (rightmost qubit).") 
    if '1b' in df2list[:]: 
          print(bg.orange + fg.lightgreen, qubit_print, Back.RESET + fg.lightgreen + "The binary string "+ Fore.YELLOW  
                + "\'..1b\' (classical bit)" + fg.lightgreen + " ends upon the least significant qubit (rightmost qubit).") 

    dfcomp = 1-df3  # Calculation of the P complement for the bitpair. 
    np.seterr(all="ignore") # Suppress irrelevant/outdated floating point numpy errors. 

    for bit in df2:
         if bit == "1":
             bit == "0"
         else:
             bit == "1"
    bitcomp = bit.replace("1", "2").replace("0", "1").replace("2", "0")

    if len(df2bin)>0 and qi_f==1: 
         # The following lines cover the bitpair property between the qdf0 to qdf1 or qdfn as assigned above (as replaced bits).
         index = 0 
         if qdf[index] == "01":   
                   bitpair = ["10"]
         if qdf[index] == "10": # We use the if statement rather than elif due to absolute conditions of the bitpair readout 
                                # from the dataset, according to above if-statements and for-loop.
                   bitpair = ["01"]
         if qdf[index] == "11":
                   bitpair = ["11"]
         if qdf[index] == "00":
                   bitpair = ["00"]
         if qdf[index] == "0b": # If classical state is = 0 in binary, result is conditioned to classical bit = 0. 
                   bitpair == "0"
         if qdf[index] =="1b": # If classical state is = 1 in binary, result is conditioned to classical bit = 1. 
                   bitpair == "1"
 
         print(fg.green+"Complement of the binary string is:"+fg.yellow, bitcomp, fg.green+", and the focused pair in it "
               +fg.yellow, bitpair, fg.green+"has a P' value of"+ Fore.LIGHTRED_EX, dfcomp.to_string(index=False, header=False))
 else: 
    print(fg.red+'Erroneous or Tied P values!') 
    subprocess.run(["python", "QAI-LCode_QFLCC.py"])  # Restart program. 

 """ Complex code alternative for the line:
 if len(df2bin)>0 and qi_f==1:
          bitpair = [bitcomp[i:i+2] for i in range(math.floor(len(bit)/2)-2, math.floor(len(bit)/2), 2)] # This line covers the 
                    # bitpair property between the qdf0 to qdf1 or qdfn as assigned above.
          index = 0 
          #bitpair = [qdf[index]] # Invert the bitpair result from the past do to compare with the last bitpair result when needed.
          #while index <= len(bitpair):
 elif len(df2bin)<=6 and qi_f==1: 
          bitpair = [bitcomp[i:i+2] for i in range(math.floor(len(bit)/2)-1, math.floor(len(bit)/2), 2)] # This line covers the 
                    # bitpair property between the qdf0 to qdf1 or qdfn as assigned above.
          print(fg.green+"Complement of the binary string is: "+fg.yellow, bitcomp, fg.green+", and the focused pair in it "
                 +fg.yellow, bitpair, fg.green+"has a P' value of"+ Fore.LIGHTRED_EX, dfcomp.to_string(index=False, header=False)) """
 
 if dir_flag == 1: # Maintain a restricted yet error tolerant safe mode environment for the user to select a dataset file form directory. 
     print(Back.LIGHTGREEN_EX + Fore.YELLOW + 
           "\033[1m<--- SAFE MODE DATASET ANALYSIS CONCLUDED --->\033[0m" + Back.RESET+ fg.lightgreen), sleep(2)

qdf_PAnalysis()   # Call the qdf_PAnalysis function. 
dfcompMem = float(dfcomp.to_string(index=False, header=False)) # Convert the string representation of string to float for
            # future use/comparison/validation.
filesFlag==1 # This file state denotes all dataset files are present within this directory. 
             # No need to overwrite in case of program restart. 
prompt()

def safeMode_dir():
  ###############################################################################
  # Directory function restricted to select a different file by the user
  # for analysis in a restricted yet safe mode environment.  
  ###############################################################################  
  global dir_flag # Flag is set to 1 for dataset directory access in safe mode. 
  global dfcompMem # Recall and reuse as global from PAnalysis() results.    
  if dir_flag == 1:
       print(Back.LIGHTGREEN_EX + Fore.YELLOW + 
             "\033[1m<--- SAFE MODE DIR ENVIRONMENT ENABLED --->\033[0m" + Back.RESET), sleep(2)
       filesFlag = 0
       file_reader()  # Execution flow of functions with dir and file flag settings
                      # must run sequentially...
       filenum_call()
       #filesFlag = 0
       filesFlag = 0
       with alive_bar(4, bar = 'blocks', manual=True) as bar:  # Print progress bar per Safe Mode step.
                                                             # Enables multiprocessing when needed. 
        csv_analyzer()
        bar(.2)
        file_ext_call()
        bar(.3)
        dataframe()
        bar(.7)
        qdf_PAnalysis()
        bar(.9)
        dfcompMem = float(dfcomp.to_string(index=False, header=False)) # Convert the string representation 
             # of string to float for future use/comparison/validation.
        #filesFlag==1 # This file state denotes all dataset files are present within this directory. 
             # No need to overwrite in case of program restart or in safe mode (SM)... 
        bar(1)
        ###  Progress concluded on the selected file by user and its preliminary anlysis. ####
       #dir_flag == 0 # Reset flag until next time requested by the user to access dataset files.
       #prompt()
       #PAnalysis_model() # Continue IBM QDF circuit simulation comparison of its dataset with the selected one.     
  else:
       print(Back.LIGHTGREEN_EX + Fore.YELLOW + 
             "\033[1m<--- SAFE MODE DIR ENVIRONMENT DISABLED --->\033[0m" + Back.RESET), sleep(2)
       """- End of safeMode_dir function calls """

def sim_log():
 ######################################
 # To log simulation checkpoints/steps
 ######################################
 global entry_stage
 
 entry_stage += 1
 idxplus = len(res) + entry_stage
 subprocess.run("echo {}- Checkpoint logged on {} for file # {}\
 as {} parallel to simulation run file {{ QDF-LCode_IBMQ-2024-codable }}, \
 Simulation State ///--{}--///".format(idxplus, now.strftime("%Y-%m-%d %H:%M:%S"), 
                                       idx, fileresult[idx-1], sim_state), shell=True, stdout=file_)
 """End of simulation log."""

def PAnalysis_model():
 ########################################################################################################################
 #--- This function compares the mapped results between QDF circuits (IBMQ <--> QI). 
 #--- SAFE MODE QFLCC AND, 
 #--- QDF Circuit Model from IBMQ article file: QDF-LCode_IBMQ-2024-codable.py, 
 # for python library purposes imported as a module:
 #--- QDF-LCode_IBMQ-2024.py (same code content as a duplicate of QDF-LCode_IBMQ-2024-codable, but will be overwritten 
 # by IBMQ folder content if you modify or update code. Only edit code within the QDF-LCode_IBMQ-2024-codable.py file!).
#########################################################################################################################
 global sim_state, dir_flag, entry_stage, hline 
 sim_state = ['']
 hline = "=================================================================================================================================="
 print(f'''{Fore.LIGHTMAGENTA_EX + hline}\n An ideal QDF circuit I/O model running realtime producing an IBMQ-based QDF dataset is from the \
 \n QDF-LCode_IBMQ-2024.py file. This circuit is compared to the analyzed dataset to show how close \
 \n the match is for a desired Hamiltonian and expected measurement outcome as a point of reference.\
 \n{hline}''')
 #---------------------------------------------------------------------------------------------------
 # <----- Display histogram results of the QDF circuit event P's and then printing the circuit 
 # as a model to display for QDF datasets of other circuits being analyzed here (next version will).
 # Future release will have current P results of QInspire or any other QDF circuit configure the 
 # IBM-QDF circuit through a QAI mapping, accordingly (subject of QAI lab for QFLCA) ----->
 #---------------------------------------------------------------------------------------------------
 P = 1 # The total probability of QDF circuit events relative to classical states or 
       # denoting the system's Hamiltonian (total energy). 
 with alive_bar(3, bar = 'blocks', manual=True) as bar:   #To print progress bar on these dataset and circuit simulation analyses.
    print(Fore.LIGHTMAGENTA_EX + Back.LIGHTGREEN_EX+ f"Please Wait!...:")
    print(f"*- Program is processing the analyzed dataset circuit P's after:"+Back.RESET), sleep(1)
    bar(0.5)
    print(f"{Back.LIGHTGREEN_EX}*- Import + Simulate the IBM QDF circuit by\
 {{ Qiskit Aer Simulator, IBMQ Provider }} [QUANTUM MODE ENVIRONMENT] on this computer."+Back.RESET), sleep(1)
    bar(0.7)
    print(f"{Back.LIGHTGREEN_EX}*- Dataset P results are compared on the imported circuit by the {{ QDF-LCode_IBMQ-2024.py }} module\
 on this computer [SAFE MODE ENVIRONMENT]."+ Back.RESET + Fore.LIGHTMAGENTA_EX), sleep(1)
    bar(1.)

 # Log the start of simulation. 
 entry_stage = 0
 sim_state[0] = " QDF CIRCUIT SIMULATION BEGINS "
 sim_log() 
 #---------------------------------------------------------------------------------------------------------------------
 ibm_qdf_module = importlib.import_module("QDF-LCode_IBMQ-2024-codable") # Unconventional call from the targeted module.      
 bar(1.)
 #---------------------------------------------------------------------------------------------------------------------
 # Log the prompt of simulation to the user to proceed, restart or exit program.
 entry_stage = 1  
 sim_state[0] = " QDF CIRCUIT SIMULATION_DATASET_ANALYSIS PROMPT "
 sim_log()  
 #-------------------------------------------------------------------------------------
 # Selected dataset and the simulated circuit's dataset validation verdict starts here, 
 # if user enters 'n' or 'next'... 
 # ------------------------------------------------------------------------------------
 print(Fore.LIGHTGREEN_EX + f"*- Enter 'n' or 'next' to proceed calculating P's between the selected dataset and the simulated\
 IBM QDF circuit results.") 
 print(f"🛈 {Fore.LIGHTMAGENTA_EX}\x1B[1;4mThe datasets of the two QDF circuits are compared and validated with a verdict on how\
 close their projection of \n events (prediction) is, given their QDF circuit configuration!\033[0m")
 print(f"{Fore.LIGHTGREEN_EX}*- ✅ Enter 'dir' or 'sm dir' to select another dataset to analyze in Safe Mode (SM:>>).\
 SIMULATION WILL NOT RESTART!") 
 print(f"{Fore.LIGHTGREEN_EX}*- ✅ Enter 'n' or 'next' to continue in Safe Mode (SM:>>).\
 QDF CIRCUITS SIMULATION_DATASET_ANALYSIS WILL START!")
 print(f"{Fore.LIGHTGREEN_EX}*- Enter any other key to change from SM:>> to regular prompt mode (>).")
 print(f"*- Enter 'r' in regular prompt mode (>) to 'restart' circuit simulation and dataset analysis. Enter 'h' for more options.")

 sm_input = input(f"SM:>> {fg.yellow}")
 if sm_input == "dir" or sm_input == "sm dir":
      dir_flag = 1 # Directory flag is set to 1 for directory access in safe mode. 
      safeMode_dir()
      pass
 elif sm_input == "n" or sm_input == "next":
      dir_flag = 1
      print(f"{Fore.LIGHTGREEN_EX}SM:>>{fg.yellow} Next..."), sleep(1)
 else:
      dir_flag = 0  # Directory flag is set to 0 in case of regular prompt mode (>) or 'r' to restart the simulation. 
      prompt()

 print(Back.LIGHTGREEN_EX + Fore.YELLOW + "\033[1m<--- QDF CIRCUITS SIMULATION_DATASET_ANALYSIS BEGINS --->\033[0m" + Back.RESET)

 ibmq_result = 'ibm-qdf-stats.txt'
 with open(ibmq_result, 'r') as file:    
        # Read the contents of the file
        content = file.read()
        
        # Extract all the p values from the content as float.
        N = re.findall(r'[-+]?(?:\d*\.*\d+)', content) 
        n_list = list(map(float, N)) 

        # Convert all the metadata digits to str to sort out binaries.
        bin_list = list(map(str, N))  # This is to identify qubit binary strings. 

        # Calculate quantum event p's for the total P.
        P = n_list[0]  # The P result is stored to the p_list.
        p1 = n_list[1] # 1st p result is stored to the p_list.
        pq1 = bin_list[4]
        p2 = n_list[2] # 2nd p result is stored to the p_list.
        pq2 = bin_list[5]
        p3 = n_list[3] # 3rd p result is stored to the p_list.
        pq3 = bin_list[6]

 ibmq_p_max = max(p1, p2, p3)  # Identify the max value from the p list.
 max_p_index = n_list.index(ibmq_p_max) # Store the index value for p_max from the ibmq_result file.

 ibmq_p_min = min(p1, p2, p3)  # Identify the min value from the p list.
 min_p_index = n_list.index(ibmq_p_min) # Store the index value for p_min from the ibmq_result file.
 
 # Set the default p color codes to 'white' as defined below in the p_color list until an if condition applies.
 p_color = [Style.BRIGHT + Fore.WHITE, Style.BRIGHT + Fore.WHITE, Style.BRIGHT + Fore.WHITE,
            Style.BRIGHT + Fore.WHITE, Style.BRIGHT + Fore.WHITE]
 
 if round(p1, 2) <= round(ibmq_p_min, 2): # Classify/color code min(p1).      
      p_color[0] = Style.BRIGHT + Fore.RED 
 if round(p2, 2) <= round(ibmq_p_min, 2): # Classify/color code min(p2). 
      p_color[1] = Style.BRIGHT + Fore.RED
 if round(p3, 2) <= round(ibmq_p_min, 2): # Classify/color code min(p3). 
      p_color[2] = Style.BRIGHT + Fore.RED
 if round(p1, 2) >= round(ibmq_p_max, 2): # Classify/color code max(p1).      
      p_color[0] = Style.BRIGHT + Fore.CYAN
 if round(p2, 2) >= round(ibmq_p_max, 2): # Classify/color code max(p2). 
      p_color[1] = Style.BRIGHT + Fore.CYAN
 if round(p3, 2) >= round(ibmq_p_max, 2): # Classify/color code max(p3). 
      p_color[2] = Style.BRIGHT + Fore.CYAN

 print(f"{Fore.LIGHTMAGENTA_EX}{hline}\nPlot = [{Fore.LIGHTGREEN_EX}P samples of the IBMQ model circuit,\
 if meets {Fore.LIGHTYELLOW_EX} ∝ {Fore.LIGHTGREEN_EX} p of the selected dataset file\
 {{ {Fore.LIGHTYELLOW_EX + fileresult[filenum-1] + Fore.LIGHTGREEN_EX} }}\non pairwise \
 qubits{Fore.LIGHTMAGENTA_EX}]...\nThen a strong vs weak p match, and the distance between QDF circuit events\
 are determined.{Fore.YELLOW}* {Fore.LIGHTGREEN_EX}\n{hline}{Fore.LIGHTGREEN_EX}\
 \n{Fore.YELLOW}* Computation model:{Fore.GREEN} κ Scalar ΨΦ Field Switch and Correlation Model, Ref. [1] of the DIB article.\
 \n  {Fore.LIGHTCYAN_EX}P(Ψ ⟷  κ²Ψ) = ⟨P(Ψ ⟷ Φ)⟩ = P(b|ij⟩); |ij⟩ ≡ |q_i q_j⟩ ≡ |qᵢqⱼ⟩. {Fore.GREEN}\
 \n{hline}"), sleep(0.5) 

 print(f'''{Fore.LIGHTMAGENTA_EX}\n\033[4m<-- P Sampling between IBM QDF Circuit and the Selected QDF Circuit Dataset -->\033[0m''')
 if dir_flag == 1:  # Read and display the printed circuit when dataset dir is in SAFE MODE.
       with open("ibm-qdf-circuit_output.bin", 'r', encoding='utf-8') as file_to_read:
            print(f'{fg.black}{bg.lightgrey}\n'+file_to_read.read(),"\n<-- IBM QDF Circuit Sample Printed in SAFE MODE --> "
                  + Back.BLUE + str(datetime.datetime.now()) + Back.RESET)
            file_to_read.close() # End reading and displaying the printed circuit.
 print(f'''{Fore.LIGHTMAGENTA_EX}\n\033[4m<-- P Results Sampled from {{ {ibmq_result} }} file are: -->\033[0m''')
 with alive_bar(3, bar = 'blocks' , manual=True) as bar:
  model_fig = tpl.figure() # Now plot histogram with horizontal bars for the computed probabilities.
  model_fig.barh([P, p1, p2, p3], [Style.BRIGHT + Fore.LIGHTGREEN_EX+"P(Total)", p_color[0]+f"ibmq qdf p({bin_list[4]})",  
                             p_color[1]+f"ibmq qdf p({bin_list[5]})", p_color[2]+f"ibmq qdf p({bin_list[6]})"], 
         force_ascii=False), sleep(1) 
  model_fig.show(), sleep(1)
  print('')
  bar(1)
  dir_flag = 0 # Reset flag until recalled.
  qdf_bit_pairs = ['',''] # To register which qdf_bit_pair has the max or min p.  
  #-------------------------------------------------------------------------------------
  # Now classify and print which sampled qdf_bit_pair set from the 
  # ibmq_result file is max_p and which min_p. 
  if min_p_index == 1:
   qdf_bit_pairs[0] = pq1
  if min_p_index == 2:
   qdf_bit_pairs[0] = pq2  
  if min_p_index == 3:
   qdf_bit_pairs[0] = pq3
  if max_p_index == 1:
   qdf_bit_pairs[1] = pq1
  if max_p_index == 2:
   qdf_bit_pairs[1] = pq2  
  if max_p_index == 3:
   qdf_bit_pairs[1] = pq3

 print(Fore.YELLOW+f'{hline}') 
 print(fg.purple+f'*- min(P) from {{ {ibmq_result} }} is performed by the QDF bit pairs\
 {{ {fg.red+ qdf_bit_pairs[0] +fg.purple} }} as {{ ibm qdf }} sample set {fg.yellow}#{min_p_index} = {ibmq_p_min}') 
 print(fg.purple+f'*- max(P) from {{ {ibmq_result} }} is performed by QDF bit pairs\
 {{ {fg.lightgreen+ qdf_bit_pairs[1] +fg.purple} }} as {{ ibm qdf }} sample set {fg.yellow}#{max_p_index} = {ibmq_p_max}') 
 print(Fore.YELLOW+f'{hline}') 
 #-----------------------------------------------------------------------------------------------------------
 # Recall and store which binary string had the minimum P from the table of the selected dataset (dataframe).
 global df_min, df_min_bin  
 if  (sample_data.min(axis=0)[1] < 1):  
           df_min=df.loc[(df['probability'] <= sample_data.min(axis=0)[1]), :].binary_string[:]
           df_min_bin = df_min.to_string(index=False, header=False) 
 #-----------------------------------------------------------------------------------------------------------
 deltaMatch_max = (1 - abs(ibmq_p_max - float(df3Mem)) ) # Calculate Δp of max(P) Match. 
 deltaMatch_min = (1 - abs(ibmq_p_min - sample_data.min(axis=0)[1]) ) # Calculate Δp of min(P) Match. 
 delta_p_min = abs(ibmq_p_min - sample_data.min(axis=0)[1]) # Calculate Δp of min(P).  
 delta_p_max = abs(ibmq_p_max - float(df3Mem)) # Calculate Δp of max(P).  
 
 Valid_Verdict = ['Weak',f'{{∞ , ⁿ/ₐ}}', 'Avg.', 'Strong', '␀']  # Validation Verdict of a strong
                                                              # vs. weak correlation match between 
                                                              # the selected file dataset p's and the IBM QDF 
                                                              # circuit event p's... 
 # Note: A verdict of ␀ denotes missing information or unknown about the max or min of the p's 
 # (calculable if config is corrected or complemented).
  
 if round(deltaMatch_max, 2) >= 0 and round(deltaMatch_max, 2) < 0.5: # Classify/color code max Δp match.      
      p_color[3] = Style.BRIGHT + Fore.RED
      Valid_Verdict = Fore.LIGHTRED_EX + Valid_Verdict[0] 
 
 if round(deltaMatch_max, 2) >= 0.5 and round(deltaMatch_max, 2) <= 0.55: # Classify/color code max Δp match.      
      p_color[3] = Style.NORMAL + fg.silver
      Valid_Verdict = Fore.LIGHTWHITE_EX + Valid_Verdict[1] 

 if round(deltaMatch_min, 2) >= 0 and round(deltaMatch_min, 2) < 1/3: # Classify/color code min Δp match.      
      p_color[4] = Style.BRIGHT + Fore.RED
      Valid_Verdict = Fore.LIGHTRED_EX + Valid_Verdict[0] 
 
 if (round(deltaMatch_min, 2) <= 1/3 and 
     round(deltaMatch_max, 2) <= 1/3) or (round(deltaMatch_min, 2) <= 1/2 and 
                                          round(deltaMatch_max, 2) <= 1/2): # Classify/color code min-max Δp match.      
      p_color[3] = Style.NORMAL + fg.silver
      p_color[4] = p_color[3]
      Valid_Verdict = Fore.LIGHTWHITE_EX + Valid_Verdict[1] 

 if round(deltaMatch_max, 2) > 0.55 and round(deltaMatch_max, 2) < 0.66: # Classify/color code max Δp match.      
      p_color[3] = Style.BRIGHT + Fore.LIGHTYELLOW_EX
      Valid_Verdict = Fore.LIGHTYELLOW_EX + Valid_Verdict[2] 
      
 if (round(deltaMatch_max, 2) >= 0.66 and 
     round(deltaMatch_max, 2) < 0.9) and (round(deltaMatch_min, 2) >= 0.66 and 
                                          round(deltaMatch_max, 2) < 0.9): # Classify/color code min-max Δp match.       
      p_color[3] = Style.BRIGHT + Fore.LIGHTMAGENTA_EX
      p_color[4] = p_color[3]
      Valid_Verdict = Fore.LIGHTCYAN_EX + 'Above ' + Valid_Verdict[2] 

 if (round(deltaMatch_max, 2) >= 0.9 and 
     round(deltaMatch_max, 2) <= 1) and (round(deltaMatch_min, 2) >= 0.9 and 
                                          round(deltaMatch_max, 2) <= 1): # Classify/color code min-max Δp match.      
      p_color[3] = Style.BRIGHT + Fore.LIGHTGREEN_EX 
      p_color[4] = p_color[3]
      Valid_Verdict = Fore.LIGHTGREEN_EX + Valid_Verdict[3] 
 
 if (round(deltaMatch_min, 2) <= 1/3 and 
     round(deltaMatch_max, 2) <= 1/2) or (round(deltaMatch_min, 2) <= 1/2 and 
                                           round(deltaMatch_max, 2) <= 1/2): # Classify/color code min-max Δp match.      
      p_color[3] = Style.NORMAL + fg.silver
      p_color[4] = p_color[3]
      Valid_Verdict = fg.silver + Valid_Verdict[4] # See note for a ␀ verdict!

 PAnalysis_fig = tpl.figure() # Now plot histogram with horizontal bars for the computed probabilities of the two datasets.
 PAnalysis_fig.barh([P, float(df3Mem), float(dfcompMem), sample_data.min(axis=0)[1], ibmq_p_min, ibmq_p_max,  
                     delta_p_min, delta_p_max, deltaMatch_min, deltaMatch_max], 
     [Style.BRIGHT + Fore.LIGHTGREEN_EX + f"P(\x1B[4mTotal\x1B[0m{Style.BRIGHT + Fore.LIGHTGREEN_EX})", 
      f'{Style.BRIGHT+Fore.WHITE}{{ {fileresult[filenum-1]} }} max(P(\x1B[4m{df2bin}\x1B[0m{Style.BRIGHT+Fore.WHITE}))', 
      f'{Style.RESET_ALL + Fore.WHITE}{{ {fileresult[filenum-1]} }} comp(P(\x1B[4m{bitcomp}\x1B[0m{Style.DIM+Fore.WHITE}))', 
      Style.BRIGHT + Fore.WHITE + f"{{ {fileresult[filenum-1]} }} min(P(\x1B[4m{df_min_bin}\x1B[0m{Style.BRIGHT + Fore.WHITE}))",  
      f"{Style.BRIGHT +  Fore.YELLOW}{{ ibm qdf }} min((P(\x1B[4m{qdf_bit_pairs[0]}\x1B[0m{Style.BRIGHT + Fore.YELLOW})) ",
      f"{Style.BRIGHT +  Fore.YELLOW}{{ ibm qdf }} max((P(\x1B[4m{qdf_bit_pairs[1]}\x1B[0m{Style.BRIGHT + Fore.YELLOW})) ",
      p_color[4] + "Δp of \x1B[4mmin(P)\x1B[0m" + p_color[4], 
      p_color[3] + f"Δp of \x1B[4mmax(P)\x1B[0m" + p_color[3], 
      p_color[4]+ "Δp of\x1B[4m min(P) match\x1B[0m" + p_color[4], 
      p_color[3]+ "Δp of\x1B[4m max(P) match\x1B[0m" + p_color[3]], force_ascii=False), sleep(1)
 PAnalysis_fig.show()
 bar(1.)
 
 print(f"{Fore.LIGHTYELLOW_EX+hline+ Fore.LIGHTMAGENTA_EX}\n*- Δp Data: ⚖️  \033[4mValidation Verdict\033[0m ⚖️{fg.yellow}  \
 between the two dataset samples from {fg.cyan}{{ {fileresult[filenum-1]} , {ibmq_result} }}{fg.yellow} \
 \n   is a/an: \
\033[4m{Valid_Verdict + ' Match {{ '+ str(round(deltaMatch_min, 2)) +' , '+ str(round(deltaMatch_max, 2)) +' }}'}\033[0m\
{Fore.LIGHTYELLOW_EX}")
 
 DeltaP_verdict = Valid_Verdict
 Valid_Verdict = ['Weak',f'{{∞ , ⁿ/ₐ}}', 'Avg.', 'Strong', '␀']  # Reset Valid_Verdict list elements upon 
                                                                  # the previously rendered verdict. 
 #----------------------------------------------------------------------------------------------------
 # Validate circuit config. based on recorded P's associated to their qubit pair binaries (strings)
 s1 = df_min_bin
 s2 = qdf_bit_pairs[0]
 s3 = df2bin
 s4 = qdf_bit_pairs[1]
 vv_circuits =[False]  
 vv_bins = [False] 
 # Validation Verdict on the two circuits qubit string sets over min and max P's as compared for a match. 
 if re.match(s2, s1):
     vv_bins = fg.lightgreen+ Valid_Verdict[3]
     qdf_s_match = f"{{ {s1} , {s2} }}"
 elif re.match(s4, s3):
     vv_bins = fg.lightgreen + Valid_Verdict[3]
     qdf_s_match = f"{{ {s3} , {s4} }}"
 else:
     vv_bins = fg.red + Valid_Verdict[4] # See note for a ␀ verdict!
     qdf_s_match =  fg.red +  "P(b|ij⟩) Loop Lock" + fg.red # This is for a false match or loop lock cases. Added on Jul 07, 2024. 
     vv_circuits = fg.red + str(vv_circuits) + fg.red # For loop lock or impossible P cases. Added on Jul 07, 2024. 
     
 # Validation Verdict on the two circuits as compared for a config. match.  
 if (vv_bins == fg.lightgreen + Valid_Verdict[3]) and (DeltaP_verdict == Fore.LIGHTGREEN_EX + Valid_Verdict[3]):
     vv_circuits = fg.green + Valid_Verdict[3]
 if (vv_bins == fg.lightgreen + Valid_Verdict[3]) and (DeltaP_verdict == Fore.LIGHTGREEN_EX + Valid_Verdict[1]):
     vv_circuits = fg.yellow + Valid_Verdict[2]
 if (vv_bins == fg.lightgreen + Valid_Verdict[3]) and (DeltaP_verdict == Fore.LIGHTCYAN_EX + 'Above ' + Valid_Verdict[2]):
     vv_circuits = Fore.LIGHTCYAN_EX + 'Above ' + Valid_Verdict[2]
 if (vv_bins == fg.red + Valid_Verdict[4]) and (DeltaP_verdict == Fore.LIGHTGREEN_EX + Valid_Verdict[3]):
     vv_circuits = fg.yellow + Valid_Verdict[2]
 if ((vv_bins == fg.red + 
      Valid_Verdict[4]) or (vv_bins == fg.lightgreen + Valid_Verdict[3])) and (DeltaP_verdict == fg.silver + Valid_Verdict[4]):
      vv_circuits = f'{{ {fg.lightred + Valid_Verdict[4]} , {False} }}' # A ␀ or false match verdict! See also next line/condition.
 if (float(df3Mem) <= 1/3 and sample_data.min(axis=0)[1]<= 1/3) and (ibmq_p_max >= 1/2):
     vv_circuits = f'{fg.lightred}{{ {Valid_Verdict[4]} , {fg.yellow}{Valid_Verdict[1]}{fg.lightred} }}' # A ␀ match verdict! In short,
      # a state transition matrix with all elements between certain circuit components return a 0 state or null match and 
      # state 2 for one of the two circuits! See P's preliminary analysis for the measured QDF circuit. 
      # This circuit event outcome can also be interpreted as a rejected match between the two circuits, based on their configuration.  
 if (vv_bins == fg.red + Valid_Verdict[4]) and (Valid_Verdict == Fore.LIGHTYELLOW_EX + Valid_Verdict[2]):
     vv_circuits = fg.red + Valid_Verdict[2]
 #----------------------------------------------------------------------------------------------------
 print(f"\033[1m{Fore.LIGHTYELLOW_EX+hline+ Fore.LIGHTMAGENTA_EX}\n*- QDF Qubit Sets: ⚖️  \033[4mValidation Verdict\033[0m ⚖️{fg.yellow}  \
 between the two dataset samples from {fg.cyan}{{ {fileresult[filenum-1]} , {ibmq_result} }}{fg.yellow} \
 \n   is a/an: \033[4m{vv_bins + ' Match ' + qdf_s_match}\033[0m {Fore.LIGHTYELLOW_EX}")

 print(f"\033[1m{Fore.LIGHTYELLOW_EX+hline+ Fore.LIGHTMAGENTA_EX}\n*- QDF Circuits: ⚖️  \033[4mValidation Verdict\033[0m ⚖️{fg.yellow}  \
 between the two QDF circuit configurations from {fg.cyan}{{ {fileresult[filenum-1]} , {ibmq_result} }}{fg.yellow} \
 \n   is a/an: \033[4m{vv_circuits} Match \033[0m {Fore.LIGHTYELLOW_EX}")

 # Log validation verdict results on simulation and dataset analysis.
 entry_stage = 2  
 sim_state[0] = f"Δp Data: {Valid_Verdict}, QDF Qubit Sets: {vv_bins + ' Match ' + qdf_s_match},  QDF Circuits: {vv_circuits} Match"
 sim_log()

 print(f"{hline + Fore.LIGHTMAGENTA_EX}\n *- The IBM QDF circuit can be reconfigured for worst and best case Hamiltonian scenarios,\
 \n    given the expected QDF measurement outcomes from the collected QFLCA datasets for a QFLCC.\
 \n\x1b[38;5;226m Simulation completed on: \033[1;32m{fg.yellow+bg.blue+str(datetime.datetime.now())+Back.RESET} \
 \n{hline + Fore.RESET}"), sleep(4)

 dir_flag = 0
 print(Back.LIGHTGREEN_EX + Fore.YELLOW + "\033[1m<--- QDF CIRCUITS SIMULATION_DATASET_ANALYSIS CONCLUDED --->\033[0m" 
       + Fore.LIGHTGREEN_EX + Back.RESET)
  
 # Log the end of simulation and dataset analysis.
 entry_stage = 3  
 sim_state[0] = " QDF CIRCUITS SIMULATION_DATASET_ANALYSIS CONCLUDED "
 sim_log()

PAnalysis_model()
'''
def safeMode_call ():
 if dir_flag == 0: 
    prompt()
 if dir_flag == 1:
    safeMode_dir()
    """- Safe Mode flag set to call one or more QFLCC functions."""
safeMode_call()'''
prompt()
#########--END OF QFLCC PROGRAM--#########

##################################################################################
# Alice & Bob's Quantum Doubles game starts from here to validate data results...
##################################################################################
__game_version__ = "ver.1.0"
__game_logo__="""
\033[92m  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
\033[92m ( o.o )( o.o )( o.o )( o.o )( x.x )( o.o )( o.o )( o.o )( o.o )( o.o )( x.- )( o.o )( o.o )( o.o )( -.- )
\033[92m  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
\033[92m  /\_/\  \033[96m    ___ __                   ___     ____         ___                                   \033[92m   /\_/\ 
\033[92m ( o.o ) \033[96m   / _ \\ \                 /   \   |  _ \       / _ \ //                               \033[92m   ( o.o )
\033[92m  > ^ <  \033[96m  | |_| |\ \  ___   _____   \ O /   | |_) ) ___ | |_) )/____                            \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m  |  _  | > \| \ \ / / __)  / _ \/\ |  _ ( / _ \|  _ < /  ._)                           \033[92m   /\_/\ 
\033[92m ( x.o ) \033[96m  | | | |/ ^ \ |\ v /> _)  ( (_>  < | |_) | (_) ) |_) | () )                            \033[92m  ( x.x )
\033[92m  > ^ <  \033[96m  |_| |_/_/ \_\_)> < \___)  \___/\/ |____/ \___/|  __/ \__/                             \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m    ____        / ^ \                           | |                _____                \033[92m   /\_/\ 
\033[92m ( o.x ) \033[96m   / __ \      /_/ \_\                          |/\               / _ \ \               \033[92m  ( o.o )
\033[92m  > ^ <  \033[96m  | |__| |_   _  __  ___  _____ _   _ _   _     /  \   ___  _   _| |_) ) \   ___ ____   \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m  |  __  | | | |/  \/ / |/ (   ) | | | | | |   / /\ \ / _ \| | | |  _ < > \ / __)  ._)  \033[92m   /\_/\ 
\033[92m ( o.o ) \033[96m  | |__| | |_| ( ()  <| / / | || |_| | |_| |  / /__\ ( (_) ) |_| | |_) ) ^ \> _| () )   \033[92m  ( -.x )
\033[92m  > ^ <  \033[96m   \____/ \___/ \__/\_\__/   \_)\___/| ._,_| /________\___/ \___/|  __/_/ \_\___)__/    \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m                                     | |                         | |                    \033[92m   /\_/\ 
\033[92m ( -.- ) \033[96m                                     |_|                         |_|                    \033[92m  ( o.o )
\033[92m  > ^ <  \033[96m  \033[91m v.1.0                                                                                \033[92m   > ^ < 
\033[92m  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
\033[92m ( o.x )( o.o )( o.o )( o.o )( -.- )( o.o )( o.o )( x.x )( o.o )( o.o )( o.o )( -.x )( o.o )( x.- )( o.o )
\033[92m  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
"""
###############################################################################
# Instantiating variables and constants of animated states of loser, winner, 
# dual(superposition), unknown. Alternatively, lists can be created in the 
# future tests after threads, timer or sleep() and subprocess runs for combined 
# datasets. For example, the constants excited1 and excited2 can be redefined 
# in a list as excited = [excited1, excited2], or by the removal of the two 
# constants hardcoding the emojis in excited = ["─=≡Σ((( つ◕ل͜◕)つ", 
# "─=≡Σ(((✌(✰ ͜ʖ ✰)✌ [✰]"] and later called for the participant's win, as 
# animated by the function winner_show() within its for-loop. 
###############################################################################
prize="[✰]"
alice="[♠]"
bob="[○]"
eve="[♣]"
audience="[♦]"
crownBob="♕💪🤴👍♕"
crownAlice="♔👸♔"
here="👇"
go="👉"

excited1 = "─=≡Σ((( つ◕ل͜◕)つ"
excited2 = "─=≡Σ(((✌(✰ ͜ʖ ✰)✌ [✰]"

grounded1= "─=≡Σ(((┏(° ʖ̯ ͡°)┛"
grounded2= "─=≡Σ(((┗(° ʖ̯ ͡°)┛"
grounded3= "─=≡Σ(((┏(╥ ʖ̯ ╥)┓"

dual3="─=≡Σ((👎 (11 ͜ʖ͠ 00)👍"
dual1="─=≡Σ((🖐 (10 ͜ʖ͠ 01)👍"
dual2="─=≡Σ((☝ (01 ͜ʖ͠ 10)🖐"

guesser1="─=≡Σ(((💪(◐ ͜ʖ͠◐ )👉"
guesser2="─=≡Σ(((☝(◐ ͜ʖ͠◐ )👍"
guesser3="─=≡Σ(((👉(❂ ͜ʖ͠❂ )👉[$̲̅ |"

classical1="─=≡Σ((🖐(° ͜ʖ ͡°)🖐"
classical2="─=≡Σ((👍(° ͜ʖ ͡°)👍"
classical3="─=≡Σ(((👉(❂ ͜ʖ͠❂ )👉[$̲̅ |"

errorP1=" ¯\_( ͠◐ ͜ʖ͠◐ )_/¯"
errorP2=" ¯\_( ͠◕ ͜ʖ͠◕ )_/¯"

aimTarget=" ||[̲̅$̲̅( ͡๑ ͜ʖ ͡๑)̲̅$̲̅]||"
helperTarget1=" |[✰]( ͡° ͜ʖ ͡°)[○]|"
helperTarget2=" |[♠]( ͡° ͜ʖ ͡°)[✰]|"
############################################################################################
# These are the QDF game description, logo and copyright details.
############################################################################################
__game_banner__ = """\n"\033[96m( ͡° ͜ʖ ͡°) vs ( ͡°( ͡° ͜ʖ ͡°(︡▧ ͜ʖ▧︠) ͡° ͜ʖ ͡°) ͡°) vs [̲̅$̲̅( ͡๑ ͜ʖ ͡๑)̲̅$̲̅]  vs ¯\_( ͠◐ ͜ʖ͠◐ )_/¯ vs \
─=≡Σ((( つ◕ل͜◕)つ [♥]]] [♦]]] [♣]]] [♠]]] ─=≡Σ(((✌(✰ ͜ʖ ✰)✌ ||||||||||||||||||||||| \033[92m"""
__game_description__= "Alice & Bob's Quantum Doubles... This QFLCC game version of the QAI-LCode is basic. \
More revisions to come, as the dataset grows on the number of trials on 1 or more QDF circuits for simulating. \
the QDF game. The QDF game simulates events of the dataset's quantum and classical parameters in observing a \
thermodynamic system = { QDF game environment and its participants Alice, Bob, Eve, Audience } based on Refs. [1-2,4] \
of the Data in Brief, Elsevier J article."
print(Back.RESET+fg.lightgreen,__game_logo__,__game_banner__ + __game_description__ , 
      Back.RESET+fg.silver+__game_version__,"\n"), sleep(2) 
"""- Colored banner to introduce the QDF game and its goal. These common constants and variables are
     frequently used during game play."""
entry_stage = 4 # Set this to 0 if the game is run as a separate file or program. 
dir_flag = 0 # Directory flag is set to 1 if dataset directory access is asked by user to analyze in safe mode. 

qdf_bits_flag = [False, False] # Flag state 0 == hide, 1 == show the qdf bit values from any dataset.
qdf_bits_flag[0] = False # By default set at least this flag to 0 == hide the qdf bit values from any dataset.

def qdf_bits_flagset(): 
 # A function to switch between states of 0 == hide and 1 == show for the qdf bit values of any dataset.
 global qdf, bitpair, qdf_bits_flag 
 if (qdf_bits_flag[0] == False) and (qdf_bits_flag[1] == False):
     qdf = '[##]' # Mask this qdf value in case of qdf_bits both flags are false. 
     bitpair = '[##]' # Mask this bitpair value in case of qdf_bits both flags are false. 
 if (qdf_bits_flag[0] == False) and (qdf_bits_flag[1] == True):
     qdf = qdf # Unmask this qdf value in case of qdf_bits 2nd flag is true. 
     bitpair = bitpair # Unmask this bitpair value in case of qdf_bits 2nd flag is true. 

def entry_add(): 
############################################################################################
# This function logs program events onto the stdout file
############################################################################################
     global entry_stage  # Redefine the entry count as global.
     entry_stage+=1
     idxplus = len(res)+entry_stage
     subprocess.run("echo {}- Checkpoint logged on {} for the QFLCC Game:\
 Alice and Bob's Quantum Doubles {}".format(idxplus, now.strftime("%Y-%m-%d %H:%M:%S"), __game_version__), 
 shell=True, stdout=file_)

entry_add()

##################################################################
# Initialize Pygame, then sound mixer to play introductory retro 
# music and welcome message sound files and create other windows 
# as a GUI.
##################################################################
from tkinter import *
import tkinter as tk
from itertools import cycle
import pygame  # To play music or sounds in the QDF game.

def flash_color(object, color):
    object.config(foreground = next(color), bg='black')
    root.after(100, flash_color, object, color)
""" Coloring the flash object from Pygame for the user's interface (UI)."""

pygame.init() 
pygame.mixer.init()

game_sound = pygame.mixer.Sound('__snd__/game_music2.wav')
game_sound.play(), sleep(2)
game_sound = pygame.mixer.Sound('__snd__/welcome2.wav')
game_sound.play()
""" Initialize pygame and sound mixer to play introductory retro 
music and welcome message sound files and other windows as a GUI."""

from PIL import Image, ImageTk
import tkinter.messagebox as msgbox 

def display_bye_msg():
    # Play Windows exit sound.
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    root.wm_attributes("-topmost", 1)
    root.withdraw() # Hide this form.
    bye = msgbox.askquestion(title=f"Alice & Bob's Quantum Doubles {__game_version__} Message", 
                             message = 'Are you sure you want to exit? If Yes, ...🖐 (° ͜ʖ ͡°)🖐 Goodbye!', 
                             icon = 'warning', parent=root)
    if bye == 'yes':
        game_sound = pygame.mixer.Sound('__snd__/goodbye1.wav')
        game_sound.play()
        Quit()
    else:
        root.wm_attributes("-topmost", 1)
        root.deiconify() # Unhide this form. 
    """Exit game if user chooses after the goodbye message."""

def flagClose():    
    root.withdraw() # Hide this form.
    root.quit() 
    #----------------------------------------------------------------------------------
    # Enable the next lines to destroy this form after quit (or by duration afterwards 
    # using sleep) as a permanent close solution. This is to not revisit the dataset(s) 
    # load & play root form, as it is already destroyed after t seconds!
    #----------------------------------------------------------------------------------
    #sleep(50)       # Dont close for t = 50 seconds, for example...
    #root.destroy()  # To destroy the root form. 
    """Quit or destroy the game app form and get back to CLI as user's interface. The quit
command gives user the illusion that the form is closed/gone, which in fact can be later 
called upon by the option 'form' from the terminal. """

def Quit():
     game_sound = pygame.mixer.Sound('__snd__/goodbye1.wav')
     game_sound.play()
     print(fg.black + Back.YELLOW +'\nExiting program...🖐 (° ͜ʖ ͡°)🖐  Goodbye!'+ Back.RESET), sleep(3)
     print(fg.yellow + Back.RED+"The QFLCC program is terminated!" + Back.RESET)
     sys.exit(1) # Force this in case of abnormal exit or program termination. 
"""Exit program and system with a message before the terminal."""

def Help():
     msgbox.showinfo(title='Input Tips', message='Input tips:\n \n-Enter \'n\' key or \'next\' for \
the next message or input. \n-Enter \'h\' or \'help\' to display these tips. \n-Enter the number \
for a game player role when prompted. \n-Enter a value between 0 and 1, or 0 or 1 for a P value. \
\n-Enter \'site\' or \'web\' to view \'about\' the game \'website\'. \
\n-Enter \'s\' or \'speed\' to change the speed of game steps. \
\n-Enter \'v\' or \'volume\' for sound volume change during play. \n-Enter \'cv\' for sound volume \
change within CLI. \n-Enter \'f\' or \'form\' to reload this form. \
\n-Enter \'dir\' or \'sm dir\' for a new dataset analysis & simulation to feed this game.*\
\n*-This command requires a passcode to see dataset results in a Safe Mode (SM:>>) environment!\
\n-Enter \'e\' or \'exit\' to exit the game.')
"""Helping tips to start the game by choosing participants and a P value, according to the QDF game model."""

def open_new_win():
   ##############################################################################
   # This function creates a new window based on the QDF game legend and rules. #
   ##############################################################################
   imagelist1 = ["game_legend.png"]
   photo = PhotoImage(file=imagelist1)
   width = photo.width()
   height = photo.height()
   fore_win=Toplevel(root)
   fore_win.wm_attributes("-topmost", 1) # these two lines will focus on the window not terminal 
   fore_win.focus_force()
   fore_win.title("Game Model Legend")
   fore_win.geometry("650x450")
   fore_win.configure(background='black')
   image = Image.open('game_legend.png').convert("RGB")
   resized = image.resize((550, 300),Image.LANCZOS) # Resize the image and antialias it from the uploaded file.
   display = ImageTk.PhotoImage(resized)
   label = Label(fore_win, image=display, background="black") # Display it within a label.
   legend_label = Label(fore_win, 
                        text=excited1+f' | Score = 10 points for {bob} or {alice} win {prize} via {eve} or {audience} \n'
                        + dual1+f' | Score = 3 points for {bob} via {eve}, or {alice}, \
superpose/entangle with {prize} between boxes \n'+ guesser3+f' Score = 2 points for {bob} or {alice} guess the {prize} \n'
                        +  grounded2+f' | Score = -5 points from {bob} or {alice} losing a/the {prize} \n'+ grounded3
                        +f' | Lose score < -9 points for {bob} or {alice} is game over \n'+ helperTarget1 
                        +f' | Score = 1 point for {bob} or {alice} guess the {prize}.  \n'+ crownBob+' | '+ crownAlice 
                        +f' | Score > 999 points for {bob} or {alice} is the final game win = level 8 complete.  \n' 
                        + alice + bob + eve + audience + prize +go 
                        +f' | Possible combination of doubles from selected dataset \
is = ' + buttonInvisible["text"] + '.\n', justify="left" , bg="black",  fg="lightgreen").pack() 
   label.image = display
   label.pack()
   # Set minimum the foreground window size value
   fore_win.minsize(650, 450)
   # Set maximum the foreground window size value
   fore_win.maxsize(650, 450)

win_min=0
def restart_QFLCC():
########################################################
# The following restarts QFLCC for choosing a dataset  #
########################################################
   global win_min
   #root.iconify()
   win_min == True
   flagClose() # An option to choose between destroying/quit the present form. 
   subprocess.run(["python", "QAI-LCode_QFLCC.py"])

##################################################################################
# Mimic an animated GIF displaying a series of GIFs an animated GIF was used to 
# create the series of GIFs with a common GIF animator utility. Buttons and usage 
# help options are appended and displayed at the end of log file and other game 
# file installation/download.
##################################################################################
from tkinter import ttk
import asyncio 

root = Tk()
# Adjust size...
width = 1550 # Width 
height = 600 # Height 
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate starting X and Y coordinates for the Window and apply to its dimensions (geometry).
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('+%d+%d' % (x, y))
root.wm_attributes("-topmost", 1) # These two lines will focus on the window not terminal. 
root.focus_force()

def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)  # This disables the [X] button on the root window to satisfy user's game options.
       # No matter how many times the user clicks on [X], nothing happens, and so is directed to other exit or resume game options. 

# Create a sprite bank (array list) to animate from files.
imagelist = ["__img__/logo_01.gif", "__img__/logo_01.gif", "__img__/logo_02.gif", "__img__/logo_02.gif", 
             "__img__/logo_02.gif", "__img__/logo_03.gif",  "__img__/logo_03.gif", "__img__/logo_04.gif", 
             "__img__/logo_05.gif", "__img__/logo_06.gif", "__img__/logo_06.gif", "__img__/logo_06.gif"]

# Create a sprite bank (array list) from the defined ASCII characters by their corresponding char variables. 
charslist = [f'{crownBob} | {dual1}' , f'{crownBob} | {dual1}', f'{crownBob} | {dual2}', 
             f'{crownBob} | {dual2}', f'{crownBob} | {dual3}', f'{crownBob} | {dual3},' f'{crownBob} | {excited1}', 
             f'{crownBob} | {excited1}', f'{crownBob} | {excited1}', f'{crownBob} | {excited2}', 
             f'{crownBob} | {excited2}', f'{crownBob} | {excited2}', f'{crownAlice} | {guesser1}', 
             f'{crownAlice} | {guesser1}', f'{crownAlice} | {guesser2}', f'{crownAlice} | {guesser2}', 
             f'{crownAlice} | {guesser3}', f'{crownAlice} | {guesser3}', f'{crownAlice} | {classical1}', 
             f'{crownAlice} | {classical1}', f'{crownAlice} | {classical2}', f'{crownAlice} | {classical3}', 
             f'{crownAlice} | {classical3}'] 
color_list = ["cyan", "yellow", "red", "yellow", "blue", "lightgreen"]

progressbar = ttk.Progressbar(length=750, style="green.Horizontal.TProgressbar")
progressbar.step(99.9) # Full progress bar...
progressbar.place(x=950,y=550, width=560)

root.minsize(1550, 600) # Set minimum window size value.
root.maxsize(1550, 600) # Set maximum window size value.
photo = PhotoImage(file = imagelist[0]) # Extract width and height info.
width = photo.width()
height = photo.height()

canvas = Canvas(width=width, height=height)
canvas.place(x=30, y=20) # Position the canvas for the gif image.

root.title(f"Alice & Bob's Quantum Doubles {__game_version__}")
root.configure(background='black')

filename='shell_output.txt'

def update_text():
   # Configuring the text in Label widget.
   my_label0.configure(text="Loading the game model and circuit. Click START to continue...")
   subprocess.call(['game_model.png'], shell=True)
   subprocess.call([f'{pngfile}.png'], shell=True)

def change_color():
   my_label0.config(bg= "gray51", fg= "red")

f = open("shell_output.txt", "r")
file_string = f.read()
schar = ' '
my_label0 = tk.Label(root, text =  __license__ + schar + __author__+ schar + __location__+','
                     + schar + __ORCID__+ schar + __copyright__+ schar + __version__
                     +"\n \n||||||||||||||||||||||||||||||||||||||||||||||||||\
|||||||||||||||--Reload Log_file--||||||||||||||||||||||||||||||||||||||||||||\
|||||||||||||||||||||||||||||\n \n"+str(file_string), fg="#000fff000", background="black", 
width=80, height =28, wraplength=525, anchor='n', justify="left")
my_label0.place(x=950, y=15)

# Create a list of image objects. 
giflist = [] # This is to store and run image sprite in .gif.
for imagefile in imagelist:
   photo = PhotoImage(file=imagefile)
   giflist.append(photo)
anim_label1 = tk.Label(root, text = '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .', 
                       fg="lightgreen" , background="black", width=80, height =2, wraplength=500, 
                       anchor="w", justify="left")
anim_label1.place(x= 950, y= 500)
anim_label0 = tk.Label(root, text = dual1, fg="cyan" , background="black", width=80, height=2, 
                       wraplength=500, anchor="w", justify="left")
anim_label0.place(x= 950, y= 500)

async def mainT():
  await asyncio.sleep(0.001)  # Sprite is updated every second and then other asynchronous updating tasks 
                              # take place in the outer loops. 

# Loop through the gif image objects for a while.
for j in range(0, 30):
    for gif in giflist:
        canvas.delete(ALL)
        canvas.create_image(width/2.0, height/2.0, image=gif)
        canvas.update()
        progressbar.step(j*5)
        anim_label0.place(x= 950+j*4, y= 500)
        #sleep(0.001) 
    for clr in color_list:
     for sprite in charslist:
          anim_label0.config(text=sprite+' . . . . . Loading . . .')
          anim_label0.update()
          #asyncio.run(mainT()) # Sprite is updated every second and then other asynchronous updating tasks 
                                # take place in the outer loops. 
          #asyncio.sleep(0.5)  
     anim_label0.config(fg=clr)
     anim_label0.update()
     sleep(0.02)

pygame.time.delay(2)

button0 = Button(root, text = 'START', bg='black', fg='white', command = flagClose)
button1 = Button(root, text = 'Input Tips', bg='black', fg='white', command = Help)
button3 = Button(root, text="QUIT", bg='black', fg='white', command = display_bye_msg)
button2 = Button(root, text="Show Game Model", bg='black', fg='white', command = open_new_win)
button4 = Button(root, text=f'Change Dataset: [##] vs Complement [##]', bg='black', fg='white', 
                 justify=LEFT, wraplength=160, command = restart_QFLCC)
buttonInvisible = Button(root, text=f'[##] vs its complement [##]', bg='black', fg='white', command = restart_QFLCC)
buttonInvisible.pack_forget() # This button remains invisible until made visible through .pack() command. 
button0.place(x=950, y=450, width=50)
button1.place(x=1010, y=450, width=80)
button2.place(x=1100, y=450, width=140)
button3.place(x=1250, y=450, width=80)
button4.place(x=1340, y=450, width=180)

def update_btn4_text(): 
# This function focuses on Button4 changes and updates in including/excluding datasets per user request...  
    global qdf, bitpair, qdf_bits_flag 
    if  (qdf_bits_flag[0] == False) and (qdf_bits_flag[1] == True):
         qdf_bits_flagset() # Call this function to show the qdf bit values of the employed dataset.
         button4.configure(text=f'Change Dataset: {qdf} vs Complement {bitpair}')
         buttonInvisible.configure(text=f'{qdf} vs its complement {bitpair}')
         button4.update()
    else:
        button4.configure(text=f'Change Dataset: [##] vs Complement [##]')
        buttonInvisible.configure(text=f'[##] vs its complement [##]')

for k in range(0, 1):
 for clr in color_list:
     for sprite in charslist:
          anim_label0.config(text='Configuring Logic Conditions for the chosen Circuit and Dataset...\n'+sprite, 
                             wraplength=400)
          anim_label0.update()
          #asyncio.run(mainT())
          anim_label0.place(x= 950-j/2+100, y= 500)
          sleep(0.1)  # Sprite is updated every second and then other asynchronous updating tasks take place in the outer loops. 
     anim_label0.config(fg=clr)
     anim_label0.update()

anim_label0.config(text=sprite+'\n QFLCC Game Circuit Configuration Complete. Click START to Continue...', 
                   wraplength=400)
anim_label0.update()

root.mainloop() # Run the Tkinter main loop.

#######################################################
# Variables for defining QDF game states and their 
# animation functions.  
#######################################################
game_points = []  # This is to keep win/lose score.
level_points= []  # This is to keep track of the level completion score.
levels = 0 
points = 0
participantMain=""
participantMid=""
spd = [] # Game speed to be changed by user and register to alter the QDF game steps pace of execution. 
spd = 1.1 # QDF game speed of 1.1 is a the default value. 
#######################################################
# Defining a simple animation function of game states.  
#######################################################
def participants():
     global participantMain, participantMid 
     if takeUIn == 1:
         participantMain = bob 
     elif takeUIn == 2:
          participantMain = alice
     if takeUIn2 == 3:
          participantMid = eve
     elif takeUIn2 ==4:
          participantMid = audience   
     """Animation function for an assigned participant by a role number."""
    
def winner_show(): 
     global points
     game_sound = pygame.mixer.Sound('__snd__/gameprize_state.wav')
     game_sound.play()
     points += 10 # Add points for each win of a QDF.
     game_points.append(points) # Add result to the scoresheet.
     print(f'Your score is: {points}. Scoresheet is: {game_points}')
     for count in range(5):
        print(fg.lightgreen + excited1, end="\r", flush=True), sleep(spd)  # Default QDF game speed is = 1.1. 
        print(excited2, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
        if count == 5 or keyboard.is_pressed("n"):
             break
                  
def winner_next():
             entry_add()
             level_show()
             subprocess.run('echo "{}- ///--- Win Entry --- \
{} /// Level: {} Scored: {} at {}"'.format(entry_stage, excited2, levels, points, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_)  # Date last I/O file entry.
             print("\n",f'Next...'+fg.lightgreen+' Level:', levels, f'{here}'+fg.orange) 

def loser_show():
     global points
     game_sound = pygame.mixer.Sound('__snd__/gameloser_state.wav')
     game_sound.play()
     points -= 5 # Lose points for each loss of a QDF.
     game_points.append(points) # Add result to the scoresheet.
     print(f'Your score is: {points}. Scoresheet is: {game_points}')
     for count in range(4): 
            print(fg.orange + grounded1, end="\r", flush=True), sleep(spd)
            print(grounded2, end="\r", flush=True), sleep(spd)
            print(fg.lightred+grounded3, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
            if count == 4 or keyboard.is_pressed("n" or "s"):
             break   

def loser_next():
             entry_add() # Reopen log file and register an event entry.
             level_show()
             subprocess.run('echo "{}- ///--- Lose Entry --- {} /// Level: {} \
Scored: {} at {}"'.format(entry_stage, grounded3, levels, points, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_) # Date last I/O file entry.
             print("\n",f'Next...'+fg.lightgreen+' Level:', levels, f'{here}'+fg.orange) 

def dual_show():
     global points
     game_sound = pygame.mixer.Sound('__snd__/gamedual_state.wav')
     game_sound.play()
     points += 2 # Add points for each gain of a duality in QDF.
     game_points.append(points) # Add result to the scoresheet.
     print(f'Your score is: {points}. Scoresheet is: {game_points}')
     for count in range(5): 
            print(fg.lightgreen + dual1, end="\r", flush=True), sleep(spd)
            print(fg.orange + dual2, end="\r", flush=True), sleep(spd)
            print(fg.red + dual3, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
            if count == 5 or keyboard.is_pressed("n" or "s"):
             break 

def dual_next():
             sleep(1)
             entry_add()
             level_show()
             subprocess.run('echo "{}- ///--- Dual Entry --- {} /// Level: {} \
Scored: {} at {}"'.format(entry_stage, dual3, levels, points, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_) # Date last I/O file entry.
             print("\n",f'Next...'+fg.lightgreen+' Level:', levels, f'{here}'+fg.orange) 

def guesser_show():
     global points
     game_sound = pygame.mixer.Sound('__snd__/gamedual_state.wav')
     game_sound.play()
     points += 3 # Add points for each guess of a QDF, close but not concluded.
     game_points.append(points) # Add result to the scoresheet.
     print(f'Your score is: {points}. Scoresheet is: {game_points}')
     for count in range(5): 
            print(fg.red + guesser1, end="\r", flush=True), sleep(spd)
            print(fg.orange + guesser2, end="\r", flush=True), sleep(spd)
            print(fg.green + guesser3, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
            if count ==5 or keyboard.is_pressed("n") or keyboard.is_pressed("s"):
              break 

def guesser_next():
             sleep(1)
             entry_add()
             level_show()
             subprocess.run('echo "{}- ///--- Guesser Entry --- {} /// Level: {} \
Scored: {} at {}"'.format(entry_stage, guesser3, levels, points, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_) # Date last I/O file entry.
             print("\n",f'Next...'+fg.lightgreen+' Level:', levels, f'{here}'+fg.orange) 

def helper_show():
     global points
     game_sound = pygame.mixer.Sound('__snd__/gamehelper_state.wav')
     game_sound.play()
     points += 1 # Add points for each guess of a QDF, close but not concluded.
     game_points.append(points) # Add result to the scoresheet.
     print(f'Your score is: {points}. Scoresheet is: {game_points}')
     for count in range(2): 
            print(fg.pink + helperTarget1, end="\r", flush=True), sleep(spd)
            print(fg.orange + helperTarget2, end="\r", flush=True), sleep(spd)
            print(fg.green + aimTarget, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
            if keyboard.is_pressed("n") or keyboard.is_pressed("s"):
              break 

def helper_next():
             sleep(1)
             entry_add()
             level_show()
             subprocess.run('echo "{}- ///--- Helper Win Entry --- {} /// Level: {} \
Scored: {} at {}"'.format(entry_stage, helperTarget1, levels, points, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_) # Date last I/O file entry.
             print("\n",f'Next...'+fg.lightgreen+' Level:', levels, f'{here}'+fg.orange) 

def level_show():
#--------------------------------------------
# Register level entry or update given the 
# accumulated and/or lost energy score points.
#--------------------------------------------
     global points, levels
     game_sound = pygame.mixer.Sound('__snd__/gamelevel_complete.wav')
     game_sound.play()
     level_points.append(levels)
     if points < 10 and points > 0:
          levels=0
          print(f'\nLevel {levels} initiated! Your score is: {points}.')
          print(fg.lightgreen + guesser3, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
          level_next()
     elif points >=10 and points < 20:
          levels=1
     elif points >=20 and points < 30:
          levels=2
     elif points >=30 and points < 40:
          levels=3 
     elif points >=40 and points < 50:
          levels=4 
     elif points >=50 and points < 60:
          levels=5
     elif points >=60 and points < 100:
          levels=6
     elif points >=100 and points < 1000:
          levels=7
     elif points >=1000:
          levels=8 
          print(bg.green+fg.yellow+ f'\nLevel {levels} complete! You won all game rounds! \
Your score is: {points}. Scoresheet is: {game_points}')
          print(fg.lightgreen + guesser3, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
          game_sound = pygame.mixer.Sound('__snd__/game_music2.wav')
          game_sound.play()
          level_next()           
     print(Fore.LIGHTGREEN_EX + f'\nLevel {levels} engaged!')
     if levels >= 1 and levels < 8:  
          level_dance()
     elif levels==8:
          game_win()
     elif points <= -10:
          game_over()  # Log event, either restart or end program by calling this function.
         
def level_dance():
     for count in range(2): 
            print(fg.orange + guesser2, end="\r", flush=True), sleep(spd)
            print(fg.lightgreen + guesser3, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
            if keyboard.is_pressed("n"):
                  break 
            
def game_win():  # Conditions to play exit sound and animation, then exit game.
     for count in range(2): 
            print(fg.lightgreen + classical1, end="\r", flush=True), sleep(spd)
            print(fg.orange + classical2, end="\r", flush=True), sleep(spd)
            print(fg.lightgreen + excited2, end="\r"+Fore.LIGHTYELLOW_EX, flush=True), sleep(spd)
            if participantMain == alice:
                 print(Back.YELLOW+ fg.lightgreen + crownAlice, end="\r"+Fore.LIGHTYELLOW_EX, 
                       flush=True), sleep(spd)
            elif participantMain == bob:
                 print(Back.YELLOW +fg.lightgreen + crownBob, end="\r"+Fore.LIGHTYELLOW_EX, 
                       flush=True), sleep(spd)
     # Play Windows exit sound.
     winsound.PlaySound("SystemExit", winsound.SND_ALIAS)      
     sys.exit() # End of game as a winner, then HALT.

def errorP(): # P Error state displayed with sound effect  after wrong user's input.   
     game_sound = pygame.mixer.Sound('__snd__/errorP.wav') 
     game_sound.play()
     game_sound = pygame.mixer.Sound('__snd__/gameno_state.wav') 
     game_sound.play()
     for count in range(0, 2):    
        print(bg.green+fg.yellow+ f'{errorP1}', end="\r", flush=True), sleep(spd)
        print(bg.green+fg.yellow+ f'{errorP2}', end="\r", flush=True), sleep(spd)

def repeatP(): # P repeated displayed with sound effect after reentering a close or identical P by user. 
     game_sound = pygame.mixer.Sound('__snd__/errorP.wav')
     game_sound.play()
     game_sound = pygame.mixer.Sound('__snd__/gameno_state.wav') 
     game_sound.play()
     for count in range(0, 2):    
        print(bg.green+fg.yellow+ f'{errorP1}', end="\r", flush=True), sleep(spd)
        print(bg.green+fg.yellow+ f'{errorP2}', end="\r", flush=True), sleep(spd)
        print(bg.green+fg.yellow+ f'{aimTarget}', end="\r", flush=True), sleep(spd)

def game_over():
        game_sound = pygame.mixer.Sound('__snd__/game_countdown.wav')
        print(bg.cyan + fg.red+'QFLCC Game Over')
        game_sound.play()

        for j in range(9,-1,-1):
             print(bg.blue+fg.pink+'Enter \'r\' to restart this game, \'b\' to restart QFLCC, or else to end program...', 
                   Back.YELLOW + fg.red+f"{j}"+Back.RESET+fg.blue, end="\r")
             sleep(1)
             if j == 6:
                  game_sound.play() # Partitioned sound replayed for the entire countdown sequence.
             if j == 0:
                 uCommand = str(input(fg.lightcyan+"\n\r> "))
        if uCommand =='b' or keyboard.is_pressed("b"):
            subprocess.run(["python", "QAI-LCode_QFLCC.py"])  # Restart program.
            file_.close() # Close the log file recording events from the user's I/O terminal.
        elif keyboard.is_pressed("r") or uCommand =='r': # keyboard.wait("r"):
            level_start()
        else: 
            print(bg.cyan+fg.red+'End of Program...'+ Back.RESET + Fore.RESET)
            subprocess.run('echo "///--- QFLCC Shell Log_file HALT --- /// on {}"'.format(entry_stage, 
                            now.strftime("%Y-%m-%d %H:%M:%S")), shell=True, stdout=file_) # Date last I/O file entry.
            sys.exit() # Game Over and HALT.       

def level_next():
             entry_add()
             subprocess.run('echo "///--- Level Entry --- {}{} ///, Level: {} Scored: \
{} at {}"'.format(entry_stage, guesser3, levels, points, now.strftime("%Y-%m-%d %H:%M:%S")), 
shell=True, stdout=file_) # Date last I/O file entry.

#########################################################################################
# QAI functions to compare correlated values based on User Input and weight them through 
# the elimination process of repeated successful hits of P values.
######################################################################################### 
PInMem = 0   # P value taken from User to store and update later.  
rep_lst0 = []
rep_lst1 = []
rep_lst2 = []
w = 0.0 # ...for weighted guess by the user.  
DeltaC = 0.0 
DeltaP = 0.0
rndDeltaC = 0.0  
dp = 0.0 # ...for a duplicate identified as a switch.

def reset_PPar(): 
     global DeltaC, PInMem, w, DeltaP  
     DeltaC = 0.0
     DeltaP = 0.0
     PInMem = 0.0
     w=0.0

def uIn_Repeat():
##############################################
# Function for P and weighted P calculations.
##############################################
     global PInMem, w, dp, DeltaP  
     dp=0
     #for PInMem in rep_lst0:
     rep_lst0.append(round(PInMem, 2))  # Append the registered input with two decimal points accuracy.
     print("List of tried P\'s: "+ Fore.LIGHTMAGENTA_EX, rep_lst0, Fore.LIGHTGREEN_EX)

     rep_lst1.append(round(w, 3))     
     print("List of assigned weights: "+ Fore.LIGHTMAGENTA_EX, rep_lst1, Fore.LIGHTGREEN_EX)

     rep_lst2.append(round(DeltaP, 2))     
     print("List of matched ∆P\'s: "+ Fore.LIGHTMAGENTA_EX, rep_lst2, Fore.LIGHTGREEN_EX)
     
     # Create a set from the list.
     sub_lst0 = set(rep_lst0)
     print('Subset of tried P\'s:', sub_lst0)

     # Compare the length and print if the list contains duplicates.
     dup0 = {x for x in rep_lst0 if rep_lst0.count(x) > 1} 
     print('Duplicated P tries:'+fg.red, dup0, ''+fg.lightgreen)

     # Create a set from the list.
     sub_lst2 = set(rep_lst2)
     print('Subset of calculated ∆P\'s:',sub_lst2)
     
     dup2 = {y for y in rep_lst2 if rep_lst2.count(y) > 1} 
     print('Duplicates of matched P\'s:'+fg.lightcyan, dup2, ''+fg.lightgreen)
 
     if (round(PInMem, 2) in dup0): # or (round(DeltaP, 2) in dup2):
          print(f'Duplicates {dup0} found in your tried P\'s list! Try again...')
          dp=1
          repeatP()
          print('\n')
    
     while dp==0:
          if round(PInMem, 2) in rep_lst0 and w>=9 and dp==0: 
               print(f'P value {PInMem} guessed a weak classical P outcome and correlated with \
max(∆P)= min(P) of qubit dataset. Your successful hit weight was: {w}')
               break
          elif round(PInMem, 2) in rep_lst0 and (w<9 and w> 2) and dp==0:  
               print(f'P value {PInMem} guessed a moderate classical P outcome and correlated with \
some <∆P>=<P> of qubit dataset. Your successful hit weight was: {w}')
               break
          elif round(PInMem, 2) in rep_lst0 and (w< 1.9 and w > 1.1) and dp==0: 
               print(f'P value {PInMem} guessed a classical P outcome and correlated with \
min(∆P)= max(P) of qubit dataset. Your successful hit weight was: {w}')
               break
          elif round(PInMem, 2) in rep_lst0 and (w==0) and dp==0: 
               w=float('inf') # Define a positive infinite integer assigned to the weight variable w.
               print(f'P value {PInMem} guessed an undefined P outcome of the qubit dataset. Your \
successful hit weight was: [0, {w}]')
               break
          elif round(PInMem, 2) in rep_lst0 and (w<=1.1 and w>0) and dp==0: 
               print(f'P value {PInMem} guessed a strong classical P outcome and correlated with \
max(∆P)=min(P) of qubit dataset. Your successful hit weight was: (0, {w}]')
               break
          elif round(PInMem, 2) in rep_lst0 and (w<=2.2 and w>=1.9) and dp==0: 
               print(f'P value {PInMem} guessed a superposition P outcome and correlated with a \
∆P=1/2 uncertainty of the qubit dataset. Your successful hit weight was: {w}')
               break
          elif dp==1: 
               reset_PPar()
               continue
          else:
               print(f'P value not guessed and uncorrelated. Your successful hit weight was: {w}')
               reset_PPar()
               break

#### Volume Settings #### 
import pyautogui as pvol

def set_game_vol(new_volume):
#############################################################
# The volume function sets volume according to your OS. 
# This option is available as 'v' or 'volume' during the game.
#############################################################
    pvol.press('volumedown', presses = 50) # Sets volume to zero.
    time.sleep(0.5) # Using time.sleep to space the presses. 
    x = math.floor(new_volume / 2) # Setting the amount of presses required.
    pvol.press('volumeup', presses = x) # Setting the volume.
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) # Sound test. 
    """- End of basic mode volume settings."""

#################################################################
# Packages and variables for sound volume change from within CLI 
# during the game (expert mode with decimal range approximation).
#################################################################
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
###- End of expert mode volume settings -###

def stayIn():
##########################################################################
# To stay in prompting environment and respond to a repeated question.
##########################################################################
 while True:    
     promptIn = str(input(bg.green + fg.yellow +'Do you want to continue in prompt mode to input command? [y/n]'+ Back.RESET))
     if (promptIn == 'y' or promptIn == 'yes') and pFlag == True:
           print(bg.green + fg.yellow +
                 "Input the relevant command according to \'h\' or \'help\', \'cv\', \'v\' or \'volume\' for sound volume change..."
                 + Back.RESET)
           promptGame() # Restart the prompt function.
           break
     elif (promptIn == 'y' or promptIn == 'yes') and pFlag == False:
           print(bg.green + fg.yellow +
                 "Input command according to \'help\'. To view the list of commands input \'h\' or \'help\':"
                 + Back.RESET)
           promptGame() # Restart the prompt function.
           break
     elif (promptIn == 'n' or promptIn == 'no') and (pFlag == True or pFlag == False):
           break  # Skip this step and continue the game based on n or any other relevant command. 

def pass_code():
###############################################################################
# Enters Safe Mode via passcode to cheat and change dataset feed to the game.
###############################################################################
 global dir_flag
 # Data here lists hardcoded data. This array can be customized and elements replaced 
 # via index value replacement by a password txt file once loaded.
 y = random.randint(0, 9999) # Can crack and override this when value is stored and accessed realtime 
                             # not after view.
 y = str(y)
 pass_file = "pass-code.txt"

 x = random.randint(0, 1)
 x= str(x)

 data = {
  "passcode": ['$ Alice & Bob cheat $', 'qdf cheat sheet 2121', 'dataset 0110 cheat',
                'qdf dataset 00,01,10,11', x, len(y[:-1])*'#'+y[-1:], ''],
  f"{Back.LIGHTGREEN_EX}qualified{Back.RESET}": [f"{Fore.LIGHTGREEN_EX}{True}{Fore.LIGHTGREEN_EX}", 
                f"{Fore.LIGHTGREEN_EX}{True}{Fore.LIGHTGREEN_EX}", 
                f"{Fore.LIGHTGREEN_EX}{True}{Fore.LIGHTGREEN_EX}", 
                f"{Fore.LIGHTGREEN_EX}{True}{Fore.LIGHTGREEN_EX}", 
                f"{Fore.LIGHTRED_EX}binary to pass [{False}]{Fore.LIGHTGREEN_EX}", 
                f"{Fore.LIGHTYELLOW_EX}one-time pass [{True}]{Fore.LIGHTGREEN_EX}", 
                f"{Fore.LIGHTRED_EX}else to pass [{False}]{Fore.LIGHTCYAN_EX}"]
 }
 df = pd.DataFrame(data, index=['pass_1', 'pass_2', 'pass_3', 'pass_4', 'pass_5', 'pass_6', 'pass_7'])
 index_ = ['pass_1', 'pass_2', 'pass_3', 'pass_4', 'pass_5', 'pass_6', 'pass_7'] # Create the index.
 df.index = index_ # Set the index.

 z=['','','','','','','']
 for i in range (0,6):
      z[i] = df.loc[f'pass_{i+1}','passcode']
      #print(z[i])  # Any other z[i], for a combo code restrictions and switches can updated to the growing passcode list below. 

 user_input = input(f"{fg.lightgreen}>>{fg.lightcyan} This command is supported only in the QFLCA's Safe Mode (SM:>>)\
 environment! \n-- Enter [Passcode + Enter] to proceed. If 'qualified' enter 'n' when prompted.{Fore.LIGHTRED_EX}* \
\n*- Some passcodes{fg.lightcyan} can unlock lower and/or higher level codes to access different game levels and datasets. \
\n-- Here is your chance to use a one-time passcode, if you know where it is locally?! Press Enter... ") 
 
 with open(pass_file, 'w+') as passf_to_write:
               # Write information about the original image sequence and final image frame.
               passf_to_write.write(y) 
 passf_to_write.close() 
 game_sound = pygame.mixer.Sound('__snd__/game_countdown.wav')
 game_sound.play()
 hline = "=========================================================================================================="
 for cnt_down in range(9, -1, -1): # 10 seconds left to see this code from its file location.
    print(f"{fg.lightgreen}>>{fg.lightcyan} One-time passcode is unmasked in the\
 background for 10 seconds...{Back.YELLOW + fg.red}{cnt_down}{Back.RESET+ fg.lightcyan}", end = '\r')
    sleep(1)
    if cnt_down == 6:
         game_sound.play() # Partitioned sound replayed for the entire countdown sequence.
    elif cnt_down == 0:
         #print(end=' ')
         print(f"{hline}")

 with open(pass_file, 'w+') as passf_to_write:
     passf_to_write.write(len(y[:-1])*"#"+y[-1:])
     passf_to_write.close() 
 with open(pass_file) as passf_to_read:
      print(f"{fg.lightgreen}>>{fg.lightcyan} One-time passcode is now masked... {Fore.LIGHTRED_EX}" 
            + passf_to_read.read() + Fore.LIGHTCYAN_EX), sleep(2)
 passf_to_read.close()

 user_input = input(f"{fg.lightgreen}>>{fg.lightcyan} Enter your passcode, or press Enter to skip back to \
regular prompt ({fg.lightgreen}>{fg.lightcyan}): {Fore.LIGHTRED_EX}")

 newdf = df.mask(df["passcode"] >= user_input[2:]) # Mask code until revealed with the 
                                                    # right one(s) entered by user 
                                                    # (the first 2 chars of input ignored).
 if (user_input == z[0] or user_input == z[1] or user_input == z[2] or user_input == z[3] or user_input == z[4]
     or user_input == z[5]):
        dir_flag = 1  # Directory flag is set to 1 for directory access in safe mode. 
        qdf_bits_flag[1] = True # Set this flag to 1 or reveal the qdf bit values from any selected dataset.
        qdf_bits_flagset() # Call this function to show the qdf bit values of the employed dataset.
        update_btn4_text() # Make sure the form button4 has qdf bit values revealed by calling this function. 
        print(f"{bg.cyan + user_input} is qualified as [True]! \nThe following list shows if there are any more \
passcodes you can use later: {Fore.LIGHTGREEN_EX +  Back.RESET}")
        print(newdf)
        prompt()
        safeMode_dir()
        PAnalysis_model() # Run QDF circuit simulation in case of successfully accessing the cheat sheet 
                          # for a new dataset feed. Dir flag will be reset back to 0 in the process. 
 if (user_input == "n" or user_input == z[6] or user_input == ' ' or user_input == "next"):
        dir_flag = 0
        prompt() 
 if user_input == y:  # Reveal all passcodes if the random number is caught/guessed and entered by the user.
        dir_flag = 1
        qdf_bits_flag[1] = True # Set this flag to 1 or reveal the qdf bit values from any selected dataset.
        qdf_bits_flagset() # Call this function to show the qdf bit values of the employed dataset.
        update_btn4_text() # Make sure the form button4 has qdf bit values revealed by calling this function. 
        print(f"{bg.cyan + user_input} You unlocked all the passcodes for future use! This is your chance to \
write them down: {Fore.LIGHTGREEN_EX +  Back.RESET} \n", df)
        prompt()
        safeMode_dir()
        PAnalysis_model()  
        """- End of passcode conditions to change the game's dataset feed."""

def promptGame():
######################### 
# QDF Game Help function.
#########################
    global spd, pFlag, site_name   # A global variable for game speed as the QDF game steps pace up or slow down.  
               # pflag is a boolean global variable to raise this flag for the prompt state for a specific prompt. 
    while True:
        print(fg.lightgreen + "\r< ", end=""), sleep(spd)
        print("\r> ", end=""+fg.orange), sleep(spd)
        try:
             promptIn = str(input()) # Respond to the user's choice or command.
             if promptIn == 'n' or promptIn == 'next' or promptIn == 'no':
                break
             elif promptIn == 's' or promptIn == 'speed':
                  takeUIn_speed = float(input(bg.orange+'Change game speed ─=≡Σ((( つ◕ل͜◕)つ ... Choose from this range:'
                                              + Back.RESET+ fg.yellow  +' [fastest = 0.1, slowest = 2]: '))
                  spd = takeUIn_speed 
                  if spd >2.0 or spd < 0.1:
                       print(fg.red +"Wrong value entered! Type in the same \'s\' command or other for an input...")
                       promptGame()
                  else:
                      spd = takeUIn_speed 
                  break
             elif promptIn == 'v' or promptIn == 'volume':
                  vol = float(input(bg.orange+'Input sound volume ─=≡Σ(((° ͜ʖ ͡°)👂🕪  between'+ Back.RESET+ fg.yellow  
                                    + '[🔇 = 0 for muted, and 🔊 = 100 for loudest]: '))
                  if vol >= 0 and vol <= 100:
                     set_game_vol(vol)
                     pFlag = True # Raise this flag for message containing a volume prompt message.
                     stayIn()  # To remain to make further volume change or input other command.
                     break 
                  elif vol < 0:
                       set_game_vol(vol)
                       print(fg.red +"Out of range or wrong value entered! Readjusted volume to muted or 0!")
                       promptGame()  # Restart prompt.
                       break 
                  elif vol > 100:
                       set_game_vol(vol)
                       print(fg.red +"Out of range or wrong value entered! Readjusted volume to maximum or 100!")
                       promptGame() # Restart prompt. 
                       break
             elif promptIn == 'cv' or promptIn == 'cliv':
                  pFlag = True # Raise this flag for message containing a volume prompt message.
                  takeUIn_volume = float(input(bg.orange+'Change game volume ─=≡Σ(((° ͜ʖ ͡°)👂🕪 ... Choose from this range:'
                                               + Back.RESET+ fg.yellow + 
                                               ' [{quietist 🔇 ⮂ 🔉 = [0 to 6], quiet 🔉 = 6.1}, loudest 🔊 = 100]: ')) # Input value 
                                                                                                      # should be between >= 0 and 100.
                  cvol = takeUIn_volume 
                  if cvol > 100 or cvol < 0:
                       print(fg.red +"Out of range or wrong value entered! Type in the same \'cv\' command or other for an input...")
                       promptGame() # Restart prompt.
                       break
                  elif cvol >= 20 and cvol <= 100:
                      cvol = takeUIn_volume
                      min_vol = ((11*cvol - 1100)/40)  # My lower conversion formula for volume range of [-29, 0] 
                                                       # is e.g.: 100-(100*(-5-0)/((0-55)/2)) as simplified.
                      print ("Volume converted and adjusted from the upper desktop's endpoint volume range of [-29, 0] =" , "%.4f" % min_vol) 
                      #--------------------------------------------
                      # Control volume proximation:
                      #--------------------------------------------
                      #volume.SetMasterVolumeLevel(0, None) #max
                      #volume.SetMasterVolumeLevel(-5.0, None) #72%
                      volume.SetMasterVolumeLevel(min_vol, None) #alternative 72% from 80 as user input.
                      #volume.SetMasterVolumeLevel(-10.0, None) #51% 
                      #volume.SetMasterVolumeLevel(-20.0, None) #26% alternative is 27 from user input (very close).
                      #volume.SetMasterVolumeLevel(-30.0, None) #13%
                      #volume.SetMasterVolumeLevel(-55.0, None) #1%
                      #--------------------------------------------
                      winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 
                      stayIn() # To remain to make further volume change.
                      break
                  elif cvol > 6  and cvol < 20:
                      cvol = takeUIn_volume 
                      min_vol = -4000/(11*cvol)  # My lower conversion formula for volume range of [-40, -30] is: 
                                                 # 100*(100/(-55-0)/((0-55)/2))=6.61 as simplified.
                      print ("Volume converted and adjusted from the lower desktop's endpoint volume range of [-41, -30] =" 
                             , "%.4f" % min_vol) 
                      volume.SetMasterVolumeLevel(min_vol, None) 
                      winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                      stayIn() # To remain to make further volume change.
                      break
                  elif cvol >= 0 and cvol <= 6: # This condition ranges the module's close to muted state or 0% volume.
                      cvol = 6  # The minimum limit has reached for the lowest bound conversion for the customized volume. 
                      min_vol = -4000/(11*cvol)  # My lower conversion formula for volume range of 
                                                 # [-60.606060..., -40) as simplified.
                      print ("Volume converted and adjusted from the upper desktop's endpoint volume range of [-60.6, -40) ="
                             , "%.4f" % min_vol) 
                      volume.SetMasterVolumeLevel(min_vol, None)
                      winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 
                      stayIn() # To remain to make further volume change.
                      break      
             elif promptIn == 'b' or promptIn == 'begin':
                  subprocess.run(["python", "QAI-LCode_QFLCC.py"])  # Restart program to analyze and validate a new dataset.
                  break
             elif promptIn == 'f' or promptIn == 'form':
                  print('Revisit dataset(s) form load & play [Temporal State]...☝ (° ͜ʖ ͡°)👉🗊 ⟵ ⛁ : '
                        + bg.red + fg.yellow +'A F F I R M A T I V E !')
                  game_sound = pygame.mixer.Sound('__snd__/gameaffirmative_state.wav')
                  game_sound.play()
                  root.deiconify() # Unhide this form and show its options to resume game, reload or choose dataset(s).
                  pFlag = False # Lower this flag for a message containing a regular prompt message 
                  stayIn() # To remain in prompt mode to input command. 
                  break
             elif promptIn == 'r' or promptIn == 'restart':
                  print('Restarting program...☝(° ͜ʖ ͡°)☝')
                  open_new_win() # Restart program.
                  break
             elif promptIn == 'website' or promptIn == 'site' or promptIn == 'about' or promptIn == 'web': 
                  site_name = "game-site" # This html file is stored in the same site folder to read.
                  site_doc() # Load website.
             elif (promptIn == 'dir' or promptIn == 'sm dir') and (dir_flag == 0):
                  pass_code()  # Call this function to enter passcode to cheat and feed a new dataset to the game.
                               # Dir flag will be set to 1 in the process.
                  continue
             elif promptIn == 'h' or promptIn == 'help':
                  userGame_Help()  # Show help.
                  continue 
             elif promptIn == 'e' or promptIn == 'exit':
                  # Play Windows exit sound.
                  game_sound = pygame.mixer.Sound('__snd__/goodbye1.wav')
                  game_sound.play()
                  print('Exiting game...🖐 (° ͜ʖ ͡°)🖐  Goodbye!'), sleep(3)
                  main_exit()  # Terminate game program.
             else:
                print('Input command or response. For help, enter \'h\'... ')
                continue
        except ValueError:
             print("Invalid input. Please enter a response.")

def userGame_Help():
#########################
# QDF Game Help function.
#########################
     while True:
          print(f'\033[0;31m\033[1m\x1B[1;4mGame Input Tips:\x1B[0m\033[0m \033[0;36m\n-Enter \'n\' key for the next message, result, \
output or next input. \n-Enter \'h\' to display these tips. \n-Enter a role number when asked for a role as Alice {alice} or Bob \
{bob} via Eve {eve} or the Audience {audience}. \n-Enter a value between 0 and 1 inclusive when asked for a \
P value. \n-Enter \'r\' to restart game. \n-Enter \'b\' to analyze and validate a new dataset. \n-Enter \'s\' \
or \'speed\' to change the speed of game steps. \n-Enter \'v\' or \'volume\' for sound volume change during the game. \
\n-Enter \'site\' or \'web\' to view \'about\' the game \'website\'. \
\n-Enter \'cv\' for sound volume change within CLI. \n-Enter \'f\' or \'form\' to reload the QDF \
game form (resume game by clicking its \'START\' button). \
\n-Enter \'dir\' or \'sm dir\' for a new dataset analysis & simulation to feed this game.*\
\n*-This command requires a passcode to see dataset results in a Safe Mode (SM:>>) environment!\
     \n-Enter \'e\' to exit the program.')
          break

##########################################
# QFLCC Game Conditions...
##########################################
p=1 # classical state of the probability
k=10 # math.inf #float('inf') 

# Set an initial condition.
game_active = True

def level_start():
     entry_add()  # Date last I/O file entry. 

level_start()
level_show() # Register level no. Levels engage and get completed given the lost vs. accumulated points.

#################################################
# The main game code block for taking in P's from 
# the user and dataset(s), and determine game's
# participant role, wins, losses and levels.
#################################################
while game_active:
    dp=0
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    try:
     takeUIn = int(input(fg.orange+f'In this game, are you Bob {bob} the guest, or Alice {alice} \
the host to win a/the prize (targeted energy state) {prize}?\nChoose 1 for \
Bob, 2 for Alice: '))
     sys.stdout.flush() # Clear line.
    except ValueError:
         game_sound = pygame.mixer.Sound('__snd__/gameno_state.wav') 
         game_sound.play()
         print(fg.lightred + f"❌ NO! Wrong Input! Input must be 1 or 2. {errorP1} Try again..."+fg.lightgreen)
         continue
    try:
     takeUIn2 = int(input(f'For your game participant {takeUIn}, will Eve {eve} join by quantum means \
to secretly share information about the prize {prize}?\nChoose 3 to have Eve \
spying, 4 for Audience {audience} to cheer/suggest and raise/lower \
participant {takeUIn}\'s energy state: '))
    except ValueError:
         game_sound = pygame.mixer.Sound('__snd__/gameno_state.wav') 
         game_sound.play()
         print(fg.lightred + f"❌ NO! Wrong Input! Input must be 3 or 4. {errorP2} Try again..."+fg.lightgreen)
         continue
    try:
     takePIn = float(input(f'Enter a P value for participant #{takeUIn}, \
{participantMain}: '))  # The var input will be a P value for the current game participant.
    except:
         game_sound = pygame.mixer.Sound('__snd__/gameno_state.wav') 
         game_sound.play()
         print(fg.lightred + f"❌ NO! Wrong Input! Input a floating-point value between 0 and 1. {errorP1} Try again..."
               +fg.lightgreen)
         continue

    promptGame()
    participants()
    PInMem = takePIn
    
    uIn_Repeat() # Register P value and compare for a weight assigned to the closest correlation vs farthest 
                 # for a strong prediction between two datasets. Not just comparingP values within this dataset 
                 # for validation purposes, according to ref. [1].  
    if ((takePIn < abs(p) and takePIn >0.5) or (takePIn < abs(p)/2 and 
                                                takePIn > 0)) and dp==0: # and takeO == 'p game':
         print(bg.green+fg.yellow+'Hello, Quantum World!'+Back.RESET)
         ##################################################
         # Now test correlation with prediction results
         ##################################################
         if (takePIn < float(df3Mem) and takePIn>0.5):
              DeltaP = float(df3Mem) - takePIn 
              if DeltaP < 0.5:
                   rndDeltaC = round(1-DeltaP, 2)   
                   DeltaC = 1-DeltaP
                   w= round((1/(DeltaC)),3)  # Weighted value of the correlation distance. 
                                             # The closer to infinity the greater the weight and 
                                             # inaccuracy of player's guess/hit on P value.    
                   print(f'Correlation to strong prediction result for participant #{takeUIn}, \
{participantMain}, is high to win:'+fg.yellow, DeltaC, Fore.RESET)
                   if (takeUIn == 1 and takeUIn2 == 3 and (DeltaC >0.5 or DeltaC ==1)): 
                        print(Back.LIGHTYELLOW_EX + 'Alice loses to Bob. Bob wins the prize with Eve\'s help!'
                              +Back.RESET+fg.green+' YOU WIN!')
                        print(fg.green+'These doubles won the prize:'+fg.pink, qdf, fg.green+ ', QDF P match is:'
                              +fg.pink, rndDeltaC)
                        winner_show()
                        winner_next()
                   elif (takeUIn == 1 and takeUIn2 == 4 and (DeltaC > 0.5 or DeltaC ==1)):
                        print(Back.LIGHTYELLOW_EX + 
                              'Alice loses to Bob. Bob wins the prize as the Audience cheer without Eve\'s help!'
                              + Back.RESET+fg.green+' YOU WIN!'+Fore.RESET)
                        print(fg.green+'These doubles won the prize:'+fg.pink, qdf, fg.green+ ', QDF P match is:'
                              +fg.pink, rndDeltaC)
                        winner_show()
                        winner_next()
                   elif (takeUIn == 2 and takeUIn2 == 3 and (DeltaC >0.5 or DeltaC ==1)): 
                        print(Back.LIGHTYELLOW_EX + 'Bob loses to Alice. Alice wins to keep the prize with Eve\'s help!'
                              + Back.RESET + fg.green +' YOU WIN!'+ Fore.RESET)
                        print(fg.green+'These doubles won the prize:'+fg.pink, qdf, fg.green+ ', QDF P match is:'
                              +fg.pink, rndDeltaC)
                        winner_show()
                        winner_next()
                   elif (takeUIn == 2 and takeUIn2 == 4 and (DeltaC >0.5 or DeltaC ==1)): 
                        print(Back.LIGHTYELLOW_EX + 'Bob loses to Alice. Alice wins to keep the prize as the Audience \
cheer without Eve\'s help!'+ Back.RESET + fg.green +' YOU WIN!'+ Fore.RESET)
                        print(fg.green+'These doubles won the prize:'+fg.pink, qdf, fg.green+ ', QDF P match is:'
                              +fg.pink, rndDeltaC)
                        winner_show()
                        winner_next()
         if (takePIn < float(df3Mem) and takePIn>0) and dp==0:
              DeltaP = float(df3Mem)-takePIn 
              if DeltaP > 0.2 and dfcompMem <= 0.5: # This condition could intersect with the winning condition 
                                                    # if results are close to DeltaP relative to df3Mem. This 
                                                    # creates a win hit and a loss hit as two consecutive rounds 
                                                    # (event outcomes) of the game.
                   rndDeltaC = round(1-DeltaP, 2)   
                   DeltaC = 1-DeltaP
                   w= round((1/(DeltaC)),3)#-DeltaC # Enable this for conditional DeltaC calculation. 
                   print(f'Correlation to strong prediction result for participant #{takeUIn}, {participantMain}, \
is low to win:'+fg.yellow, rndDeltaC, Fore.RESET) 
                   if (takeUIn == 1 and takeUIn2 == 3 and (DeltaC >0 and DeltaP>=(1/3))):
                        print(Back.LIGHTYELLOW_EX + 
                              'Bob loses to Alice despite Eve\'s help. Alice wins to keep the prize!'
                              + Back.RESET+fg.red+f' YOU {participantMain} via {participantMid} LOSE!'+Fore.RESET)
                        print(fg.orange+'These doubles:'+fg.lightred, qdf, fg.orange+'lost the prize to'
                              +fg.lightred, bitpair, fg.orange+', QDF P match is:'+fg.lightred, rndDeltaC)
                        loser_show()
                        loser_next()
                   elif (takeUIn == 1 and takeUIn2 == 4 and 
                         (DeltaC >0 and DeltaP>=(1/3))): # This operation got registered with values like 02, .03 etc.
                         print(Back.LIGHTYELLOW_EX + 
                               'Bob loses to Alice despite the Audience cheer without Eve\'s help. \
Alice wins to keep the prize!'+Back.RESET +fg.red +f' YOU {participantMain} via {participantMid} LOSE!'+Fore.RESET)
                         print(fg.green+'These doubles lost the prize:'+fg.lightred, qdf, fg.orange
                               +'lost the prize to'+fg.lightred, bitpair, fg.orange+', QDF P match is:'+fg.pink, rndDeltaC)
                         loser_show()
                         loser_next()
                   elif (takeUIn == 2 and takeUIn2 == 3 and (DeltaC >0 and DeltaP>=(1/3))):
                         print(Back.LIGHTYELLOW_EX + 'Bob loses to Alice despite Eve\'s help. Alice wins to keep the prize!'
                               + Back.RESET+fg.red+f' YOU {participantMain} via {participantMid} LOSE!'+Fore.RESET)
                         print(fg.green+'These doubles lost the prize:'+fg.lightred, qdf, fg.orange+'lost the prize to'
                               +fg.lightred, bitpair, fg.orange+', QDF P match is:'+fg.pink, rndDeltaC)
                         loser_show()
                         loser_next()
                   elif (takeUIn == 2 and takeUIn2 == 4 and (DeltaC >0 and DeltaP>=(1/3))):
                         print(Back.LIGHTYELLOW_EX + 
                               'Bob loses to Alice despite the Audience cheer without Eve\'s help. \
Alice wins to keep the prize!'+Back.RESET+fg.red+f' YOU {participantMain} via {participantMid} LOSE!'+Fore.RESET)
                         print(fg.green+'These doubles lost the prize:'+fg.lightred, qdf, 
                               fg.orange+'lost the prize to'+fg.lightred, bitpair, fg.orange+', QDF P match is:'
                               +fg.pink, rndDeltaC)
                         loser_show()
                         loser_next()
         else:
              print(bg.orange + fg.green+f'Continue guessing the P as participant #{takeUIn2}, {participantMid}, \
helps you {participantMain}...'+Back.RESET + fg.orange)
              helper_show()  # Grant only 1 point as a helper to the progression of user guesses to come. 
              helper_next()
    if (takePIn == abs(p) or takePIn == 0) and dp==0:
        print(bg.blue+'Hello, Classical World!\n', bg.orange + fg.green
              +'Now guess what the QDF outcome would be relative to your next classical guess?'
              +Back.RESET + fg.orange)
    elif (takePIn < float(df3Mem) and (takePIn >= 0.45 and dfcompMem <=0.5)) and dp==0:
        print(bg.blue +'Hello, Quantum-classical World!'+Back.RESET + fg.orange)
        print(f'{fg.purple}Welcome {participantMain} to the world of superposition or entanglement!')
        DeltaP = float(df3Mem)-takePIn
        rndDeltaC = round(1-DeltaP, 2)
        DeltaC = 1-DeltaP
        w= round((1/(DeltaC)),3) # -DeltaC), # Include this in case of further DeltaC calculation. 
        print('These doubles \"are all in\" for the prize:' +fg.pink, qdf, fg.green+'QDF P match is:'
              +fg.pink, rndDeltaC)
        print(bg.orange + fg.green+'Now guess what the next QDF outcome would be?'
              +Back.RESET + fg.orange)
        guesser_show()
        guesser_next()
    elif (((takePIn < float(df3Mem) and takePIn >= 0.5) and (dfcompMem <= 0.5 and dfcompMem > 0.48))) and dp==0:
             DeltaP = float(df3Mem)-takePIn
             rndDeltaC = round(1-DeltaP, 2)
             DeltaC = 1-DeltaP
             w= round((1/(DeltaC)),3) # -DeltaC), include in case of further calculation. 
             print(bg.blue+'Hello, Quantum-classical World!'+Back.RESET + fg.orange)
             print(f'{fg.purple}Welcome {participantMain} to the world of superposition or entanglement!')
             print(f'These doubles \"are all in\" for the prize: {qdf}', f'QDF P match is: {rndDeltaC}')
             print(bg.orange + fg.green+'Now guess what the next QDF outcome would be?'+Back.RESET + fg.orange)
             dual_show()
             dual_next()
             continue
    if takePIn > 1 or takePIn < 0:
        print('Wrong P value!')
        errorP()
        dp=1
        print('\n')
        continue
#########--END OF PROGRAM--#########