
void setup() {
  // put your setup code here, to run once:
  pinMode(A5, INPUT); // 设定A5引脚的模式
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i = analogRead(A5); // 从指定的模拟输入引脚读取值。
  Serial.print("水滴的数值是（没水时水滴值是1023-1024，有水时水滴值降低）：");
  Serial.println(i);  //打印从指定的模拟输入引脚读取值。
  delay(1000); //延时1000毫秒
}
