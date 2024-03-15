use actix_web::{post, web::Json, Responder, HttpResponse};
use jsonwebtoken::{ encode, EncodingKey, Header};
use crate::utils::structures::{Claims, LoginData, LoginRequest, LoginResponse};


fn generate_token(username: &str) -> String {
    let expiration = 60 * 60;
    let claims = Claims {
        sub: username.to_owned(),
        exp: expiration
    };
    encode(&Header::default(), &claims, &EncodingKey::from_secret("secret".as_ref())).unwrap()
}


#[post("/user/login")]
pub async fn login(login_info: Json<LoginRequest>) -> impl Responder {
    let token = generate_token(&login_info.username);
    let response = LoginResponse {
        code: 200,
        data: LoginData { token }
    };
    HttpResponse::Ok().json(response)
}