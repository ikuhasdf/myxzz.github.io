#include <Servo.h>

Servo myServo; // 舵机命名
int angle;  // 设定角度

void setup() {
  // put your setup code here, to run once:
  myServo.attach(2); // 选择2号引脚
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()==0); // 等待输入
  angle=Serial.parseInt();
  Serial.print("角度是：");
  Serial.println(angle); // 输出角度
  myServo.write(angle);
  delay(1000);
}
