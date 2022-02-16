#!/usr/bin/env python3
# coding: utf-8

# ## Funcion para recortar reads

#import argparse


# Funcion cutout(string a recortar, pocision de inicio, longitud del recorte)
def cutout(read,i,n_length): 
    cropped_read = read[i:i+n_length]
    return(cropped_read)

# ejemplo  
cropped_read = cutout("CCGTTCCTCGGGCGTGCAGTCGGGCTTGCGGTCTGCCATGTCGTGTTCGGCGTCGGTGGTGCCGATCAGGGTGAAATCCGTCTCGTAGGGGATCGCGAAGATGATCCGCCCGTCCGTGCCCTGAAAGAAATAGCACTTGTCAGATCGGAAGAGCACACGTCTGAACTCCAGTCACCTCAGAATCTCGTATGCCGTCTTCTGCTTGAAAAAAAAAAAAGCAAACCTCTCACTCCCTCTACTCTACTCCCTT",25,10)
cropped_read


 ####### Arguments #######
#parser = argparse.ArgumentParser()
#parser.add_argument("-r","--read",type=str, help="read")
#parser.add_argument("-i","--pocision_inicial",type=int, help="pocision inicial")
#parser.add_argument("-n","--longitud_final",type=int, help="longitud del read")
#args = parser.parse_args()


