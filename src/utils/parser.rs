use std::fs;
use serde::de::DeserializeOwned;

pub fn parse_json<T>(path: &str) -> Vec<T> 
    where T: DeserializeOwned
{
    let file_content = fs::read_to_string(path).expect("Unable to read file");
    serde_json::from_str(&file_content).expect("Failed to parse json")
}