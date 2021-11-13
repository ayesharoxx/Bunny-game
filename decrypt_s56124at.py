import argparse
import sys
import os
import string

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
        f = os.path.join(parsed_args.inputDirectory, filename)
        f2=open(f,'r')
        if os.path.isfile(f):
            f1=os.path.join(directory,filename[0:-4]+"_s56124at.txt")
            f3=open(f1,'w')
            def morsecode(f2):
                d= { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----'}
                s1=f2.read()
                b=0
                for i in s1:
                    b+=1
                    if i==':':
                        break
                s=s1[b:]

                l=s.split(' ')
                text=''
                a=''
                for i in l:
                    if '.' in i or'-' in i:
                        for key in d:
                            if d[key]==i:
                                a+=key.lower()
                    elif i=='/':
                        a+='/'
                    elif i=='\n':
                        a+='\n'
                    else: 
                        pass
                l1=a.split('/')
                text=' '.join(l1)
                f2.close() 
                return text
            def ceaser(f2):
                s1=f2.read()
                b=0
                for i in s1:
                    b+=1
                    if i==':':
                        break
                s=s1[b:]
                text=''
                for i in s.lower():
                    if i in string.ascii_lowercase: 
                        p=ord(i)
                        np=p-ord('a')
                        shift=(np-3)%26
                        np1=shift+ord('a')
                        text+=chr(np1)
                    else:
                        text+=i
                f2.close()
                return text
            def hexadecimal(f2): 
                s1=f2.read()
                b=0
                for i in s1:
                    b+=1
                    if i==':':
                        break
                s=s1[b:]
                s2 = ''.join(chr(int(i, 16)) for i in s.split())
                f2.close()
                return s2.lower()
            def checkmethod(f2):
                s1=f2.read()
                b=0
                for i in s1:
                    b+=1
                    if i==':':
                        break
                s=s1[b:]
                l = [' ', '\t', '\n']
                for j in l:
                    s = s.replace(j, '')
                if s.isalpha():
                    method='ceaser(+3)'
                elif s.isalnum():
                    method='hexadecimal'
                else:
                    method='morse code'
                return method
            method=checkmethod(f2)
            f2.seek(0)
            if method=='morse code':
                text=morsecode(f2)
                f3.write(text)
                f3.close()
            elif method=='ceaser(+3)':
                text=ceaser(f2)
                f3.write(text)
                f3.close()
            else:
                text=hexadecimal(f2)
                f3.write(text)
                f3.close()