use actix_web::{App, HttpServer};
use pdas_backend::api::api::{get_user_info, login, recommend_by_history, search_for_business};


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(login)
            .service(get_user_info)
            .service(recommend_by_history)
            .service(search_for_business)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}