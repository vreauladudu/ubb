﻿using System;
using System.Windows.Forms;

namespace sgbd
{
    internal static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Moto());
        }
    }
}