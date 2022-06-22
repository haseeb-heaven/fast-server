/*
Info : FastClient in GoLang for FastApi connection.
Author: Haseeb Mir.
*/

package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"strings"
)

var url = "http://localhost:8000"

func ExecuteRequest(url string, method string, payload string) string {
	var data = strings.NewReader(payload)
	var req, _ = http.NewRequest(method, url, data)
	var res, _ = http.DefaultClient.Do(req)

	defer res.Body.Close()
	var body, _ = ioutil.ReadAll(res.Body)
	return string(body)
}

func AddUser(name string, age int, gender string, email string, phone string, address string) string {
	var user_url = url + "/add-user/"
	var payload = "{\n\"name\":\"" + name + "\",\n\"age\":" + strconv.Itoa(age) + ",\n\"gender\":\"" + gender + "\",\n\"email\":\"" + email + "\",\n\"phone\":\"" + phone + "\",\n\"address\":\"" + address + "\"\n}"
	var resp = ExecuteRequest(user_url, "POST", payload)
	return resp
}

func GetUsers() string {
	var resp = ExecuteRequest(url, "GET", "")
	return resp
}

func UpdateUser(id int, name string, age int) string {
	var user_url = url + "/update-user/?id=" + strconv.Itoa(id) + "&name=" + name + "&age=" + strconv.Itoa(age)
	var resp = ExecuteRequest(user_url, "PATCH", "")
	return resp
}

func RemoveUser(id int) string {
	var user_url = url + "/remove-user/?id=" + strconv.Itoa(id)
	var resp = ExecuteRequest(user_url, "DELETE", "")
	return resp
}

func GetUser(id int) string {
	var user_url = url + "/user/?id=" + strconv.Itoa(id)
	var resp = ExecuteRequest(user_url, "GET", "")
	return resp
}

func main() {

	//Add user.
	var data = AddUser("GoLang", 13, "M", "goPro@gmail.com", "+971-545454", "GO")
	fmt.Println(data)

	//Update user.
	//var data = UpdateUser(0, "HaseebHM", 32)
	//fmt.Println(data)

	//Remove user.
	// var data = RemoveUser(1)
	// fmt.Println(data)

	//Show single user.
	//var data = GetUser(0)
	//fmt.Println(data)

	//Show all user.
	data = GetUsers()
	fmt.Println(data)
}
