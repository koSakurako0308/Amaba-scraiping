# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from amaba_sc import amaba
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 247,248 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"検索", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"出力先", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"出力", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.URL )
		self.m_spinCtrl1.Bind( wx.EVT_TEXT, self.page )
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.word )
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.csv )
		self.m_button2.Bind( wx.EVT_BUTTON, self.go )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def URL( self, event ):
		event.Skip()

	def page( self, event ):
		event.Skip()

	def word( self, event ):
		event.Skip()

	def csv( self, event ):
		event.Skip()

	def go( self, event ):
		group = self.m_textCtrl1.GetValue()
		pagecount = self.m_spinCtrl1.GetValue()
		word = self.m_textCtrl3.GetValue()
		imgfile_url = self.m_dirPicker1.GetPath()
		amaba(imgfile_url,pagecount,group,word)
		wx.MessageBox(u'終了しました', u'タイトル', wx.OK)
		event.Skip()

