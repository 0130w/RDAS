use std::time::{SystemTime, UNIX_EPOCH};

use actix_web::{get, post, web::{self, Json}, HttpRequest, HttpResponse, Responder};
use jsonwebtoken::{ decode, encode, errors::ErrorKind, DecodingKey, EncodingKey, Header, Validation};
use serde_json::Value;
use crate::utils::{parser::parse_json, structures::{BusinessAfterFilterInfo, BusinessInfo, BusinessQuery, BusinessResponse, BusinessesWrapper, Claims, LoginData, LoginRequest, Response, SearchParams, Suggestion, UserInfoData}};

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
            let users: Vec<UserInfoData> = parse_json("dataset/userinfo.json");
            let user = users.into_iter().find(|user| user.info.username == username);
            match user {
                Some(user_info) => HttpResponse::Ok().json(Response::<UserInfoData>{
                    code: 200,
                    data: Some(user_info)
                }),
                None => HttpResponse::BadRequest().body(format!("Unknown user: {}", username)),
            }
        }
        Err(e) => HttpResponse::Unauthorized().body(format!("Invalid token: {}", e)),
    }
}

#[post("/user/logout")]
pub async fn logout() -> impl Responder {
    // TODO maintain expired token
    HttpResponse::Ok().json( Response::<()> {
        code: 200,
        data: None
    })
}

#[get("/user/searchForBusiness")]
pub async fn search_for_business(query: web::Query<SearchParams>) -> impl Responder {
    let choice = query.choice.to_string();
    let file_contents = std::fs::read_to_string("dataset/epic7_task3.json").unwrap();
    let business_with_filter: BusinessesWrapper = serde_json::from_str(&file_contents).unwrap();
    
    match serde_json::to_value(&business_with_filter) {
        Ok(json_data) => HttpResponse::Ok().json(Response::<Value>{
            code: 200,
            data: Some(json_data)
        }),
        Err(e) => HttpResponse::InternalServerError().body(format!("Error converting to json : {}", e))
    }
}


#[get("/user/recommendByHistory")]
pub async fn recommend_by_history() -> impl Responder {
    let file_contents = std::fs::read_to_string("dataset/epic8_task1.json").unwrap();
    let business_with_filter: BusinessesWrapper = serde_json::from_str(&file_contents).unwrap();
    
    match serde_json::to_value(&business_with_filter) {
        Ok(json_data) => HttpResponse::Ok().json(Response::<Value>{
            code: 200,
            data: Some(json_data)
        }),
        Err(e) => HttpResponse::InternalServerError().body(format!("Error converting to json : {}", e))
    }
}

#[get("/business/getBusinessInfo")]
pub async fn get_business_info(query: web::Query<BusinessQuery>) -> impl Responder {
    let business_id = query.business_id.to_string();
    let businesses : Vec<BusinessInfo> = parse_json("dataset/business.json");
    let mut target : Option<BusinessInfo> = None;
    for business in businesses {
        if business_id == business.business_id {
            target = Some(business)
        }
    }
    match target {
        Some(business) => {
            HttpResponse::Ok().json(Response::<BusinessResponse> {
                code: 200,
                data: Some(BusinessResponse {
                    businessInfo: business
                })
            })
        },
        None => {
            HttpResponse::InternalServerError().body(format!("Error converting to json."))
        }
    }
}

#[get("/business/getSuggestion")]
pub async fn get_suggestion() -> impl Responder {
    let file_contents = std::fs::read_to_string("dataset/advice.json").unwrap();
    let suggestion : Suggestion = serde_json::from_str(&file_contents).unwrap();
    
    match serde_json::to_value(&suggestion) {
        Ok(json_data) => HttpResponse::Ok().json(Response::<Value>{
            code: 200,
            data: Some(json_data)
        }),
        Err(e) => HttpResponse::InternalServerError().body(format!("Error converting to json : {}", e))
    }
}

// #[get("/user/friendRecommend")]
// pub async fn friend_recommend(user_id: String) -> impl Responder {
    
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