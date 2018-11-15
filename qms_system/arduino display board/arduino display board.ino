/*
  Quick demo of major drawing operations on a single DMD
 */

#include <SPI.h>
#include <DMD2.h>
#include <fonts/SystemFont5x7.h>

SoftDMD dmd(1,1);  // DMD controls the entire display

String messagea  = "C00ab,C00cd,C00ef,C00gh,C00ij,C00kl,C00mn,C00op,C00qr,C00st";
String messageb  = "";
String messagec  = "";
String messaged  = "";

String message1 = "";
String message2 = "";
String message3 = "";
String message4 = "";


String message5 = "";
String message6 = "";
String message7 = "";


String message8 = "";
String message9 = "";
String message10 = "";


String Mech1 = "";
String Mech2 = "";
String Mech3 = "";
String Mech4 = "";
String Mech5 = "";
String Mech6 = "";
String Mech7 = "";
String Mech8 = "";
String Mech9 = "";
String Mech10 = "";



// the setup routine runs once when you press reset:
void setup() {
  dmd.setBrightness(255);
  dmd.selectFont(SystemFont5x7);
  dmd.begin();
 Serial.begin(9600);
  // Circle with a line at a tangent to it
 /* dmd.drawCircle(24,8,5);
  dmd.drawLine(14,9,28,15);

  // Outline box containing a filled box
  dmd.drawBox(6,10,11,15);
  dmd.drawFilledBox(8,12,9,13);*/
}

int btime = 1000;

// the loop routine runs over and over again forever:
void loop() {
  
   
  while (Serial.available())
   messagea = Serial.readString();
  if (messagea != "")
  {
    Serial.println(messagea);
  }
  else
{
 // messagea = "C00ab,C00cd,C00ef,C00gh,C00ij,C00kl,C00mn,C00op,C00qr,C00st";
//    messagea = "C00**,C00**,C00**,C00**,C00**,C00**,C00**,C00**,C00**,C00**";
} 
 Serial.println(messagea);
messageb = messagea;
messagec = messagea;
messaged = messagea;

  message1= messagea.substring(0,3);
  Mech1=messagea.substring(3,5);
  
  message2= messageb.substring(6,9);
  Mech2=messagea.substring(9,11);
  
  message3 =messagec.substring(12,15);
  Mech3=messagea.substring(15,17);
  
  message4= messaged.substring(18,21);
  Mech4=messagea.substring(21,23);
  
  message5= messageb.substring(24,27);
  Mech5=messagea.substring(27,29);
  
  message6 =messagec.substring(30,33);
  Mech6=messagea.substring(33,35);
  
  message7= messaged.substring(36,39);
  Mech7=messagea.substring(39,41);
  
  message8= messageb.substring(42,45);
  Mech8=messagea.substring(45,47);
  
  message9 =messagec.substring(48,51);
  Mech9=messagea.substring(51,53);
  
  message10= messaged.substring(54,57);
  Mech10=messagea.substring(57);
  
  
  Serial.println("************");
  Serial.println(message1);
  
  Serial.println(message2);
  Serial.println(message3);
  Serial.println(message4);
  /*
  
  Serial.println("R1:" + Mech1+ "-" + message1);
  Serial.println("R2:" + Mech2+ "-" + message2);
  Serial.println("R3:" + Mech3+ "-" + message3);
  Serial.println("R4:" + Mech4+ "-" + message4);
  Serial.println("R5:" + Mech5+ "-" + message5);
  Serial.println("R6:" + Mech6+ "-" + message6);
  Serial.println("R7:" + Mech7+ "-" + message7);
  Serial.println("R8:" + Mech8+ "-" + message8);
  Serial.println("R9:" + Mech9+ "-" + message9);
  Serial.println("R10:" + Mech10+ "-" + message10);
  
  */
  
  
  dmd.drawString(0,0,"R1:"+Mech1);
   dmd.drawString(12,8,message1);
   delay (btime);
   
  dmd.drawString(0,0,"                 ");
   dmd.drawString(12,8,"     ");
   delay (btime);
   
    dmd.drawString(0,0,"R2:"+Mech2);
   dmd.drawString(12,8,message2);
   delay (btime);
    
  dmd.drawString(0,0,"                    ");
   dmd.drawString(12,8,"       ");
   delay (btime);
   
   dmd.drawString(0,0,"R3:"+Mech3);
   dmd.drawString(12,8,message3);
   delay (btime);
   
  dmd.drawString(0,0,"                   ");
   dmd.drawString(12,8,"      ");
   delay (btime);
   
    dmd.drawString(0,0,"R4:"+Mech4);
   dmd.drawString(12,8,message4);
   delay (btime);
      
  dmd.drawString(0,0,"                   ");
   dmd.drawString(12,8,"     ");
   delay (btime);


   
    dmd.drawString(0,0,"R5:"+Mech5);
   dmd.drawString(12,8,message5);
   delay (btime);
   
  dmd.drawString(0,0,"                       ");
   dmd.drawString(12,8,"        ");
   delay (btime);


   
    dmd.drawString(0,0,"R6:"+Mech6);
   dmd.drawString(12,8,message6);
   delay (btime);
    
  dmd.drawString(0,0,"                       ");
   dmd.drawString(12,8,"        ");
   delay (btime);



   
    dmd.drawString(0,0,"R7:"+Mech7);
   dmd.drawString(12,8,message7);
   delay (btime);
   
  dmd.drawString(0,0,"                      ");
   dmd.drawString(12,8,"       ");
   delay (btime);



   
    dmd.drawString(0,0,"R8:"+Mech8);
   dmd.drawString(12,8,message8);
   delay (btime);
   
  dmd.drawString(0,0,"                       ");
   dmd.drawString(12,8,"        ");
   delay (btime);



   
    dmd.drawString(0,0,"R9:"+Mech9);
   dmd.drawString(12,8,message9);
   delay (btime);
   
  dmd.drawString(0,0,"                      ");
   dmd.drawString(12,8,"        ");
   delay (btime);

   
    dmd.drawString(0,0,"R10:"+Mech10);
   dmd.drawString(12,8,message10);
   delay (btime);
    
  dmd.drawString(0,0,"                           ");
   dmd.drawString(12,8,"          ");
   delay (btime);
}
