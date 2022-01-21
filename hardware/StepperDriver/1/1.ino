#define speeed 1  


void setup() {  
  //ALL ON
  //==========
  pinMode(8, OUTPUT); //gate 1
  pinMode(7, OUTPUT); //gate 2
  pinMode(6, OUTPUT); //gate 3
  pinMode(5, OUTPUT); //gate 4
  while(true){

    //one step
  PORTB = B00000001;
  PORTD = B01000000;
  delay(speeed *2);
  PORTB = B00000001;
  PORTD = B01000000;
  delay(speeed);
  
//two steps
  PORTB = B00000000;
  PORTD = B11000000;
  delay(speeed *2);
  PORTB = B00000000;
  PORTD = B11000000;
  delay(speeed);
//thre steps
  PORTB = B00000000;
  PORTD = B10100000;
  delay(speeed *2);
  PORTB = B00000000;
  PORTD = B10100000;

  delay(speeed); 
//foursteps
  PORTB = B00000001;
  PORTD = B00100000;
delay(speeed *2 );
  
  PORTB = B00000001;
  PORTD = B00100000;
  
  
  delay(speeed);

  }
}
