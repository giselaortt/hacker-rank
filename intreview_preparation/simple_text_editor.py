#URL:
#https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-six

from collections import deque

class MyTextEditor():

    lastOperations = deque()
    text = str()
    
    def undo( self ):
        operation, argument = self.lastOperations.pop( )
        if( operation == 'I' ):
            self.delete( len( argument ) )
        else:
            self.append( argument )
        self.lastOperations.pop()
        

    def append( self, string ):
        self.text = self.text + string
        self.lastOperations.append( ("I", string) )
        

    def delete( self, sizeOfDeletion ):
        endOfTheText = self.text[ -sizeOfDeletion : ]
        self.text = self.text[ 0 : - sizeOfDeletion ]
        self.lastOperations.append( ("D", endOfTheText ) )
    

    def accessElement( self, k ):
        if( k < len(self.text) ):
            return self.text[k]

        return None
        

    def __str__( self ):

        return self.text + "\n"


if __name__ == '__main__':

    numberOfOperations = int(input())
    txteditor = MyTextEditor()
    
    for i in range( numberOfOperations ):
        #print( txteditor )
        inputs = input().strip().split()
        operation = int(inputs[0])
        if( operation == 1 ):
            txteditor.append( inputs[1] )
            
        if( operation == 2 ):
            txteditor.delete( int(inputs[1]) )
            #print(text)
            
        if( operation == 3 ):
            k = int(inputs[1])-1
            print(txteditor.accessElement(k))
            
        if( operation == 4 ):
            txteditor.undo()
