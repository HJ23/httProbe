import sys
sys.path.append(".")

import argparse
from core.httprobe import HttProbe

parser=argparse.ArgumentParser(description="Raptor advanced subdomain discovery,recon tool.")

parser.add_argument("--input","-i",required=True )
parser.add_argument("--threads","-t",required=False,default=10,type=int)
parser.add_argument("--output","-o",required=False,default="httprobe_out.txt")
parser.add_argument("--verbose","-v",required=False,action="store_true",default=False)


args=parser.parse_args()

if(__name__=="__main__"):
    obj=HttProbe(args.threads,args.verbose,args.output)
    _list=obj.read(args.input)
    print(_list)
    print(obj.start(_list))
    