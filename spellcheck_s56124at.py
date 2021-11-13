import string
import argparse
import sys
import os

def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                    help='Path to the english.txt file')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')

    parser.add_argument('outputDirectory',
                    help='Name of the output directory.')
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.inputDirectory):
       print('')
    englishpath=parsed_args.file 
    directory=parsed_args.outputDirectory
    if not os.path.exists(directory):
        os.mkdir(directory)
    for filename in os.listdir(parsed_args.inputDirectory):
        f = os.path.join(parsed_args.inputDirectory, filename)
        f2=open(f,'r')
        if os.path.isfile(f):
            f1=os.path.join(directory,filename[0:-4]+"_s56124at.txt")
            f3=open(f1,'w')
            new_text=''
            u,p=0,0
            n1=0
            mytext=''
            l=f2.readlines()  
            t1=['.','?','!',',',':',';','-','(',')','{','}','[',']',"'",'"','–']
            for i in l:
                pcount=i.count(' . . . ')
                if pcount>=1:
                    i=i.replace(' . . . ','')
                for s in i:
                    if s.isnumeric():
                        n1+=1
                        new_text+=''
                    elif s in t1:
                        p+=1
                        new_text+=''
                    elif s in string.ascii_uppercase:
                        u+=1
                        new_text+=s.lower()
                    else:
                        new_text+=s
                p=p+pcount
            twords=len(new_text.split())
            correct_words,incorrect_words=0,0
            f2.close()
            f2=open(f,'w')
            f2.write(new_text)
            f2.close()
            f=open(englishpath,'r')
            filewords=new_text.split()
            l=f.readlines()
            for i in filewords:
                if i in l or (i+'\n') in l: 
                    correct_words+=1
                else:
                    incorrect_words+=1
            f.close()
            print(new_text)
            f3.write('s56124at'+'\n')
            f3.write('Formatting ###################'+'\n')
            f3.write('Number of upper case letters changed:'+' '+str(u)+'\n')
            f3.write('Number of punctuations removed:'+' '+str(p)+'\n')
            f3.write('Number of numbers removed:'+' '+str(n1)+'\n')
            f3.write('Spellchecking ###################'+'\n')
            f3.write('Number of words:'+' '+str(twords)+'\n')
            f3.write('Number of correct words:'+' '+str(correct_words)+'\n')
            f3.write('Number of incorrect words:'+' '+str(incorrect_words)+'\n')
            f3.close()