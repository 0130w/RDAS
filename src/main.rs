use actix_web::{get, App, HttpResponse, HttpServer, Responder};
use pdas_backend::api::api::login;


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(login)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}