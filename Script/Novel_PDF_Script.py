#Author : Mohammad Ahmed Mayariwala
#Date: 2022-08-25

from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fpdf import FPDF
import urllib.request
import os
import time


def header(title):
    pdf.set_font('helvetica', 'B', 19)
    # Calculate width of title and position
    title_w = pdf.get_string_width(title) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    # colors of frame, background, and text
    pdf.set_draw_color(0, 80, 180) # border = blue
    pdf.set_fill_color(255, 229, 204) # background = nude 
    pdf.set_text_color(0, 0, 0) # text = balck
    # Thickness of frame (border)
    pdf.set_line_width(1)
    # Title
    pdf.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
    # Line break
    pdf.ln(10)

def titlee(title):
    pdf.set_font('helvetica', 'b', 16)
    # background color
    pdf.set_fill_color(200, 220, 255)
    pdf.set_text_color(0, 0, 0)
    # Chapter title

    pdf.cell(0, 5, title, ln=1, fill=1,align="C")
    # line break
    pdf.ln()

def body(txt):
    pdf.set_font('times', '', 16)
    pdf.set_fill_color(0, 0, 0) # background = yellow
    pdf.set_text_color(0, 0, 0)
        # insert text
    
    pdf.multi_cell(0, 10, txt)
        # line break
    pdf.ln()
        # end each chapter
    pdf.set_font('times', 'I', 16)
    pdf.cell(0, 5, 'END OF CHAPTER')
    pdf.ln(30)
    
def print_pdf(title,txt):
    titlee(title)
    body(txt)

pdf =FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_auto_page_break(auto = True, margin = 15)
count=0
os.system('cls') 

i= int(input("1st chapter number : "))
p=i
lst= int(input("last chapter number : "))+1
os.system('cls') 
print("hold up retriving ur novel...")

z=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
while i < lst:

#you can replace this your URL as well jus remember to copy ur url before the chapter number
    url='https://tales.xperimentalhamid.com/novel/the-proxy-bride-of-the-billionaire-chapter-'+str(i)+'/'
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,'html.parser')

    #if there are more images you can change the if conditions accordingly 
    images = soup.find_all("img", class_="attachment-full size-full")
    number="0"+".png"
    if count== 0:   
        for image in images:
            image_src =image["src"]
            urllib.request.urlretrieve(image_src,str(number))
            number=+1

    
    heading = soup.find('h1',class_="entry-title") 
    heading=heading.text
    index = heading.index("Chapter")
    title= heading[:index-1]
    c_title =heading[index:]
    
    
    a=[]
    articals= soup.find_all("p")
    for artical in articals:
        a.append(artical.text)
    b=a[4:]
    b=b[:-6]
    all_ =[]
    for a in b:
        a=a.replace('“','"').replace('”','""').replace("’","`").replace("é","e").replace("…","...").replace('""','"').replace("—" ,"-").replace("–" ,"-").replace("charmap","chr")
        all_.append(a)
        z.append(a)
    b=all_

    with open('try.txt', 'w') as fp:
        for item in b:
            # write each item on a new line
            fp.write("%s\n" % item)
        
    str1=""
    for item in b:
        str1+=("%s\n" % item)
    splited = str1.split("\n")    

    with open ("try.txt","r") as fp:
        q=fp.read()
    if count == 0:
        header(title)
        pdf.image("0.png",x=-0.5,w=pdf.w+1)
        #count+=1
    else:
        pass
    
    if count==round((30/100)*(lst-p)):
        print('25% completed')
    elif count==round((50/100)*(lst-p)):
        print("50% completed")
    elif count==round((75/100)*(lst-p)):
        print("75% Sheeshh")
    count+=1
    print_pdf(c_title,q)
    #pdf.add_page()
    
    i+=1

os.remove("try.txt")
os.remove("0.png")
os.system("cls")
pdf.output(f'{title}.pdf')


print(f"Your novel has been created :\n file name is  {title}.pdf \n total number of chapters downloaded = {count}")
   