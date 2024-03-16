use actix_web::{App, HttpServer};
use pdas_backend::api::api::{get_user_info, login};


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(login)
            .service(get_user_info)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}