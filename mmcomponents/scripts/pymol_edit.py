import pymol

pymol.cmd.set('retain_order', 1)
pymol.cmd.set('pdb_use_ter_records', 0)

pymol.cmd.load('data/dialanine/dialanine.pdb')
residues = []

def get_resn(index, resn):
    residues.append([index, resn])

myspace = {'get_resn': get_resn}
pymol.cmd.iterate('(all)', 'get_resn(index, resn)', space=myspace)

def set_resn(atom_index):
    print(atom_index, residues[atom_index-1][1], len(residues))
    pymol.cmd.alter(f'(index {atom_index})', f'resn="{residues[atom_index-1][1]}"')

pymol.cmd.delete('dialanine')
pymol.cmd.load('data/dialanine/dialanine.xyz')

myspace = {'set_resn': set_resn}
pymol.cmd.iterate('(all)', 'set_resn(index)', space=myspace)
pymol.cmd.save('dialanine_pymol.pdb')
