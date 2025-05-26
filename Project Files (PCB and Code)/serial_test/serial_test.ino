void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(1, OUTPUT);
int port = 3;
int f = 0;
String var = "default";
String ser = "idk";
}

void loop() {
  // put your main code here, to run repeatedly:
  int port = 3;
  
 
int f;
ser = Serial.read();
switch (ser){
  case 'a':
    var = "TMP"
  break
   case 'b':
    var = "BP"
  break
  
  case 'c':
    var = "HR"
  break
if (digitalRead(port) == LOW) {                         // the light was flashed 10 time?
       for (int c=0; c < 255; c++){
      Serial.println(var);
      Serial.print(c);
      delay(50);
       }
      }
      }
      //Serial.print("1");
//      Serial.print("2");
//      Serial.print("3");
      
    
                                           // wait 250ms   
       
  }
}
  
