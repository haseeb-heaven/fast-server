/*
Info : FastClient in C++ for FastApi connection.
Author: Haseeb Mir.
*/

#include <iostream>
#include <fstream>
#include "lib/HTTPRequest.hpp"
#include "lib/json.hpp"
using string = std::string;
using json = nlohmann::json;

// Main URL of server.
const string url = "http://localhost:8000";

string ExecuteRequest(string url, string method = "GET", string params = {}, http::InternetProtocol protocol = http::InternetProtocol::V4)
{
    http::Request request{url, protocol};
    const auto response = request.send(method, params, {{"Content-Type", "application/json"}, {"User-Agent", "runscope/0.1"}, {"Accept", "*/*"}}, std::chrono::seconds(2));

    if (response.status.code == http::Status::Ok)
    {
        string data{response.body.begin(), response.body.end()};
        return data;
    }
    return {};
}

string GetUser(int id = 0)
{
    string user_url = url + "/user/?id=" + std::to_string(id);
    string data = ExecuteRequest(user_url, "GET");
    return data;
}

string GetUsers()
{
    string data = ExecuteRequest(url, "GET");
    return data;
}

string AddUser(string params)
{
    string user_url = url + "/add-user/";
    auto data = ExecuteRequest(user_url, "POST", params);
    return data;
}

string UpdateUser(int id = 0, string name = "", int age = -1)
{
    string user_url = url + "/update-user/?id=" + std::to_string(id) + "&name=" + name + ((age != -1) ? ("&age=" + std::to_string(age)) : "");
    string data = ExecuteRequest(user_url, "PATCH");
    return data;
}

string RemoveUser(int id = 0)
{
    string user_url = url + "/remove-user/?id=" + std::to_string(id);
    string data = ExecuteRequest(user_url, "DELETE");
    return data;
}

void PrintJsonData(json &user)
{
    std::cout << "Name: " << user["name"] << '\t';
    std::cout << "Age: " << user["age"] << '\t';
    std::cout << "Gender: " << user["gender"] << '\t';
    std::cout << "Email: " << user["email"] << '\t';
    std::cout << "Contact: " << user["phone"] << '\t';
    std::cout << "Address: " << user["address"] << std::endl;
}

void ShowUser(int id = 0)
{
    string data = GetUser(id);
    json j_data = json::parse(data);
    PrintJsonData(j_data);
}

void ShowUsers(int indent = 4)
{
    string data = GetUsers();
    auto json_data = json::parse(data);
    std::cout << json_data.dump(indent) << std::endl;
}

void PPrintJson(string data, int indent = 4)
{
    if (data.length() == 0)
        return;
    auto json_data = json::parse(data);
    std::cout << json_data.dump(indent) << std::endl;
}

void PrintResponse(string resp)
{
    json data = json::parse(resp);
    if (data.is_null() || data.empty())
        std::cout << resp << std::endl;
    else
        std::cout << data["data"] << std::endl;
}

int main()
{
    try
    {
        // Add User.
        const std::string params = "{\"name\": \"DMR-Ritchie\",\"age\": 45, \"gender\": \"M\",\"email\": \"denis@dmr.com\",\"phone\": \"+1-555-343434\",\"address\": \"BELL-LABS\"}";
        string data = AddUser(params);
        PrintResponse(data);

        // Update user.
        //string data = UpdateUser(2,"Khawarizm",25);
        //PrintResponse(data);       

        // Remove user.
        // string data = RemoveUser(3);
        // PrintResponse(data);

        // Show single Users.
        //ShowUser(1);

        // Show all Users.
        ShowUsers();
    }

    catch (const http::RequestError &e)
    {
        std::cerr << "Request error: " << e.what() << '\n';
        return EXIT_FAILURE;
    }
    catch (const http::ResponseError &e)
    {
        std::cerr << "Response error: " << e.what() << '\n';
        return EXIT_FAILURE;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << '\n';
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}