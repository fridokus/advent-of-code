package main

import (
    "fmt"
    "os"
    "strconv"
    "strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
    // Read-in file and error check (just for convention)
    data, errors := os.ReadFile("1_lan.in")
    check(errors)

    // Calculate landing frequency
    var frequency int = 0
    var frequency_to_add int
    var frequencies_string []string = strings.Split(string(data), "\n")
    frequencies_string = frequencies_string[:len(frequencies_string)-1]
    var f_len int = len(frequencies_string)
    frequencies := make([]int, f_len)
    for i := 0; i < f_len ; i++ {
        frequency_to_add, errors = strconv.Atoi(frequencies_string[i])
        check(errors)
        frequencies[i] = frequency_to_add
        frequency += frequency_to_add
    }

    // Re-calculate landing frequency if meter oscillates infinitely
    var freq int = 0
    var i int = 0
    unique_frequencies := make(map[int]bool)
    for i < f_len {
        freq += frequencies[i]
        if unique_frequencies[freq] {
            break
        }
        unique_frequencies[freq] = true
        i = (i + 1) % f_len
    }

    // Print summary
    fmt.Println("AoC 2018 Day 1: Chronal Calibration")
    fmt.Println("  Part 1:")
    fmt.Println("\tFinal (finite) landing frequency is: ", frequency)
    fmt.Println("  Part 2:")
    fmt.Println("\tFinal (infinite) landing frequency is: ", freq)
}
