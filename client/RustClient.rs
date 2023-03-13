extern crate reqwest;
use serde::{Deserialize, Serialize};

const BASE_URL: &str = "http://localhost:8000";

#[derive(Serialize, Deserialize, Debug)]
struct User {
    name: String,
    age: i32,
    gender: String,
    email: String,
    phone: String,
    address: String,
}

fn send_get_request(endpoint: &str) -> Result<String, reqwest::Error> {
    let url = format!("{}{}", BASE_URL, endpoint);
    let response = reqwest::blocking::get(&url)?;
    let body = response.text()?;
    Ok(body)
}

fn send_post_request(endpoint: &str, request_body: &str) -> Result<String, reqwest::Error> {
    let url = format!("{}{}", BASE_URL, endpoint);
    let client = reqwest::blocking::Client::new();
    let response = client.post(&url)
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .body(request_body.to_string())
        .send()?;
    let body = response.text()?;
    Ok(body)
}

fn send_patch_request(endpoint: &str, id: i32, name: &str, age: Option<i32>) -> Result<String, reqwest::Error> {
    let url = format!("{}{}?id={}&name={}&age={}", BASE_URL, endpoint, id, name, age.unwrap_or(-1));
    let client = reqwest::blocking::Client::new();
    let response = client.patch(&url)
        .send()?;
    let body = response.text()?;
    Ok(body)
}

fn send_delete_request(endpoint: &str, id: i32) -> Result<String, reqwest::Error> {
    let url = format!("{}{}?id={}", BASE_URL, endpoint, id);
    let client = reqwest::blocking::Client::new();
    let response = client.delete(&url)
        .send()?;
    let body = response.text()?;
    Ok(body)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Get all users
    let users_json = send_get_request("/")?;
    let users: Vec<User> = serde_json::from_str(&users_json)?;
    for user in &users {
        println!("Name: {}", user.name);
        println!("Age: {}", user.age);
        println!("Gender: {}", user.gender);
        println!("Email: {}", user.email);
        println!("Phone: {}", user.phone);
        println!("Address: {}\n", user.address);
    }

    // Add a new user
    let new_user = User {
        name: String::from("John Doe"),
        age: 25,
        gender: String::from("Male"),
        email: String::from("johndoe@example.com"),
        phone: String::from("+1234567890"),
        address: String::from("123 Main St"),
    };
    let request_body = serde_json::to_string(&new_user)?;
    let add_user_response = send_post_request("/add-user/", &request_body)?;
    println!("{}", add_user_response);

    // Update a user
    let update_user_response = send_patch_request("/update-user/", 0, "John Smith", Some(30))?;
    println!("{}", update_user_response);

    // Remove a user
    let remove_user_response = send_delete_request("/remove-user/", 0)?;
    println!("{}", remove_user_response);

    // Get server info
    let server_info_json = send_get_request("/server-info/")?;
    println!("{}", server_info_json);

    // Null server database
    let null_response = send_get_request("/null/")?;
    println!("{}", null_response);

    Ok(())
}


