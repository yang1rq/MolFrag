import os
from rdkit import Chem
from rdkit.Chem import BRICS, Recap
import argparse


def read_molecules(file_path):
    file_type = file_path.split('.')[-1]
    if file_type == 'sdf':
        suppl = Chem.SDMolSupplier(file_path)
        mols = [x for x in suppl if x is not None]
    elif file_type == 'smi':
        suppl = Chem.SmilesMolSupplier(file_path)
        mols = [x for x in suppl if x is not None]
    elif file_type == 'mol2':
        suppl = Chem.Mol2MolSupplier(file_path)
        mols = [x for x in suppl if x is not None]
    else:
        raise ValueError(f'Unsupported file type: {file_type}')

    if len(mols) == 0:
        raise ValueError('No molecules found in file!')

    return mols


def Brics_frag(mol):
    brics_fragments = BRICS.BRICSDecompose(mol)

    return brics_fragments


def Recap_frag(mol):
    recap_tree = Recap.RecapDecompose(mol)
    recap_fragments = list(recap_tree.children.keys())

    return recap_fragments


def main(smi_path, output, methods):
    mols = read_molecules(smi_path)

    if 'Brics' in methods:
        with open(os.path.join(output), 'w') as f:
            for mol in mols:
                brics_fragments = Brics_frag(mol)
                f.write('\n'.join(brics_fragments) + '\n')

    if 'Recap' in methods:
        with open(os.path.join(output), 'w') as f:
            for mol in mols:
                recap_fragments = Recap_frag(mol)
                f.write('\n'.join(recap_fragments) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='make fragments for smiles file')
    parser.add_argument( '--smi_path', required=True, type=str)
    parser.add_argument( '--output', required=True, type=str)
    parser.add_argument('--method', required=True, choices=['Brics', 'Recap'], type=str)
    args = parser.parse_args()

    smi_path = args.smi_path
    output = args.output
    methods = args.method

    main(smi_path, output, methods)
