from numpy import genfromtxt
import sys

#filename = sys.argv[1]
#fieldname = sys.argv[2]

class MyCSVImport:
    
    #from mycsvimport import MyCSVImport
    #MyCSVImport.csvprop('file.csv', 'res3')
    
    @classmethod
    def csvprop(self, filename, fieldname):
        data = genfromtxt('file.csv', delimiter='=', dtype=None)
        #return (data)
	    text = ''
        for ii in range(0, len(data)):
            #print(data[ii][0])
            #text += data[ii][0] + str(data[ii][1])
            text  += fieldname.lower()
            if data[ii][0].lower() == fieldname.lower():
                #print(data[ii][1])
                return data[ii][1]
	    return text
        #return 'Property: ' + fieldname + ' in file: ' + filename +   ' NOT found.'
