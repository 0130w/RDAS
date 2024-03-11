use serde::Deserialize;
use std::collections::HashMap;

#[derive(Debug, Clone, Deserialize)]
pub struct BusinessInfo {
    pub business_id: String,
    pub name: String,
    pub address: String,
    pub city: String,
    pub state: String,
    pub postal_code: String,
    pub latitude: f64,
    pub longitude: f64,
    pub stars: f32,
    pub review_count: u32,
    pub is_open: u8,
    pub attributes: Option<HashMap<String, String>>,
    pub categories: String,
    pub hours: Option<HashMap<String, String>>
}

pub enum SortConditions {
    Synthesis,
    Distance,
    Stars
}

pub enum FilterConditions {
    Distance,
    Stars,
    Facility
}