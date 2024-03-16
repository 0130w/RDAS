use std::time::{SystemTime, UNIX_EPOCH};

use actix_web::{get, post, web::Json, HttpRequest, HttpResponse, Responder};
use jsonwebtoken::{ decode, encode, errors::ErrorKind, DecodingKey, EncodingKey, Header, Validation};
use crate::utils::{parser::parse_json, structures::{BusinessWithGradeScore, Claims, LoginData, LoginRequest, Response, UserInfoData}};

#[post("/user/login")]
pub async fn login(login_info: Json<LoginRequest>) -> impl Responder {
    let token = generate_token(&login_info.username);
    let response = Response {
        code: 200,
        data: Some(LoginData { token })
    };
    HttpResponse::Ok().json(response)
}

#[get("/user/info")]
pub async fn get_user_info(req: HttpRequest) -> impl Responder {
    let token = match req.headers().get("Authorization") {
        Some(header_value) => header_value.to_str().unwrap_or(""),
        None => "",
    };

    match decode_token(token) {
        Ok(claims) => {
            let username = claims.sub;
            let users: Vec<UserInfoData> = parse_json("../../dataset/userinfo.json");
            let user = users.into_iter().find(|user| user.username == username);
            match user {
                Some(user_info) => HttpResponse::Ok().json(user_info),
                None => HttpResponse::BadRequest().body(format!("Unknown user: {}", username)),
            }
        }
        Err(e) => HttpResponse::Unauthorized().body(format!("Invalid token: {}", e)),
    }
}

#[post("/user/logout")]
pub async fn logout(_token: String) -> impl Responder {
    // TODO maintain expired token
    HttpResponse::Ok().json( Response::<()> {
        code: 200,
        data: None
    })
}

// #[post("/user/searchForBusiness")]
// pub async fn search_for_business(latitude: String, longitude: String, city: String) -> impl Responder {

// }

#[post("/user/recommendByHistory")]
pub async fn recommend_by_history(_token: String) -> impl Responder {
    let business_with_grade_score: Vec<BusinessWithGradeScore> = parse_json("../../dataset/epic8_task1.json");
    match serde_json::to_value(&business_with_grade_score) {
        Ok(json_data) => HttpResponse::Ok().json(json_data),
        Err(e) => HttpResponse::InternalServerError().body(format!("Error converting to json : {}", e))
    }
}

// #[post("/user/getBusinessInfo")]
// pub async fn get_business_info(business_id: String) -> impl Responder {

// }

// #[post("/user/friendRecommend")]
// pub async fn friend_recommend(user_id: String) -> impl Responder {
//     // epic8 task3
// }

fn decode_token(token: &str) -> Result<Claims, String> {
    let key = "secret".as_ref();
    match decode::<Claims>(token, &DecodingKey::from_secret(key), &Validation::default()) {
        Ok(token_data) => Ok(token_data.claims),
        Err(err) => match *err.kind() {
            ErrorKind::ExpiredSignature => Err("Token expired".to_string()),
            _ => Err("Invalid token".to_string())
        }
    }
}

fn generate_token(username: &str) -> String {
    let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
    let expiration = now + 60 * 60;
    let claims = Claims {
        sub: username.to_owned(),
        exp: expiration
    };
    encode(&Header::default(), &claims, &EncodingKey::from_secret("secret".as_ref())).unwrap()
}