#!/usr/bin/python

#
#

from os import listdir, walk
from os.path import isfile, join

import subprocess

def global_consts():
  global PATH
  global PREFIX 
  # number of n-uples in searches default is 3 <-- 1word 2words 3words
  global NUM_TYPES
  
  PREFIX = "result_"
  PATH = "./"
  NUM_TYPES = 3



def graphs(filelist):
  
  print '--> tests using 1 word in search (1/3)'
  for filename in filelist:
    type = '1word'
    
    print '---'
    print '--> '+title
    print '--> generating plot-file for ('+style+')'

    try:
      subprocess.call(["gnuplot", "-e FILENAME='"+filename+ "'", "creategraphs.gp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    finally:
      None
    
  print '--> tests using 2 word in search (2/3)'
  for filename in filelist:
    type = '2word'
    
    print '---'
    print '--> '+title
    print '--> generating plot-file for ('+style+')'
    try:
      subprocess.call(["gnuplot", "-e FILENAME='"+filename+ "'", "creategraphs.gp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    finally:
      None

  print '--> tests using 3 words in search (3/3)'
  for filename in filelist:
    type = '3word'
    
    print '---'
    print '--> '+title
    print '--> generating plot-file for ('+style+')'
    try:
      subprocess.call(["gnuplot", "-e FILENAME='"+filename+ "'", "creategraphs.gp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    finally:
      None



def get_files():
  
  # method 1
  # files = [ f for f in listdir(PATH) if (isfile(join(PATH,f)) and f.startswith(PREFIX)) ]

  # method 2
  # f = []
  # for (dirpath, dirname, filenames) in walk(PATH):
  #   f.extend(filenames)  
  #   break

  files = []
  for f in listdir(PATH):
    if isfile(join(PATH, f)) and f.startswith("r"):
      print f    
    
  return files
  
  
if __name__ == "__main__":
  print '1. initializing variables ..'
  global_consts()
  
  print '2. retrieving files from filesystem...'
  f = get_files()
  
  print '3. ----'
  
  for a in f:
    print a
  
  print '4. ...ending.'
  



    
    
    

  
