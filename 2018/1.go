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

func contains_int(int_slice []int, value int) bool {
    for _, val := range int_slice {
        if value == val {
            return true
        }
    }
    return false
}

func main() {
    // Read-in file and error check (just for convention)
    data, errors := os.ReadFile("1_lan.in")
    check(errors)

    // Calculate landing frequency
    var frequency int = 0
    var frequencies []string = strings.Split(string(data), "\n")
    frequencies = frequencies[:len(frequencies)-1]
    for i := 0; i < len(frequencies); i++ {
        frequency_to_add, errors := strconv.Atoi(frequencies[i]);
        check(errors)
        frequency += frequency_to_add
    }

    // Re-calculate landing frequency if meter oscillates infinitely
    var freq int = 0
    var i int = 0
    var unique_frequencies []int
    for i < len(frequencies) {
        frequency_to_add, errors := strconv.Atoi(frequencies[i])
        check(errors)
        freq += frequency_to_add
        if contains_int(unique_frequencies, freq) {
            break
        } else {
            unique_frequencies = append(unique_frequencies, freq)
        }
        i = (i + 1) % len(frequencies)
    }

    // Print summary
    fmt.Println("AoC 2018 Day 1: Chronal Calibration")
    fmt.Println("  Part 1:")
    fmt.Println("\tFinal (finite) landing frequency is: ", frequency)
    fmt.Println("  Part 2:")
    fmt.Println("\tFinal (infinite) landing frequency is: ", freq)
}
