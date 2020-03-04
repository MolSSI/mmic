from qcelemental import models

try:
    from rdkit import Chem
except:
    raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')

class Bond:
    """ RDKit-based bond order: {0: unspecified, 1: single, etc., up to 21} """
    try:
        from rdkit import Chem
    except:
        raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')    
    orders = list(Chem.BondType.values.values())

class RDKitMolecule(models.ProtoModel):
    mol: Chem.rdchem.Mol = None

    class Config:
        arbitrary_types_allowed = True

class MMToRDKit:
    try:
        from models.tools.rdkit.molecule import RDKitMolecule
    except:
        raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')

    @staticmethod
    def convert(mmol: "MMolecule") -> RDKitMolecule:
        try:
            from rdkit import Chem
        except:
            raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')
        
        rdkmol = Chem.Mol()
        erdkmol = Chem.EditableMol(rdkmol)

        for index, symb in enumerate(mmol.symbols):
            atom = Chem.Atom(symb)
            resname, resnum = mmol.residues[index]
            residue = Chem.AtomPDBResidueInfo()
            residue.SetResidueName(resname)
            residue.SetResidueNumber(resnum)
            residue.SetOccupancy(1.0)
            residue.SetTempFactor(0.0)
            atom.SetMonomerInfo(residue)
            #atom.SetIdx(index+1)
            erdkmol.AddAtom(atom)

        for i,j,btype in mmol.connectivity:
            erdkmol.AddBond(i, j, Bond.orders[int(btype)])            

        newmmol = erdkmol.GetMol()
        conf = Chem.Conformer(len(mmol.geometry))
        for i, coords in enumerate(mmol.geometry):
            conf.SetAtomPosition(i, coords)
        newmmol.AddConformer(conf)

        return newmmol