#!/usr/bin/env python
# _*_coding: utf8 _*_

# Cabeceras
import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de cambeceras")
parser.add_argument('-t','--target', help="Objetivo")
parser = parser.parse_args()



def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            cabeceras =   dict(url.headers)
            for x in cabeceras:
                print(x + " : " + cabeceras[x])
        except:
            print("No me pude conectar")
    else:
        print ("no hay objetivo")

if __name__ == '__main__':
    main()

