import argparse
import sys
import os

def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser()
    parser.add_argument('inputDirectory',
                    help='Path to the input folder.')

    parser.add_argument('outputDirectory',
                    help='Path to the output folder.')
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.inputDirectory):
       print('')
    
    directory=parsed_args.outputDirectory
    if not os.path.exists(directory):
        os.mkdir(directory)
    for filename in os.listdir(parsed_args.inputDirectory):
        f = os.path.join(parsed_args.inputDirectory,filename)
        f2=open(f,'r')
        if os.path.isfile(f):
            f1=os.path.join(directory,filename[0:-4]+"_s56124at.txt")
            f3=open(f1,'w')
            d={'t':5,'c':2,'p':3,'d':3}   
            score_t1=0
            score_t2=0
            def score(f2,score_t1,score_t2):
            	s=' '  
            	while s:
            		s=f2.read(3)
            		if s=='T1t':
            			score_t1+=d['t']
            		elif s=='T1c':
            			score_t1+=d['c']
            		elif s=='T1p':
            			score_t1+=d['p']
            		elif s=='T1d':
            			score_t1+=d['d']
            		elif s=='T2t':
            			score_t2+=d['t']
            		elif s=='T2c':
            			score_t2+=d['c']
            		elif s=='T2p':
            			score_t2+=d['p']
            		elif s=='T2d':
            			score_t2+=d['d']
            		else:
            			pass
            	return score_t1,score_t2
            score_t1,score_t2=score(f2,score_t1,score_t2)
            def result(score_t1,score_t2):
            	if score_t1>score_t2:
            		result='T1 is the winner'
            	elif score_t2>score_t1:
            		result='T2 is the winner'
            	else:
            		result='Draw'
            	return result
            result=result(score_t1,score_t2)
            f3.write(str(score_t1)+':'+str(score_t2))
            f3.close()
            f2.close()
