# Langton's ant

# Description

This is a code for the langton's ant where you can choose your own rules. 
It's using tkinter and is not optimized nor commentated.

# Some paterns :

Langton's original patern :
  -rule1 {Right}
  -rule2 {Left}

Weird convergent behaviour :
  -rule1 {Right}
  -rule2 {Down, Left}

Binary counter :
 [[-90], [-4, -5]] 
 [[0], [-5, 4]]

Stationnary behaviour :
  -rule1 {Right}
  -rule2 {Right, Right}

Typical divergent behaviour:
  -rule1 {Up,Left}
  -rule2 {Up}
  
Kind of langton's ant :
  -rule1 {Up, Left}
  -rule2 {Down, Right}
