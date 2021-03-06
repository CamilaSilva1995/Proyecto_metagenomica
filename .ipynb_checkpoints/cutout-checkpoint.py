{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "46f69177",
   "metadata": {},
   "source": [
    "## Funcion para recortar reads"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a0ffb424",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Funcion cutout(string a recortar, pocision de inicio, longitud del recorte)\n",
    "def cutout(read,i,n_length): \n",
    "    cropped_read = read[i:i+n_length]\n",
    "    return(cropped_read)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "32172e02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'TTGCGGTCTG'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ejemplo  \n",
    "cropped_read = cutout(\"CCGTTCCTCGGGCGTGCAGTCGGGCTTGCGGTCTGCCATGTCGTGTTCGGCGTCGGTGGTGCCGATCAGGGTGAAATCCGTCTCGTAGGGGATCGCGAAGATGATCCGCCCGTCCGTGCCCTGAAAGAAATAGCACTTGTCAGATCGGAAGAGCACACGTCTGAACTCCAGTCACCTCAGAATCTCGTATGCCGTCTTCTGCTTGAAAAAAAAAAAAGCAAACCTCTCACTCCCTCTACTCTACTCCCTT\",25,10)\n",
    "cropped_read"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
