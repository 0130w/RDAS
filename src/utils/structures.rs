use serde::Deserialize;
use std::collections::HashMap;

pub struct Position {
    pub latitude: f64,
    pub longitude: f64
}

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

#[allow(unused)]
enum DistanceCategories {
    FiveKM,
    TenKM,
    TwentyKM
}

#[allow(unused)]
pub struct FilterConditions {
    distance_filter: Option<DistanceCategories>,
    stars_filter: Option<f64>,
    facility_filter: Option<String>
}