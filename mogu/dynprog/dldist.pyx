
cimport dldist

cdef damerau_levenshtein_distance(char *word1, char *word2):
   return dldist.damerau_levenshtein(word1, word2)