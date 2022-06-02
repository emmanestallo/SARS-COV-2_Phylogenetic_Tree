#import modules 
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator as dcl
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor as dtc 
import matplotlib.pyplot as plt 

#fasta filename 
title = 'aligned_FFT-NS-2-input-order_clean.fasta' 

#open fasta file 
with open(title, 'r') as aln: 
    alignment = AlignIO.read(aln,'fasta') 

#get document distance usingg matrix calculator in biopython
calculator = dcl('identity')
distanceMatrix = calculator.get_distance(alignment) 

#construct tree based on document distance 
constructor = dtc(calculator) 

#build tree 
_tree = constructor.build_tree(alignment) 
_tree.rooted = True
print(_tree)

#plot 
fig = Phylo.draw(_tree)

Phylo.write(_tree, "covid_tree.xml", "phyloxml")