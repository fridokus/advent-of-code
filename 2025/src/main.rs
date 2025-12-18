use std::collections::{HashMap, HashSet};
use std::fs;

fn main() {
    let data: Vec<String> = fs::read_to_string("2025/7.in")
        .expect("Failed to read input file")
        .lines()
        .map(|s| s.to_string())
        .collect();

    // Part 1: Count beam splits
    let start_pos = data[0].chars().position(|c| c == 'S').unwrap();
    let mut beams: HashSet<usize> = HashSet::new();
    beams.insert(start_pos);
    
    let mut r1 = 0;
    for i in 1..data.len() {
        let line: Vec<char> = data[i].chars().collect();
        let mut new_beams: HashSet<usize> = HashSet::new();
        
        for &j in &beams {
            if j < line.len() && line[j] == '^' {
                r1 += 1;
                if j > 0 {
                    new_beams.insert(j - 1);
                }
                if j + 1 < line.len() {
                    new_beams.insert(j + 1);
                }
            } else {
                new_beams.insert(j);
            }
        }
        beams = new_beams;
    }
    println!("{}", r1);

    // Part 2: Count total paths
    let mut beams_map: HashMap<usize, i64> = HashMap::new();
    beams_map.insert(start_pos, 1);
    
    for i in 1..data.len() {
        let line: Vec<char> = data[i].chars().collect();
        let mut new_beams_map: HashMap<usize, i64> = HashMap::new();
        
        for (&j, &count) in &beams_map {
            if j < line.len() && line[j] == '^' {
                if j > 0 {
                    *new_beams_map.entry(j - 1).or_insert(0) += count;
                }
                if j + 1 < line.len() {
                    *new_beams_map.entry(j + 1).or_insert(0) += count;
                }
            } else {
                *new_beams_map.entry(j).or_insert(0) += count;
            }
        }
        beams_map = new_beams_map;
    }
    
    let sum: i64 = beams_map.values().sum();
    println!("{}", sum);
}
