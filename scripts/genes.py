from random import choice, randint

white_patches = None 
class Genes(object): 
  name = "Genes"
  
  GenderGene = ['OO', 'OB', 'Ob', 'BB', 'Bb', 'bb', 'OY', 'BY', 'bY']
  
  AlbinoGene = ['CC', 'Cc', 'Cg', 'cc', 'cg', 'gg']
  
  DiluteGene = ['DD', 'Dd', 'dd']
  
  SpotGene = ['SS', 'Ss', 'ss']
  
  TabbyGene = ['AA', 'AK', 'Aa', 'KK', 'Ka', 'aa']
  
  LengthGene = ['LL', 'Ll', 'll']
  
  def __init__(self, GenderGene, AlbinoGene, DiluteGene, SpotGene, TabbyGene, LengthGene):
    self.GenderGene = GenderGene
    self.AlbinoGene = AlbinoGene 
    self.DiluteGene = DiluteGene
    self.SpotGene = SpotGene
    self.TabbyGene = TabbyGene
    self.LengthGene = LengthGene
   
  def __repr__(self)
    return self.GenderGene + self.AlbinoGene + self.DiluteGene + self.SpotGene + self.TabbyGene + self.LengthGene
  
  
  


  
