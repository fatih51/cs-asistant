using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;

namespace Asistan
{
    public partial class Asistan : Form
    {
        public Asistan()
        {
            InitializeComponent();
        }
        public void launchBrowser()
        {
            string browserName = "iexplore.exe";
            using (RegistryKey userChoiceKey = Registry.CurrentUser.OpenSubKey(@"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"))
            {
                if (userChoiceKey != null)
                {
                    object progIdValue = userChoiceKey.GetValue("Progid");
                    if (progIdValue != null)
                    {
                        if (progIdValue.ToString().ToLower().Contains("chrome"))
                            browserName = "chrome.exe";
                        else if (progIdValue.ToString().ToLower().Contains("firefox"))
                            browserName = "firefox.exe";
                        else if (progIdValue.ToString().ToLower().Contains("safari"))
                            browserName = "safari.exe";
                        else if (progIdValue.ToString().ToLower().Contains("opera"))
                            browserName = "opera.exe";
                    }
                }
            }
            System.Diagnostics.Process.Start(browserName);
        }

        protected void richTextBoxkomut_TextChanged(object sender, EventArgs e)
        {
            Takvim takvim = new Takvim();
            takvim.Hide();

            if (richTextBoxkomut.Text.ToLower() == "arama")
            {
                launchBrowser();
            }
            else if (richTextBoxkomut.Text.ToLower() == "takvim")
            {
                takvim.Show();
            }
            else if (richTextBoxkomut.Text.ToLower() == "hesap makinesi")
            {
                string myPath = @"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Calculator.lnk";
                System.Diagnostics.Process islem = new System.Diagnostics.Process();
                islem.StartInfo.FileName = myPath;
                islem.Start();
            }
            else if (richTextBoxkomut.Text.ToLower() == "youtube") 
            {
                System.Diagnostics.Process.Start("https://www.youtube.com/?hl=tr&gl=TR");
            }
            else if (richTextBoxkomut.Text.ToLower() == "vikipedi") 
            {
                System.Diagnostics.Process.Start("https://tr.wikipedia.org/wiki/Anasayfa");
            }
            else if (richTextBoxkomut.Text.ToLower() == "çeviri") 
            {
                System.Diagnostics.Process.Start("https://translate.google.com.tr/");
            }
            else if (richTextBoxkomut.Text.ToLower() == "müzik") 
            {
                System.Diagnostics.Process.Start("https://www.spotify.com/tr/");
            }
            else if (richTextBoxkomut.Text.ToLower() == "hava") 
            {
                System.Diagnostics.Process.Start("https://www.mgm.gov.tr/");
            }
            else if (richTextBoxkomut.Text.ToLower() == "lig") 
            {
                System.Diagnostics.Process.Start("https://www.tff.org/default.aspx?pageID=198");
            }
            else if (richTextBoxkomut.Text.ToLower() == "ders") 
            {
                string myPath = @"C:\Users\Güçlü\Desktop\EBA CANLI DERS FATİH İÇİN İNDİRİLENLER\BİLGİSAYAR\PyQt5 Arayüz Tasarımı\ders notları iki özel tasarım\Yeni klasör\Yeni klasör\dist\Ders.exe";
                System.Diagnostics.Process islem = new System.Diagnostics.Process();
                islem.StartInfo.FileName = myPath;
                islem.Start();
            }
            else if (richTextBoxkomut.Text.ToLower() == "wp") 
            {
                System.Diagnostics.Process.Start("https://web.whatsapp.com");
            }
        }
    }  
}
