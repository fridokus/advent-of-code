use std::collections::HashMap;
use std::fs;

fn paths(
    current: &str,
    target: &str,
    graph: &HashMap<String, Vec<String>>,
    memo: &mut HashMap<(String, String), i64>,
) -> i64 {
    let key = (current.to_string(), target.to_string());
    
    if let Some(&result) = memo.get(&key) {
        return result;
    }
    
    if current == target {
        return 1;
    }
    
    if !graph.contains_key(current) {
        return 0;
    }
    
    let mut result = 0;
    for next in &graph[current] {
        result += paths(next, target, graph, memo);
    }
    
    memo.insert(key, result);
    result
}

fn main() {
    let contents = fs::read_to_string("11.in")
        .expect("Failed to read input file");
    
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();
    
    for line in contents.lines() {
        let key = line[..3].to_string();
        let values: Vec<String> = line[5..]
            .split(' ')
            .map(|s| s.to_string())
            .collect();
        graph.insert(key, values);
    }
    
    let mut memo: HashMap<(String, String), i64> = HashMap::new();
    
    // Part 1
    let r1 = paths("you", "out", &graph, &mut memo);
    println!("{}", r1);
    
    // Part 2
    let r2 = paths("svr", "fft", &graph, &mut memo) 
        * paths("fft", "dac", &graph, &mut memo) 
        * paths("dac", "out", &graph, &mut memo);
    println!("{}", r2);
}
