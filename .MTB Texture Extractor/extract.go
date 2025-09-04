package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os"
    "strings"
    "strconv"
    "runtime"
    "os/exec"
    "encoding/hex"
)

func main() {
    // checking command line
    if runtime.GOOS != "windows" {
        fmt.Println("Warning: This tool has been only tested on windows.")
    }

    if _, err := os.Stat("helpers\\quickbms.exe"); os.IsNotExist(err) {
      println("Error: quickbms.exe not found in the helpers folder")
      os.Exit(1)
    }

    if _, err := os.Stat("helpers\\disney_infinity.bms"); os.IsNotExist(err) {
      println("Error: disney_infinity.bms not found in the helpers folder")
      os.Exit(1)
    }

    if _, err := os.Stat("..\\DisneyInfinity3.exe"); os.IsNotExist(err) {
      println("Error: DisneyInfinity3.exe not found. Check the documentation")
      os.Exit(1)
    }

    if len(os.Args[1:]) != 1 {
      println("Wrong number of arguments!")
      println("Usage: " + os.Args[0] + " [model name]")
      os.Exit(1)
    }

    character := os.Args[1]
    var matchesFound = 0
    var lastMatch = ""

    // try to find one single match for the character
    println("Trying to find: " + character)

    files, err := ioutil.ReadDir("../assets/characters")
    if err != nil {
        log.Fatal(err)
    }


    // if no parameter was pased
    for _, f := range files {
            if strings.Contains(f.Name() , character) {
              if (f.Name() == character) {
                fmt.Println("Exact match found: " + f.Name())
                matchesFound = 1
                lastMatch = f.Name()
                break
              }
                fmt.Println("Match found: " + f.Name())
                matchesFound++
                lastMatch = f.Name()
            }
    }

    // check if there are no matches
    if matchesFound == 0 {
        println("OPS! [" + character + "] was not found!")
        os.Exit(1)
      }

    // check if there are multiple matches - This should be improved to something more nice
    if matchesFound > 1 {
        println("Multiple matches found! Please use a specific character name.")
        println("Number of matches:" + strconv.Itoa(matchesFound))
        println("Last match found:" + lastMatch)
        os.Exit(1)
    }

    // executing quickbms to extract the character name

    println("Extracting data from the character's zip file")
    out, err := exec.Command("helpers\\quickbms.exe","-o","-q","helpers\\disney_infinity.bms","..\\assets\\characters\\"+lastMatch+"\\"+lastMatch+".zip").Output()
    if err != nil {
        println("something bad happened")
        fmt.Printf("%s", err)
        os.Exit(1)
    }


    output := string(out[:])
    fmt.Println("Data extracted succesfully from: " + output)

    // Opening the mtb file to find out the texture names
    var path = lastMatch+"\\"+lastMatch+".mtb"
    file, err := os.Open(path)
    if err != nil {
        log.Fatal("Error while opening file:" + path, err)
    }
    fmt.Printf("%s opened\n", path)
    formatName := readNextBytes(file, 4)
    fmt.Printf("Parsed format: %s\n", formatName)
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
    println("Number of textures found on the mtb file:" + strconv.Itoa(numberOfTextures)) // Ugly hack: using just the first byte to get the number of textures
    for i := 1; i <= int(numberOfTextures); i++ {

      textureName := readNextBytes(file, 8)
      data = readNextBytes(file, 4) // Skiping the FFFFFFFF delimiter
      ZipFile := hex.EncodeToString(textureName)[0:2]+".zip"
      fmt.Printf("Texture %d \n",i)
      println("Filename :"+hex.EncodeToString(textureName) + " should be on:" + ZipFile)
      _ = data // ultrahack to stop golang compiler annoy me about "file declared but not used"

      println("Trying to extract the texture")
      out, err = exec.Command("helpers\\quickbms.exe","-D","-o","-f","\"*"+hex.EncodeToString(textureName)+".tbody\"","helpers\\disney_infinity.bms","..\\assets\\textures\\"+ZipFile,lastMatch).Output()
      if err != nil {

          println("something bad happened while trying to extract the first texture")
          fmt.Printf("%s", err)
          //os.Exit(1)

      }
      output = string(out[:])
      fmt.Println("Output from quickbms: " + output)


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
