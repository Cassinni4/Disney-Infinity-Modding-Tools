package main

import (
    "fmt"
    "log"
    "os"
    "strconv"
    "runtime"
    "encoding/hex"
)

func main() {
    // checking command line
    if runtime.GOOS != "windows" {
        fmt.Println("Warning: This tool has been only tested on windows.")
    }

    if len(os.Args[1:]) != 1 {
      println("Wrong number of arguments!")
      println("Usage: " + os.Args[0] + " [mtbfile]")
      os.Exit(1)
    }

    filename := os.Args[1]

    // Opening the mtb file to find out the texture names
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal("Error while opening file:" + filename, err)
    }
    fmt.Printf("DEBUG: %s opened\n", filename)
    formatName := readNextBytes(file, 4)
    fmt.Printf("DEBUG: Parsed format: %s\n", formatName)
        if string(formatName) != "BNDL" {
            log.Fatal("Provided mtb file seems incorrect. Header doesnt match!")
        }
    // Hardcoded position, lets hope its always +32 bytes after the header. Probably this will be superbroken
    //data := readNextBytes(file, 32)
    data := readNextBytes(file, 24)
    // offset 0x1c number of textures
    data = readNextBytes(file, 4)
    numberOfTextures := int(data[0])
    data = readNextBytes(file, 4)
    internalTextureNameLength := int(data[0])

    if internalTextureNameLength>0 {
    internalTextureName := readNextBytes(file, internalTextureNameLength)

    println("DEBUG: Internal texture name: " + string(internalTextureName[:]))
	    for int(readNextBytes(file, 1)[0])==0 {
		println("DEBUG: 00 found")
            }
    file.Seek(-1, os.SEEK_CUR)  

    }

    println("DEBUG: Number of textures found on the mtb file:" + strconv.Itoa(numberOfTextures)) // Ugly hack: using just the first byte to get the number of textures... lets hope there isnt a case of more than 255...
    for i := 1; i <= int(numberOfTextures); i++ {

      textureName := readNextBytes(file, 8)
      data = readNextBytes(file, 4) // Skiping the FFFFFFFF delimiter
      //ZipFile := hex.EncodeToString(textureName)[0:2]+".zip"
      // fmt.Printf("Texture %d \n",i)
      //println("Filename ;"+hex.EncodeToString(textureName) + " should be on:" + ZipFile)
      println( filename + ";"+hex.EncodeToString(textureName))
      _ = data // ultrahack to stop golang compiler annoy me about "file declared but not used"

    }
}


func readNextBytes(file *os.File, number int) []byte {
    bytes := make([]byte, number)

    _, err := file.Read(bytes)
    if err != nil {
        log.Fatal(err)
    }

    return bytes
}
