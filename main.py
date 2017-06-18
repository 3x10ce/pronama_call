#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
dir = os.path.dirname(sys.argv[0])
os.chdir(dir)

import pronama_call as pc
import owmexec as owm

import datetime
today = datetime.date.today()


echowords = ["good_morning"]

# get date
echowords.append("m%02d" % today.month )
echowords.append("d%02d" % today.day)

print echowords

vm = pc.VoiceManager()
vm.prepare(" ".join(echowords))

vm.play()

# get weather

wth = owm.getWeather()
print wth
vm = pc.VoiceManager()
vm.prepare(wth)
vm.play()
