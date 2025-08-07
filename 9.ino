void setup()
{
  // put your setup code here, to run once:
  pinMode(3,OUTPUT);
  pinMode(9,OUTPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  analogWrite(3,255);
  analogWrite(9,0);
  delay(1000);
  analogWrite(3,0);
  analogWrite(9,255);
  delay(1000);
}
