"""from musicpy import *
import mido

sakura = read('./midiFiles/千本樱.mid')
# print(sakura)
play(sakura,wait=True,instrument=27)


rules = lambda x: C(x) @ [1, 2, 3, 1.1, 2.1, 3, 1.1, 2.1] % (1/8, 1/8) * 2
A = rules('Cmajor') | rules('C7sus4') | rules('G7/B') - octave | rules('Cmajor')

play(A,wait=True,instrument=27)

## midi file play method
goodman = read('./midiFiles/千本樱.mid')

play(goodman,wait=True,instrument=1)

# handwritten midi way

a = note('A',5)   # a note play

b = note('A',num=4,duration=0.25,volume=100,channel=None)

play(b,wait=True,instrument=27)

"""



from musicpy import *

"""# 休止符 ？？
bmp = 120
N1 = note('E', 4, 1/4, 100)
N2 = note('F#', 4, 1/8, 100)
N3 = note('E', 4, 1/8, 100)

S1 = chd(N1,N2,N3)

play(S1, wait=True)
"""
# 下面的C -> chd
guitar = (C('EM7', 3, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2 |
          C('A7sus', 2, 1/4, 1/8)^2 |
          C('Em7', 2, 1/4, 1/8)^2 |
          C('FM7', 2, 1/4, 1/8)^2 |
          C('CM7', 3, 1/4, 1/8)@1 |
          C('AbM7', 2, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2) * 2

play(guitar, bpm=125, instrument=25,wait=True)

