import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class JavaClient {
    private static final String BASE_URL = "http://localhost:8000";

    public static void main(String[] args) {
        try {
            // Get all users
            String usersJson = getResponse("/");

            // Parse JSON to User objects
            Gson gson = new GsonBuilder().create();
            User[] users = gson.fromJson(usersJson, User[].class);

            // Print user details
            for (User user : users) {
                System.out.println("Name: " + user.getName());
                System.out.println("Age: " + user.getAge());
                System.out.println("Gender: " + user.getGender());
                System.out.println("Email: " + user.getEmail());
                System.out.println("Phone: " + user.getPhone());
                System.out.println("Address: " + user.getAddress());
                System.out.println();
            }

            // Add a new user
            User newUser = new User("John Doe", 25, "Male", "johndoe@example.com", "+1234567890", "123 Main St");
            String addUserResponse = postResponse("/add-user/", gson.toJson(newUser));
            System.out.println(addUserResponse);

            // Update a user
            String updateUserResponse = patchResponse("/update-user/", "0", "John Smith", "30");
            System.out.println(updateUserResponse);

            // Remove a user
            String removeUserResponse = deleteResponse("/remove-user/", "0");
            System.out.println(removeUserResponse);

            // Get server info
            String serverInfoJson = getResponse("/server-info/");
            System.out.println(serverInfoJson);

            // Null server database
            String nullResponse = getResponse("/null/");
            System.out.println(nullResponse);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String getResponse(String endpoint) throws IOException {
        URL url = new URL(BASE_URL + endpoint);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();

        return content.toString();
    }

    private static String postResponse(String endpoint, String requestBody) throws IOException {
        URL url = new URL(BASE_URL + endpoint);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json");

        con.setDoOutput(true);
        con.getOutputStream().write(requestBody.getBytes("UTF-8"));

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();

        return content.toString();
    }

    private static String patchResponse(String endpoint, String id, String name, String age) throws IOException {
        URL url = new URL(BASE_URL + endpoint + "?id=" + id + "&name=" + URLEncoder.encode(name, "UTF-8") + "&age=" + age);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("PATCH");

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder content = null;
        while ((inputLine = in.readLine()) != null) {
        content.append(inputLine);
    }
    in.close();

    return content.toString();
}

private static String deleteResponse(String endpoint, String id) throws IOException {
    URL url = new URL(BASE_URL + endpoint + "?id=" + id);
    HttpURLConnection con = (HttpURLConnection) url.openConnection();
    con.setRequestMethod("DELETE");

    BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuilder content = new StringBuilder();
    while ((inputLine = in.readLine()) != null) {
        content.append(inputLine);
    }
    in.close();

    return content.toString();
}
}

