#!/usr/bin/python
import sys
sys.dont_write_bytecode = True
import unittest
import application.libraries.sqlite as sqlite
import datetime
import os


class TestSQLite(unittest.TestCase):
  def setUp(self):
    # self.path = '/tmp/test_db.db'
    self.path = ":memory:"
    self.db = sqlite.Connection(self.path)
    
  def tearDown(self):
    self.db.close()
    # os.unlink(self.path)
    
  def testConnection(self):
    self.assertNotEqual(self.db._db, None)
    
  def testReconnection(self):
    self.db.reconnect()
    self.assertNotEqual(self.db._db, None)
    
  def testCreateInsert(self):
    self.db.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""") 
    self.db.execute('insert into stocks values (?,?,?,?,?)', '2006-01-05','BUY','RHAT',100,35.14)
    result = self.db.query("SELECT * FROM stocks")
    self.assertNotEqual(result, [])
    
if __name__ == '__main__':
  unittest.main()