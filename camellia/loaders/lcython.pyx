cdef extern from "camellia.c":
    void camellia(int, uint_8, uint8_t, uint8_t, uint8_t)


cpdef _camellia(a,b,c,d,e):
    camellia(a,b,c,d,e)
