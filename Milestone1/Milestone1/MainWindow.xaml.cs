using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Npgsql;

namespace Milestone1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public class Business
        {
            public string name { get; set; }
            public string state { get; set; }
        }
        public MainWindow()
        {
            InitializeComponent();
            addStates();
            addColums2Grid();
        }
        private string buildConnString()
        {
            return "Host=localhost; Username=postgres; Password=password; Database=milestone1db";

        }

        public void addStates()
        {
            using (var comm = new NpgsqlConnection(buildConnString()))
            {
                comm.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = comm;
                    cmd.CommandText = "SELECT distinct state FROM business ORDER BY state;";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            stateList.Items.Add(reader.GetString(0));
                        }
                    }
                }
                comm.Close();
            }
        }

        public void addColums2Grid()
        {
            DataGridTextColumn col1 = new DataGridTextColumn();
            col1.Header = "Business Name";
            col1.Binding = new Binding("name");
            col1.Width = 255;
            businessGrid.Columns.Add(col1);

            DataGridTextColumn col2 = new DataGridTextColumn();
            col2.Header = "State";
            col2.Binding = new Binding("state");
            businessGrid.Columns.Add(col2);
        }

        private void StateList_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            businessGrid.Items.Clear();
            if (stateList.SelectedIndex > -1)
            {
                using (var comm = new NpgsqlConnection(buildConnString()))
                {
                    comm.Open();
                    using (var cmd = new NpgsqlCommand())
                    {
                        cmd.Connection = comm;
                        cmd.CommandText = "SELECT name,state FROM business WHERE state = '" + stateList.SelectedItem.ToString() + "';";
                        using (var reader = cmd.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                businessGrid.Items.Add(new Business() { name = reader.GetString(0), state = reader.GetString(1) });
                            }
                        }
                    }
                    comm.Close();
                }
            }
        }
    }
}
