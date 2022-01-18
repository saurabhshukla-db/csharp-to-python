

def a():
    
def SaveItemToLookupTable(int compressedCode):

      tempBufferIndex = -1
      while compressedCode >= 258:
        tempDecompressBuffer[++tempBufferIndex] = lzwLookupTable[compressedCode].Suffix
        compressedCode = lzwLookupTable[compressedCode].Prefix  # type: object
      tempDecompressBuffer[++tempBufferIndex] = compressedCode
      for (i = tempBufferIndex; i >= 0; i--)
        finalByteBuffer[currentByteBufferIndex++] = (byte)tempDecompressBuffer[i]