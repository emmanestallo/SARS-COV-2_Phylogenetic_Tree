from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator as dcl
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor as dtc 
import matplotlib.pyplot as plt 

title = 'aligned_FFT-NS-2-input-order_clean.fasta' 

with open(title, 'r') as aln: 
    alignment = AlignIO.read(aln,'fasta') 

calculator = dcl('identity')
distanceMatrix = calculator.get_distance(alignment) 

constructor = dtc(calculator) 

_tree = constructor.build_tree(alignment) 
_tree.rooted = True
print(_tree)

fig = Phylo.draw(_tree)