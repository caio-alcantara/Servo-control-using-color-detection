# Servo-control-using-color-detection
 Arduino and Python code to find the coordinate of a green object in the screen, and change the servo motor position according to the object position.

Tutorial (PT-BR) - Ubuntu 18.04 / 20.04
Para usar o programa, você deve ter instalado no seu computador o interpretador Python, alguma distribuição do ROS 1, e as bibliotecas que são utilizadas no código, incluindo a ROSSERIAL. Além disso, não se esqueça de upar o código do arduino no controlador (também é necessário ter a biblioteca do ROS instalada no Arduino IDE).
Primeiro, crie um workspace com o catkin, e depois crie um pacote com as dependências rospy, std_msgs, e cv_bridge. Coloque o arquivos de código dentro deste pacote.
Numa janela de terminal, utilize o comando "source /opt/ros/suaDistroDoRos/setup.bash", e rode o roscore. Em outra janela do terminal, rode novamente o source, e rode o node do ROSSERIAL com "rosrun rosserial_python serial_node.py /dev/ttyACM0". Neste ponto, o led do arduino deve começar a piscar. Novamente, abra outra janela do terminal, vá até o diretório do seu pacote catkin e rode "source /devel/setup.bash". Após isso, rode "rosrun nomeDoSeuPacote servo_cam_ofc.py". O programa deverá ser inicializado e tudo correrá normalmente. 

Qualquer dúvida, contate-me pessoalmente via email: caioalcantarasantos3@gmail.com
