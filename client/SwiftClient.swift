
Swift Client:
```swift
import Foundation

struct User: Codable {
    var name: String
    var age: Int
    var gender: String
    var email: String
    var phone: String
    var address: String
}

let BASE_URL = "http://localhost:8000"

func sendGetRequest(endpoint: String) -> String? {
    guard let url = URL(string: "\(BASE_URL)\(endpoint)") else {
        return nil
    }
    var request = URLRequest(url: url)
    request.httpMethod = "GET"

    do {
        let data = try NSURLConnection.sendSynchronousRequest(request, returning: nil)
        return String(data: data, encoding: .utf8)
    } catch {
        print(error.localizedDescription)
        return nil
    }
}

func sendPostRequest(endpoint: String, requestBody: String) -> String? {
    guard let url = URL(string: "\(BASE_URL)\(endpoint)") else {
        return nil
    }
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.httpBody = requestBody.data(using: .utf8)
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    do {
        let data = try NSURLConnection.sendSynchronousRequest(request, returning: nil)
        return String(data: data, encoding: .utf8)
    } catch {
        print(error.localizedDescription)
        return nil
    }
}

func sendPatchRequest(endpoint: String, id: Int, name: String, age: Int?) -> String? {
    guard let url = URL(string: "\(BASE_URL)\(endpoint)?id=\(id)&name=\(name.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)!)&age=\(age ?? -1)") else {
        return nil
    }
    var request = URLRequest(url: url)
    request.httpMethod = "PATCH"

    do {
        let data = try NSURLConnection.sendSynchronousRequest(request, returning: nil)
        return String(data: data, encoding: .utf8)
    } catch {
        print(error.localizedDescription)
        return nil
    }
}

func sendDeleteRequest(endpoint: String, id: Int) -> String? {
    guard let url = URL(string: "\(BASE_URL)\(endpoint)?id=\(id)") else {
        return nil
    }
    var request = URLRequest(url: url)
    request.httpMethod = "DELETE"

    do {
        let data = try NSURLConnection.sendSynchronousRequest(request, returning: nil)
        return String(data: data, encoding: .utf8)
    } catch {
        print(error.localizedDescription)
        return nil
    }
}

// Get all users
if let usersJson = sendGetRequest(endpoint: "/") {
    let jsonData = Data(usersJson.utf8)
    do {
        let users = try JSONDecoder().decode([User].self, from: jsonData)
        for user in users {
            print("Name: \(user.name)")
        print("Age: \(user.age)")
        print("Gender: \(user.gender)")
        print("Email: \(user.email)")
        print("Phone: \(user.phone)")
        print("Address: \(user.address)\n")
    }

    // Add a new user
    let newUser = User(name: "John Doe", age: 25, gender: "Male", email: "johndoe@example.com", phone: "+1234567890", address: "123 Main St")
    let requestBody = try! JSONEncoder().encode(newUser)
    let addUserResponse = sendPostRequest(endpoint: "/add-user/", requestBody: String(data: requestBody, encoding: .utf8)!)
    print(addUserResponse!)

    // Update a user
    let updateUserResponse = sendPatchRequest(endpoint: "/update-user/", id: 0, name: "John Smith", age: 30)
    print(updateUserResponse!)

    // Remove a user
    let removeUserResponse = sendDeleteRequest(endpoint: "/remove-user/", id: 0)
    print(removeUserResponse!)

    // Get server info
    if let serverInfoJson = sendGetRequest(endpoint: "/server-info/") {
        print(serverInfoJson)
    }

    // Null server database
    let nullResponse = sendGetRequest(endpoint: "/null/")
    print(nullResponse!)
}
}
