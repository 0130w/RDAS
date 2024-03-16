use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Serialize, Deserialize)]
pub struct Claims {
    pub sub: String,
    pub exp: usize
}

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

#[derive(Serialize)]
pub struct LoginData {
    pub token: String
}

#[derive(Serialize, Deserialize)]
pub struct UserInfo {
    pub user_id: Option<String>,
    pub business_id: Option<String>,
    pub nickname: String,
    pub role: String,
    pub avatar: String,
}

#[derive(Serialize, Deserialize)]
pub struct UserInfoData {
    pub username: String,
    pub password: String,
    pub user_info: UserInfo,
    pub permissions: Vec<String>
}

#[derive(Serialize)]
pub struct Response<T: Serialize> {
    pub code: i32,
    pub data: Option<T>
}

#[derive(Deserialize)]
pub struct LoginRequest {
    pub username: String,
    pub password: String
}

#[derive(Serialize, Deserialize)]
pub struct BusinessWithGradeScore {
    pub business_id: String,
    pub grade_score: f64
}