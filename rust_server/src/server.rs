use tonic::{transport::Server, Request, Response, Status};

use interface::{ConfigurationStatus, FrequencyInfo, MessageInfo};
use interface::message_server_server::{MessageServer, MessageServerServer};


pub mod interface {
    tonic::include_proto!("interface");
}

#[derive(Debug, Default)]
pub struct RustyServer {}

#[tonic::async_trait]
impl MessageServer for RustyServer {
    async fn configure_frequency(
        &self,
        request: Request<FrequencyInfo>,
    ) -> Result<Response<ConfigurationStatus>, Status> {
        println!("Got a request: {:?}", request);

        let reply = interface::ConfigurationStatus {
            status: String::from("success"),
        };

        Ok(Response::new(reply))
    }

    async fn configure_message(
        &self,
        request: Request<MessageInfo>,
    ) -> Result<Response<ConfigurationStatus>, Status> {
        println!("Got a request: {:?}", request);

        let reply = interface::ConfigurationStatus {
            status: String::from("success"),
        };

        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "127.0.0.1:50500".parse()?;
    let greeter = RustyServer::default();

    Server::builder()
        .add_service(MessageServerServer::new(greeter))
        .serve(addr)
        .await?;

    Ok(())
}
