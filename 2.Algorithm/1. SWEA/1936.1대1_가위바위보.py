import sys
A, B = map(int, input().split())
if (A + B) % 3  ==  1:
    if ( A > B ):
        print ( "B" )
    else: print ( "A" )
else: 
    if ( A > B ):
        print ( "A" )
    else: print ( "B" )