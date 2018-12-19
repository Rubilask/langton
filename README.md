# langton
Langton's ant

This is the program for the langton's ant where you can choose your own rules. 
It's using tkinter and is not optimized nor commentated.
For example, it might have some problem goind though the corner of the grid.

I'd be glad receiving some comments about optimization or else.

// Some paterns : (you can multiply each actions on each rule by the same number to get the same in bigger)

Langton's original patern :
  -rule1 {Right}
  -rule2 {Left}

Weird convergent behaviour :
  -rule1 {Right}
  -rule2 {Down, Left}

Binary counter :

Stationnary behaviour :
  -rule1 {Right}
  -rule2 {Right, Right}

Typical divergent behaviour:
  -rule1 {Up,Left}
  -rule2 {Up}
  
Kind of langton's ant :
  -rule1 {Up, Left}
  -rule2 {Down, Right}
