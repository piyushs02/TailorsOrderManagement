import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 

	app = QApplication(sys.argv)
	web = QWebView()
	web.load(QUrl("file:///home/piyush/Dropbox/venv_tailor/Tailor_code/bills/1.html"))

	printer = QPrinter()
	printer.setPageSize(QPrinter.A4)
	printer.setOutputFormat(QPrinter.PdfFormat)
	printer.setOutputFileName("fileOK.pdf")

	def convertIt():
	    web.print_(printer)
	    print "Pdf generated"
	    QApplication.exit()

	QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
	sys.exit(app.exec_())