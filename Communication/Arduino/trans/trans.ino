#include <VirtualWire.h>
char inData[50];
int newmessage = 0;
void setup() {
  vw_setup(2000);
  vw_set_tx_pin(12);
  Serial.begin(9600);
}
void loop()
{
  char inChar;
  byte index = 0;
  char mss[20];
  while (Serial.available() > 1) {
    if (index < 49)
    {
      delay(10);
      inChar = Serial.read();
      inData[index] = inChar;
      index++;
      inData[index] = '\0';
    }
    newmessage = 1;
  }
  if (newmessage == 1) {
    sprintf(mss,inData);
    vw_send((uint8_t *)mss, strlen(mss));
    vw_wait_tx();
    //Serial.println(mss);
    delay(600);
    newmessage = 0; // Indicate that there is no new message to wait for the new one
  }
}


