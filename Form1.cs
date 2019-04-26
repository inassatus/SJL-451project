using Npgsql;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace WindowsFormsApp1
{
    public partial class Milestone3 : Form
    {
        public string userid;

        public Milestone3()
        {
            InitializeComponent();
        }

        private void user_TextChanged(object sender, EventArgs e)
        {
            using (var conn = new NpgsqlConnection("Host = localhost; Username=postgres; Password=0815; Database=yelpdb;")) {
                conn.Open();
                using (var cmd = new NpgsqlCommand()) {
                    cmd.Connection = conn;
                    cmd.CommandText = "Select * from userTable where userTable.name LIKE '" + user.Text + "%';";

                    using (var reader = cmd.ExecuteReader()) {
                        users.Items.Clear();
                        while (reader.Read()) {
                            users.Items.Add(reader.GetString(0));
                        }
                    }
                }
                conn.Close();
            }
        }

        private void users_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (users.SelectedItem != null) {
                userid = users.SelectedItem.ToString();
            }
        }
    }
}
