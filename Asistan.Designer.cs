namespace Asistan
{
    partial class Asistan
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Asistan));
            this.label1 = new System.Windows.Forms.Label();
            this.richTextBoxkomut = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.label1.Location = new System.Drawing.Point(12, 42);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(271, 31);
            this.label1.TabIndex = 1;
            this.label1.Text = "Ne Yapmak İstersiniz";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // richTextBoxkomut
            // 
            this.richTextBoxkomut.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.richTextBoxkomut.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.richTextBoxkomut.Cursor = System.Windows.Forms.Cursors.Hand;
            this.richTextBoxkomut.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.richTextBoxkomut.ForeColor = System.Drawing.SystemColors.HighlightText;
            this.richTextBoxkomut.Location = new System.Drawing.Point(18, 322);
            this.richTextBoxkomut.Multiline = false;
            this.richTextBoxkomut.Name = "richTextBoxkomut";
            this.richTextBoxkomut.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.richTextBoxkomut.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.None;
            this.richTextBoxkomut.Size = new System.Drawing.Size(389, 48);
            this.richTextBoxkomut.TabIndex = 4;
            this.richTextBoxkomut.Text = "";
            this.richTextBoxkomut.TextChanged += new System.EventHandler(this.richTextBoxkomut_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 19F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.label2.Location = new System.Drawing.Point(13, 94);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(386, 120);
            this.label2.TabIndex = 5;
            this.label2.Text = "Fonksiyonlar\r\n(Arama,Takvim,Hesap Makinesi,\r\nYoutube,Vikipedi,Çeviri,Müzik,\r\nHava" +
                ",Lig,Whats App(wp))";
            // 
            // Asistan
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.ClientSize = new System.Drawing.Size(419, 461);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.richTextBoxkomut);
            this.Controls.Add(this.label1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximumSize = new System.Drawing.Size(435, 500);
            this.MinimumSize = new System.Drawing.Size(435, 500);
            this.Name = "Asistan";
            this.Text = "Asistan";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RichTextBox richTextBoxkomut;
        private System.Windows.Forms.Label label2;

    }
}

