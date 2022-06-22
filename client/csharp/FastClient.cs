/*
Info : FastClient in CSharp(C#) for FastApi connection.
Author: Haseeb Mir.
*/
using Bogus;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace FastClient
{
    class FastClient
    {
        internal class User
        {
            public string name { get; set; }
            public int age { get; set; }
            public string gender { get; set; }
            public string email { get; set; }
            public string phone { get; set; }
            public string address { get; set; }

            //public User()
            //{

            //}

            //public User(string name, int age, char gender, string email, string phone, string address)
            //{
            //    this.name = name; this.age = age; this.gender = gender; this.email = email; this.phone = phone; this.address = address;
            //}
        }

        private static string url = "http://localhost:8000";

        internal static string ExecuteRequest(string url)
        {
            string data = null;
            var client = new RestClient(url);
            var request = new RestRequest();
            request.Method = Method.Get;
            var response = client.Execute(request);
            if (response.StatusCode == System.Net.HttpStatusCode.OK)
                data = response.Content;
            return data;
        }

        internal static async Task<string> ExecuteRequestAsync(string url)
        {
            HttpClient client = new HttpClient();
            HttpResponseMessage response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();
            string data = await response.Content.ReadAsStringAsync();
            return data;
        }

        internal static string AddUser(User user,RestClient client)
        {
            var request = new RestRequest();
            request.Method = Method.Post;
            request.AddHeader("content-type", "application/json");
            request.AddParameter("application/json", "{\n\"name\":\"" + user.name + "\",\n\"age\":" + user.age.ToString() + ",\n\"gender\":\"" + user.gender + "\",\n\"email\":\"" + user.email + "\",\n\"phone\":\"" + user.phone + "\",\n\"address\":\"" + user.address + "\"\n}", ParameterType.RequestBody);
            var response = client.Execute(request);
            return response.Content;
        }

        internal static string AddUser(string name, int age, string gender, string email, string phone, string address)
        {
            var client = new RestClient(url + "/add-user/");
            var request = new RestRequest();
            request.Method = Method.Post;
            request.AddHeader("content-type", "application/json");
            request.AddParameter("application/json", "{\n\"name\":\"" + name + "\",\n\"age\":" + age.ToString() + ",\n\"gender\":\"" + gender + "\",\n\"email\":\"" + email + "\",\n\"phone\":\"" + phone + "\",\n\"address\":\"" + address + "\"\n}", ParameterType.RequestBody);
            var response = client.Execute(request);
            return response.Content;
        }

        internal static void AddUsers(List<User> users, bool showResponse = true)
        {
            var client = new RestClient(url + "/add-user/");
            foreach (var user in users)
            {
                var res = AddUser(user,client);
                if (showResponse)
                    Console.WriteLine(res);
            }
        }

        internal static string RemoveUser(int id)
        {
            var client = new RestClient(url + "/remove-user/?id=" + id.ToString());
            var request = new RestRequest();
            request.Method = Method.Delete;
            var response = client.Execute(request);
            return response.Content;
        }

        internal static string UpdateUser(int id = 0, string name = "", int age = -1)
        {
            var client = new RestClient(url + "/update-user/?id=" + id.ToString() + "&name=" + name + ((age != -1) ? ("&age=" + age.ToString()) : ""));
            var request = new RestRequest();
            request.Method = Method.Patch;
            var response = client.Execute(request);
            return response.Content;
        }

        internal static void ShowUsers()
        {
            var data = ExecuteRequest(url);
            dynamic jsons = JsonConvert.DeserializeObject(data);
            foreach (var json in jsons)
            {
                Console.Write("Name:" + json.name);
                Console.Write("\tAge:" + json.age);
                Console.Write("\tGender:" + json.gender);
                Console.Write("\tEmail:" + json.email);
                Console.Write("\tPhone:" + json.phone);
                Console.WriteLine("\taddress:" + json.address);
            }
        }

        //Generate random users using faker.
        internal static List<User> GenerateRandUser(int len)
        {
            var user = new Faker<User>();
            user.RuleFor(u => u.name, f => f.Person.FullName);
            user.RuleFor(u => u.age, f => f.Random.Number(15, 100));
            user.RuleFor(u => u.gender, f => f.Person.Gender == Bogus.DataSets.Name.Gender.Male ? "Male" : "Female");
            user.RuleFor(u => u.email, f => f.Person.Email);
            user.RuleFor(u => u.phone, f => "+" + f.Person.Phone.ToString());
            user.RuleFor(u => u.address, f => f.Person.Address.Street);

            var users = user.Generate(len);
            return users;
        }

        static async Task Main(string[] args)
        {
            //Add user.
            var users = GenerateRandUser(10);

            // var stopwatch = new Stopwatch();
            // stopwatch.Start();
            AddUsers(users);

            // stopwatch.Stop();
            // double elapsed_time = stopwatch.ElapsedMilliseconds / 1000;
            // Console.WriteLine("Time took " + elapsed_time + "s");

            //Update user.
            //var data = UpdateUser(1, "Akil", 25);
            //Console.WriteLine(data);

            //Remove user.
            //var data = RemoveUser(1);
            //Console.WriteLine(data);

            //Show Users.
            ShowUsers();
        }
    }
}
