int led = 6;
void setup()
{
    pinMode(led,OUTPUT);
    Serial.begin(9600);
}
void loop()

{
    for(int i = 0;i <= 255;i++)
    {
        analogWrite(led,i);
        Serial.println("hu");
        delay(10);
    }
    for(int i = 255;i >= 0;i--)
    {
        analogWrite(led,i);
        Serial.println("xi");
        delay(10);
    }
}
