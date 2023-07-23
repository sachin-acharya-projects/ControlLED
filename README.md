# Control LED

---------------

GUI for controlling built-in LED of Nodemcu made using Python. This application helps to `TURN ON` and `TURN OFF` the build-in LED of Nodemcu over the internet.

## Contents

-   [Controller.py](./Controller.py), This is a GUI for controlling LED light
-   [Controller.ui](./Controller.ui), Markup for GUI
-   [resources_rc.py](./resources_rc.py), Defination of Assets (icons)
-   [SerialConnection.py](./packages/SerialConnection.py), Read Serial Connection Data. For monitoring ESP8266.
-   [resources.qrc](./assets/resources.qrc), Markup for resources

## Request

Send `GET` request to Local IP (http://192.168.1.75/param), set `param = 1` for `ON` and `param = 0` for `OFF`
