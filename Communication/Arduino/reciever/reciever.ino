#include <VirtualWire.h>
void setup()
{
  Serial.begin(9600);
  //Serial.println("Listening");
  vw_setup(2000);
  vw_rx_start();
}
void loop()
{
  byte message[VW_MAX_MESSAGE_LEN];
  byte messageLength = VW_MAX_MESSAGE_LEN;
  if (vw_get_message(message, &messageLength))
  {
    for (int i = 0; i < messageLength; i++)
    {
      Serial.write(message[i]);
    }
    Serial.println();
  }
}
