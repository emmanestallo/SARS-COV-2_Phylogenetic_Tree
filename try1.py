#import modules 
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator as dcl
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor as dtc 
import matplotlib.pyplot as plt 

#function code 
def create_tree(fasta_file):
    #fasta filename 
    title = fasta_file 

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
    Phylo.convert('covid_tree.xml','phyloxml', 'covid_tree.nhx', 'newick')
    return 
#do not change anything before this line 
#######################################
#######################################
#######################################
#######################################
#######################################

#place fasta filename here to automatically generate xml and nhx files 
create_tree('aligned_FFT-NS-2-input-order_clean.fasta')