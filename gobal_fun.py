#!/usr/bin/env python 
import datetime
import time
import sys
import MySQLdb as mysql
conn= mysql.connect(user="xxx", passwd="xxx",db="xxxx", charset="utf8")
cur = conn.cursor()
