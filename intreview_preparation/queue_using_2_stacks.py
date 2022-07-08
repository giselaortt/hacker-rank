from collections import deque


class Queue():
    
    firstStack = deque()
    secondStack = deque()
    
    def _isSecondStackEmpty( self ):
        if( len(self.secondStack) == 0 ):
            return True
        return False

    def _transferFromStacks( self ):
        while( len(self.firstStack) > 0 ):
            element = self.firstStack.pop()
            self.secondStack.append( element ) 
        
    def dequeue( self ):
        if( self._isSecondStackEmpty() ):
            self._transferFromStacks()
            
        if( len(self.secondStack) > 0 ):
            self.secondStack.pop()
        
    def enqueue( self, element ):
        self.firstStack.append( element )
        
    def front( self ):
        if( self._isSecondStackEmpty() ):
            self._transferFromStacks()
        
        if( len(self.secondStack) > 0 ):
            return self.secondStack[-1]

        else:
            return -1


if __name__ == "__main__":
    
    numberOfQueries = int(input().strip())
    myqueue = Queue()
    
    for i in range( numberOfQueries ):
        inputs = input().strip().split(' ')
        
        if( len(inputs) == 2 ):
            myqueue.enqueue(int(inputs[1]))
            
        elif( int(inputs[0]) == 3 ):
            print( myqueue.front() )
            
        else:
            myqueue.dequeue()
            
