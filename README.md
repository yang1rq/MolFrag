# MolFrag
### Our web server is freely available at https://dpai.ccnu.edu.cn/MolFrag/

## Requirements
```
torch    1.13.1
dgl      1.0.1
dgllife  0.3.2
rdkit    2022.9.5
igraph   0.10.6
```
## Usage
### If you want to use DigFrag to segment drug (or pesticde) molecules, run these commands:
```
python segment_Drug.pyc --pred_path=mol.csv --model_path=BEST_DF_Drug.pth --frag_path=frag_drug.csv --image_path=./image_drugfrag
```
or
```
python segment_Pesticide.pyc --pred_path=mol.csv --model_path=BEST_DF_Pesticide.pth --frag_path=frag_pesticide.csv --image_path=./image_pesticidefrag
```
Where the first parameter is the molecules you want to segment, the second parameter is the trained model(which has been provided), the third parameter is the file where the results will be stored, and the fourth parameter is the folder where the fragment images will be generated.



### If you want to use other methods to segment molecules, run these commands:
```
# BRICS
python main.py --smi_path=mol.smi --output=brics.csv --methods=Brics
```
or
```
# RECAP
python main.py --smi_path=mol.smi --output=recap.csv --methods=Recap
```
or
```
# MacFrag
python MacFrag.py -i mol.smi -o macfrag.csv -maxBlocks 6 -maxSR 8 -asMols False -minFragAtoms 1
```
Please note that the MacFrag code is sourced from [Diao et al](https://github.com/yydiao1025/MacFrag).

### If you have any questions, please contact Fan Wang (fwang@ccnu.edu.cn) or Guangfu Yang (gfyang@ccnu.edu.cn)
