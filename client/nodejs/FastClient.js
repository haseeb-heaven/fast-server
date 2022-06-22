/*
Info : FastClient in NodeJS for FastApi connection.
Author: Haseeb Mir.
*/

var request = require("request");
const { faker } = require("@faker-js/faker");

var url = "http://localhost:8000";

function ExecuteRequest(url, method, body) {
  var resp = null;
  var options = {
    method: method,
    url: url,
    headers: { "content-type": "application/json" },
    body: body,
    json: true,
  };

  request(options, function (error, response, data) {
    if (error) throw new Error(error);
    else console.log(data);
  });
  return resp;
}

//Show user.
function ShowUser(id) {
  var userUrl = url + "/user/?id=" + id;
  ExecuteRequest(userUrl, "GET", {});
}

//Show Users
function ShowUsers() {
  ExecuteRequest(url, "GET", {});
}

//Add user.
function AddUser(body) {
  var userUrl = url + "/add-user/";
  ExecuteRequest(userUrl, "POST", body);
}

//Update user.
function UpdateUser(id, name, age) {
  var userUrl =
    url + "/update-user/?id=" + id + "&name=" + name + "&age=" + age;
  ExecuteRequest(userUrl, "PATCH", {});
}

//Remove user.
function RemoveUser(id = 0) {
  var userUrl = url + "/remove-user/?id=" + id;
  ExecuteRequest(userUrl, "DELETE", {});
}

function CreateRandomUser() {
  const rand = faker.datatype.number();
  var gender = rand % 2 == 0 ? "male" : "female";
  var name = faker.name.firstName(gender);
  return {
    name: name,
    age: faker.datatype.number(100, 15, 100),
    gender:gender,
    email: name + "_" + faker.name.lastName(gender) + "@" + faker.internet.domainSuffix() + ".com",
    phone: "+" + faker.phone.number(),
    address: faker.address.country(),
  };
}

function GenerateRandUsers(length){
    var users = [];

    Array.from({ length: length }).forEach(() => {
      users.push(CreateRandomUser());
    });
    return users;
}

async function AddUsers(length) {
    var users = GenerateRandUsers(length);
    console.time('AddUsers');
    users.forEach((user) => {
      AddUser(user);
    });
    console.timeEnd('AddUsers');
}

//Main Function area..
function main() {
  
  //Adding user.
  var user = { name: "NodeJS-Pro", age: 22, gender: "M",email: "nodejs@pro.com",phone: "+971-54545400",address: "GBR"};
  AddUser(user)

  //Adding random users.
  //AddUsers(10)

  //Updating user.
  //UpdateUser(1,'GoPro',22)

  //Removing user.
  //RemoveUser(1)

  //Show single users.
  //ShowUser(1)

  //Show all users.
  ShowUsers()
}

if (require.main === module) {
  main();
}
