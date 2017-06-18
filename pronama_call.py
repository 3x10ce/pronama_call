#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame.mixer
import time
import csv
import sys
import os


pygame.mixer.init(frequency = 48000, size = -16, channels = 2)

class VoiceManager:
    def __init__(self):
        self.vlist = {}
        self.voices = []
        with open('voice_list.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in reader:
                self.vlist[row[0]] = row[1]

    def prepare(self, serif):
        splitted = serif.split(" ")
        for s in splitted :
            if s in self.vlist :
                voice = Voice( "./voice/" + self.vlist[s] )
                self.voices.append(voice)

    def play(self):
        if self.voices is not None :
            for v in self.voices :
                v.play()

class Voice:
    def __init__(self, filename):
        self.filename = filename
        self.__sound = pygame.mixer.Sound( self.filename )
    
    def play(self):
        self.__sound.play()
        time.sleep(self.__sound.get_length())



# vm = VoiceManager()

# vm.prepare(sys.argv[1])
# vm.play()

# time.sleep( 0.3 )
